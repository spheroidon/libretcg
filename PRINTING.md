# Printing Guidelines for LibreTCG

## Official Card Size

All LibreTCG cards are designed to be 2x3 inches. Ensure your printer settings are adjusted to match this size to maintain consistency and quality.

## Card Location

Individual cards are saved in the `./printables/cards/[expansion]` directory. This structure helps organize cards by expansion and makes it easier to locate and print the cards you need.

## Printable Generation Guide

To generate printable cards, you can use the `generate_printables.py` script. Follow these steps:

1. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Navigate to the script directory:**
   ```sh
   cd ./scripts
   ```

3. **Run the script:**
   ```sh
   python generate_printables.py
   ```

4. **Provide the required inputs:**
   - **Expansion Name:** Enter the name of the expansion you are working on.
   - **Comma Separated List of Card Names:** Enter the names of the cards you want to generate, separated by commas.

   Example:
   ```sh
   Expansion name: 00_base
   Cards to generate (comma-separated, leave empty to generate all): example, knights_shield, mystic_healing
   ```

5. **Locate the generated printables:**
   The script will save the generated printable cards in the `./printables/cards/[expansion]` directory.

By following these guidelines, you can easily generate and print your custom LibreTCG cards. Happy printing!