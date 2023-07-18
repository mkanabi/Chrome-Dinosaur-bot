# Dinosaur Game Playing Bot

This is a Python script that acts as a bot for playing the Dinosaur Game in a web browser. The script captures the screen, identifies obstacles by detecting gray pixels, and triggers a jump action when an obstacle is detected. The script utilizes the PyAutoGUI, OpenCV, NumPy, and Keyboard libraries.

## Prerequisites
- Python 3.x
- PyAutoGUI
- OpenCV
- NumPy
- Keyboard

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required dependencies by running the following command:
pip install pyautogui opencv-python numpy keyboard

csharp
Copy code

## Usage
1. Open the web browser with the Dinosaur Game.
2. Run the script using the following command:
python dinosaur_game_bot.py

markdown
Copy code
3. The script will start capturing the screen and displaying the captured region with a red border.
4. Whenever gray pixels (obstacles) are detected in the captured region, the script will trigger a jump action by pressing the spacebar.
5. Use the arrow keys to move the region of interest and adjust the bot's detection area.
6. Press 'q' to stop the script and close the OpenCV windows.

## Customization
You can customize the bot's behavior by modifying the following variables:

- `jump_key`: The key to be pressed for the jump action. Default: `'space'`.
- `region_x`, `region_y`: The initial coordinates of the top-left corner of the region of interest. Default: `578`, `300`.
- `region_width`, `region_height`: The width and height of the region of interest. Default: `110`, `35`.
- `lower_gray_range`, `upper_gray_range`: The lower and upper bounds for gray pixel detection in BGR format. Modify these values to adjust the obstacle detection threshold. Default: `(0, 0, 0)`, `(255, 255, 200)`.
- `move_step`: The number of pixels to move the region of interest when using arrow keys for region movement. Default: `10`.

Feel free to modify these variables according to your specific requirements.

## Contributions
Contributions to the project are welcome! If you find any issues or want to enhance the functionality, feel free to open a pull request.
