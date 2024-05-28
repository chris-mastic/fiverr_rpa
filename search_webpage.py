import pyautogui
import cv2
import screeninfo
import time

# Move mouse to upper-left corner to abort program
pyautogui.FAILSAFE = True

'''
MS Edge Ctrl + Shift + K or Cmd + Shift + K in Mac
Chrome ALT + D and then ALT + Enter (the first selects the current tab
the second opens it)
'''
screens = screeninfo.get_monitors()
main_screen = None
for screen in screens:
    if screen.x == 0 and screen.y == 0:
        main_screen = screen
        break
print(main_screen)

png_list = ['484.png', '4841.png', '4842.png', '48411.png', '484110.png', '484121.png', '484230.png', '492110.png']
# png_list = ['484.png']
# result = pyautogui.locateOnScreen('484.png')
# print(f"result{result}")
for png in png_list:
    image_position = pyautogui.locateOnScreen('static/images/' + png, confidence=0.8)
    if image_position:
        # Get the center coordinates
        x, y = pyautogui.center(image_position)

        # Move the mouse to the center
        pyautogui.moveTo(x, y)
        print(f"x {x} and y {y} name= {png}")
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'shift', 'k')
        
        # Click to focus on the textbox
        # pyautogui.click()
    else:
        print("Image not found.")
    time.sleep(10)