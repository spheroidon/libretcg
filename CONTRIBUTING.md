### Contribution Guide for Open-Source Trading Card Game

Thank you for considering contributing to the LibreTCG project! This guide will help you understand how you can contribute effectively while adhering to our guidelines.

#### Contribution Guidelines

1. **Fork the Repository**
   - Fork the repository to your GitHub account.

2. **Clone the Repository**
   - Clone the forked repository to your local machine:
     ```
     git clone https://github.com/spheroidon/LibreTCG.git
     ```

3. **Explore the Project**
   - Familiarize yourself with the project structure and existing cards.

4. **Adding New Cards**

   - **Card Template**:
      ```json
      {
         "author": "LibreTCG",
         "name": "Example",
         "health": 60,
         "power": 100,
         "action": "Deal 20 damage to an\nenemy card of your choice.",
         "lore": "This is a template!",
         "image": "example.png",
         "font": "roboto-medium.ttf",
         "text_color": [255, 255, 255],
         "text_outline": 3,
         "text_outline_color": [2, 2, 2],
         "text_outline_blur": 0
      }
      ```

   - **Requirements**:
     - **author**: The contributor's name/username. If credit is unwanted, set to "LibreTCG".
     - **name**: The name of the card.
     - **health**: The health points of the card.
     - **power**: The power level of the card.
     - **action**: The action or ability of the card.
     - **lore**: Lore or flavor text describing the card.
     - **image**: Image filename of the card (must be included in the repository under `./assets/images/`). 900 by 1350 pixels, border shouldn't be larger than 25 pixels.
     - **font**: Font file used for text.
     - **text_color**: RGB color values for text.
     - **text_outline**: Radius of the text's outline. Set to 0 to disable.
     - **text_outline_color**: RGB color values for the text's outline.
     - **text_outline_blur**: Radius for blurring the text's outline. Set to 0 to disable.

   - **Modify Cards**:
     - You may modify existing cards for balancing or grammatical errors only.

5. **Submitting Changes**

   - **Commit**:
     - Commit your changes with a descriptive commit message:
       ```
       git commit -m "Add Example card"
       ```

   - **Push**:
     - Push your changes to your fork:
       ```
       git push origin master
       ```

   - **Pull Request**:
     - Submit a pull request from your fork to the main repository.
     - Ensure the pull request description clearly describes the changes made.

6. **Review Process**
   - Your pull request will be reviewed by project maintainers.
   - Feedback may be given for further improvements or adjustments.

7. **Legal Requirements**
   - All assets used (images, scripts, cards) must be licensed under terms compatible with CC-BY-SA.

8. **Respect Project Rules**
   - Do not modify core rules, contribution guide, readme, or any of the scripts, except for grammatical errors or bug fixes.

#### Code of Conduct

- Follow the project's [code of conduct](./CODE_OF_CONDUCT.md) at all times.
- Respect other contributors and maintainers.

#### Get Help

- If you need any assistance, feel free to reach out to maintainers through GitHub issues.