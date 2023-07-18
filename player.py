import pyautogui
import cv2
import numpy as np     
import time
import keyboard

# Constants
jump_key = 'space'
region_x = 578
region_y = 300
region_width = 110
region_height = 35                                            
lower_gray_range = (0, 0, 0)               # Lower bounds for gray pixel detection in BGR
upper_gray_range = (255, 255, 200)   # Upper bounds for gray pixel detection in BGR
move_step = 10

# Function to check if gray pixels are present
def is_gray_pixels_present(region):              
    mask = cv2.inRange(region, lower_gray_range, upper_gray_range)
    if np.any(mask == 255):
        return True
    return False

# Main game loop
while True:
    # Capture the screen
    screen = np.array(pyautogui.screenshot())

    # Extract the region of interest
    region = screen[region_y:region_y + region_height, region_x:region_x + region_width]

    # Add red border to the captured region
    region_with_border = cv2.rectangle(region, (0, 0), (region.shape[1], region.shape[0]), (0, 0, 255), 2)

    # Display the screen with the captured region and border
    cv2.imshow('Captured Region', region_with_border)
    cv2.waitKey(1)

    # Check if gray pixels are present
    if is_gray_pixels_present(region):
        # Jump when gray pixels are detected
        pyautogui.press(jump_key)
        print("Jump!")
        print(region_x)
        print(region_y)


        


    # Read keyboard inputs for region movement
    if keyboard.is_pressed('left'):
        region_x -= move_step
    if keyboard.is_pressed('right'):
        region_x += move_step
    if keyboard.is_pressed('up'):
        region_y -= move_step
    if keyboard.is_pressed('down'):
        region_y += move_step

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
                    