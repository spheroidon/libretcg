"""
A script to generate card images based on user input.
"""

import json
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CARD_WIDTH, CARD_HEIGHT = 900, 1350

class CardGenerator:
    """
    A class to generate card images.
    """

    def __init__(self, assets_dir='./assets', expansion='', card_data_list=[]):
        self.assets_dir = assets_dir
        self.card_data_dir = './cards/'+expansion
        self.printables_dir = './printables/cards/'+expansion
        self.card_data_list = card_data_list

    def save_card_image(self, card_image, card_name):
        """
        Save the provided card image to the printables directory.
        """
        if not os.path.exists(self.printables_dir):
            os.makedirs(self.printables_dir)

        card_path = f"{card_name.replace(' ', '_').replace('\'', '').replace(':', '').lower()}.png"
        output_path = os.path.join(self.printables_dir, card_path)
        card_image.save(output_path)
        print(f"Card '{card_name}' generated at {output_path}")

    def generate_card_image(self, card, expansion):
        """
        Generate a card image based on the provided card data.
        """
        # Load fonts
        font_path = os.path.join(self.assets_dir, 'fonts', card.get('font', 'roboto-semibold.ttf'))
        font = ImageFont.truetype(font_path, 64)
        small_font = ImageFont.truetype(font_path, 40)
        # Create a blank card image
        card_image = Image.new('RGB', (CARD_WIDTH, CARD_HEIGHT), color=(255, 255, 255))
        draw = ImageDraw.Draw(card_image)

        # Load and resize the background image
        if 'image' in card and card['image']:
            card_image_path = os.path.join(self.assets_dir, 'images', card['image'])
            if os.path.exists(card_image_path):
                bg_img = Image.open(card_image_path)
                bg_img = bg_img.resize((CARD_WIDTH, CARD_HEIGHT))
                card_image.paste(bg_img, (0, 0))

        # Helper method to draw text with outline
        def draw_text_with_outline(draw, position, text, font):
            """
            Draw text with an outline on the card image.
            """
            outline_color = tuple(card.get('text_outline_color', [0, 0, 0]))
            text_color = tuple(card.get('text_color', [255, 255, 255]))
            text_outline = card.get('text_outline', 3)
            if text_outline > 0:
                # Draw outline first
                outline_image = Image.new('RGBA', card_image.size, (0, 0, 0, 0))
                outline_draw = ImageDraw.Draw(outline_image)

                for x in range(-text_outline, text_outline + 1):
                    for y in range(-text_outline, card['text_outline'] + 1):
                        if x == 0 and y == 0:
                            continue
                        pos = (position[0] + x, position[1] + y)
                        outline_draw.text(pos, text, font=font, fill=outline_color)
                # Apply blur if needed
                if card.get('text_outline_blur', 0) > 0:
                    radius = card.get('text_outline_blur', 0)
                    outline_image = outline_image.filter(ImageFilter.GaussianBlur(radius=radius))
                # Paste the blurred outline image over the original image
                card_image.paste(outline_image, (0, 0), outline_image)

                # Draw the text itself
                draw.text(position, text, font=font, fill=text_color)
            else:
                draw.text(position, text, font=font, fill=text_color)

        # Draw the card elements
        # Card name
        text = card['name']
        draw_text_with_outline(draw, (30, 30), text, font)

        # Lore
        text = card.get('lore', '')
        width = 0
        for c in text:
            width += small_font.getbbox(c)[2]
        x = CARD_WIDTH - width - 30  # Align to the right
        draw_text_with_outline(draw, (x, 40), text, small_font)

        # Card author
        text = f"Card by {card.get('author', 'LibreTCG')} / V{card.get('version', '1')}"
        width = 0
        for c in text:
            width += small_font.getbbox(c)[2]
        x = (CARD_WIDTH - width) / 2 # Center the line horizontally
        draw_text_with_outline(draw, (x, 1200), text, small_font)

        expansion = expansion.replace('_',' ').split(' ')[1:] # Remove the expansion number
        expansion = ' '.join(expansion).replace('/', '').replace('.', '').strip()
        expansion = expansion.title()
        text = f"Expansion: {expansion}"
        width = 0
        for c in text:
            width += small_font.getbbox(c)[2]
        x = (CARD_WIDTH - width) / 2 # Center the line horizontally
        draw_text_with_outline(draw, (x, 1260), text, small_font)

        # Card HP & Power
        text = f"HP: {card.get('health', 'N/A')} / PWR: {card.get('power', 'N/A')}"
        draw_text_with_outline(draw, (30, 110), text, font)

        # Action description
        text = card.get('action', 'N/A')
        lines = text.split('\n')

        # Calculate the height of each line
        heights = [font.getbbox(c)[3] for line in lines for c in line]
        max_height = max(heights) if heights else 0
        height = max_height * len(lines)

        # Calculate the starting y-coordinate to vertically center the text block
        start_y = (CARD_HEIGHT - height) / 2.2

        for i, line in enumerate(lines):
            width = sum(font.getbbox(c)[2] for c in line)
            x = (CARD_WIDTH - width) / 2  # Center the line horizontally
            y = start_y + i * max_height  # Position each line below the previous one

            draw_text_with_outline(draw, (x, y), line, font)

        # Save the card image
        self.save_card_image(card_image, card['name'])                

    def load_cards(self):
        """
        Load card data from the provided directory and return a list of card objects.
        """
        # Error checking
        if not os.path.exists(self.card_data_dir):
            raise FileNotFoundError(f"'{self.card_data_dir}' does not exist.")
        if not os.path.isdir(self.card_data_dir):
            raise NotADirectoryError(f"'{self.card_data_dir}' is not a directory.")
        if not os.listdir(self.card_data_dir):
            raise ValueError(f"'{self.card_data_dir}' is empty.")
        if not any(filename.endswith('.json') for filename in os.listdir(self.card_data_dir)):
            raise ValueError(f"'{self.card_data_dir}' does not contain any JSON files.")
        if not all(filename.endswith('.json') for filename in os.listdir(self.card_data_dir)):
            print(f"Warning: '{self.card_data_dir}' contains non-JSON files. Ignoring them.")

        # Load card data
        cards = []
        for filename in self.card_data_list:
            if filename.endswith('.json'):
                with open(os.path.join(self.card_data_dir, filename), 'r', encoding='utf-8') as f:
                    card = json.load(f)
                    cards.append(card)
        return cards

    def generate_cards_from_input(self):
        """
        Generate card images based on user input.
        """
        # Set up directories
        self.card_data_dir = './cards/'
        self.printables_dir = './printables/cards/'
        self.card_data_list = []

        # Get the expansion and card names from the user
        try:
            card_data_dir_input = sys.argv[1]
        except IndexError:
            card_data_dir_input = input("Expansion name: ")
        except KeyboardInterrupt:
            print("Exiting...")
            return
        try:
            card_names_input = sys.argv[2]
        except IndexError:
            card_names_input = input("Cards to generate (comma-separated, leave empty for all): ")
        except KeyboardInterrupt:
            print("Exiting...")
            return
        
        self.card_data_dir += card_data_dir_input
        self.printables_dir += card_data_dir_input
        card_names = card_names_input.split(',')

        # Create a list of filenames by processing each card name from the user input
        for card in card_names:
            formatted_card = card.strip().lower().replace(' ', '_').replace('.json', '')
            self.card_data_list.append(f"{formatted_card}.json")

        # Check if the expansion name is valid
        if not os.path.exists(self.card_data_dir) or self.card_data_dir == './cards/':
            print(f"Error: '{card_data_dir_input}' is not valid. Defaulting to '00_base'.")
            card_data_dir_input = '00_base'
            self.card_data_dir = './cards/00_base'
            self.printables_dir = './printables/cards/00_base'

        # Check if the card names are valid
        if not card_names[0]:
            print(f"Warning: No names provided. Generating all cards in '{self.card_data_dir}'.")
            self.card_data_list = os.listdir(self.card_data_dir)
        elif not all(card in os.listdir(self.card_data_dir) for card in self.card_data_list):
            print("Error: One or more card names are invalid.")
            return

        # Load and generate card images
        cards = self.load_cards()
        for card in cards:
            self.generate_card_image(card, card_data_dir_input)

def main():
    """
    Main function to initiate card generation process.
    """
    generator = CardGenerator()
    generator.generate_cards_from_input()

if __name__ == "__main__":
    main()
