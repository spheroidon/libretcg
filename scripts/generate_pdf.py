import os
import sys
import time
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class PDFGenerator:
    def create_pdf(self, pdf_filename, images):
        # Define page size
        page_width, page_height = letter
        
        # Define image size and spacing
        img_width = 2 * inch
        img_height = 3 * inch
        spacing = (1/4) * inch

        # Calculate total width and height of the grid
        total_width = 3 * img_width + 2 * spacing
        total_height = 3 * img_height + 2 * spacing
        
        # Create a canvas
        c = canvas.Canvas(pdf_filename, pagesize=letter)

        # Function to draw images on the page
        def draw_images(image_subset):
            x_offset = (page_width - total_width) / 2
            y_offset = (page_height - total_height) / 2

            for row in range(3):
                for col in range(3):
                    x = x_offset + col * (img_width + spacing)
                    y = y_offset + row * (img_height + spacing)
                    image_index = row * 3 + col
                    if image_index < len(image_subset):
                        c.drawImage(image_subset[image_index], x, y, width=img_width, height=img_height)

        # Add images to each page
        num_pages = -(-len(images) // 9)  # Ceiling division
        for page in range(num_pages):
            print(f"Generating page {page + 1}/{num_pages}")
            draw_images(images[page * 9:(page + 1) * 9])
            c.showPage()

        c.save()

    def generate_pdf_from_input(self):
        self.card_data_dir = './printables/cards/'
        self.card_data_list = []

        try:
            card_data_dir_input = sys.argv[1]
        except IndexError:
            card_data_dir_input = input("Expansion name: ").strip()
        except KeyboardInterrupt:
            print("Exiting...")
            return
        
        try:
            card_names_input = sys.argv[2]
        except IndexError:
            card_names_input = input("Cards to generate (comma-separated, leave empty for all): ").strip()
        except KeyboardInterrupt:
            print("Exiting...")
            return
        
        self.card_data_dir = os.path.join(self.card_data_dir, card_data_dir_input)
        
        # Check if the expansion name is valid
        if not os.path.exists(self.card_data_dir) or not os.path.isdir(self.card_data_dir) or card_data_dir_input.strip() == '':
            print(f"Error: '{card_data_dir_input}' is not valid. Defaulting to '00_base'.")
            self.card_data_dir = './printables/cards/00_base'

        # Get card names or default to all cards in the directory
        if card_names_input.strip() != '':
            card_names = [name.replace('.png', '').replace(' ', '_').strip() + '.png' for name in card_names_input.split(',')]
            for card in card_names:
                card_info_list = card.split('*')
                num = 1
                if len(card_info_list) == 2 and card_info_list[0].isdigit():
                    num = int(card_info_list[0])
                    card = card_info_list[1]
                for _ in range(num):
                    self.card_data_list.append(card)
            print(self.card_data_list)
            
            for card in self.card_data_list:
                if not os.path.exists(os.path.join(self.card_data_dir, card)):
                    print("Error: One or more card names are invalid.")
                    return
        else:
            self.card_data_list = [f for f in os.listdir(self.card_data_dir) if f.endswith('.png')]

        if not self.card_data_list:
            print(f"Error: No cards found in directory '{self.card_data_dir}'.")
            return
        
        output_path = os.path.abspath(f"./output_{card_data_dir_input}_{int(time.time())}.pdf")
        
        images = [os.path.join(self.card_data_dir, card) for card in self.card_data_list]
        self.create_pdf(output_path, images)
        print(f"PDF created successfully at {output_path}")

def main():
    pdf_generator = PDFGenerator()
    pdf_generator.generate_pdf_from_input()

if __name__ == "__main__":
    main()
