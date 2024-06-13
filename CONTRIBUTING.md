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
         "version": 1,
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
     - **version**: The current revision of the card. Start at 1, increase by 1 each time the name, action, health or power change.
     - **author**: The contributor's name/username. If credit is unwanted, set to "LibreTCG".
     - **name**: The name of the card. Must be the same as the filename, but can include spaces, special characters and have uppercase letters.
     - **health**: The health points of the card.
     - **power**: The power level of the card.
     - **action**: The action or ability of the card.
     - **lore**: Lore or flavor text describing the card.
     - **image**: Image filename of the card (must be included in the repository under `./assets/images/`). 900 by 1350 pixels, border shouldn't be larger than 25 pixels. PSD template available at `./assets/example.psd`.
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

#### Using GitHub Issues

1. **Bug Reports**
   - If you encounter issues with the scripts, use the GitHub issue tracker to submit a detailed bug report.
   - **Title**: Clearly describe the issue in the title.
   - **Description**: Provide a comprehensive description of the bug, including steps to reproduce, screenshots, and error messages, if possible.
   - **Environment Information**: Specify the platform on which the bug occurs (e.g., operating system).
   - **Expected Behavior**: Describe the expected outcome versus the observed issue.

2. **Suggestions for Core Rule Changes**
   - If you have suggestions for changing the core rules of the game, submit them as a GitHub issue.
   - **Title**: Clearly indicate the nature of the suggestion.
   - **Description**: Explain the reasoning behind the suggestion, any impact on gameplay, and how it would enhance the overall experience.

3. **Suggestions for New Cards**
   - For suggestions of new cards to be added to the game, submit them as a GitHub issue under the `New Card Suggestion` label.
   - **Title**: The name of the new card.
   - **Description**: Provide details on the card's health, action, power, and how it integrates into the game’s current balance.
   - **Image**: If you have a proposed image for the card, attach it as a file in the issue. If possible, include the design file (PSD) and any additional resources to support the visual design.

4. **Questions**
   - If you have questions about gameplay mechanics, contributing guidelines, or any aspect of the project, submit them as a GitHub issue under the `Questions` label.
   - **Title**: A brief summary of your question or inquiry.
   - **Description**: Clearly outline your question or issue, including any relevant details or context that would help provide clarity or context for the discussion.
   - **Screenshots/Examples**: If necessary, attach screenshots, photos or examples to help clarify your question or concern.

#### Code of Conduct

- Follow the project's [code of conduct](./CODE_OF_CONDUCT.md) at all times.
- Respect other contributors and maintainers.

#### Get Help

- If you need any assistance, feel free to reach out to maintainers through GitHub issues.