import pyautogui
import screeninfo
import time
from selenium import webdriver

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

codes = ['484', '4841', '4842', '48411', '484110', '484121', '484230', '492110']
# png_list = ['484.png']
# result = pyautogui.locateOnScreen('484.png')
# print(f"result{result}")
time.sleep(4)
for code in codes:
    image_position = pyautogui.locateOnScreen('static/images/naics.png', confidence=0.7)
    
    if image_position:
        # Get the center coordinates
        x, y = pyautogui.center(image_position)
        print(f"NAICS found at {x}, {y}")
        pyautogui.moveTo(x + 200, y)
        pyautogui.click()
        # clear text
        for x in range(10):
            pyautogui.press('delete')
        for x in range(10):
            pyautogui.press('backspace')
        # for x in range(100):
        # for char in code:
        #     pyautogui.press('backspace')
        
        time.sleep(5)
        pyautogui.typewrite(code, interval=0.2)
        #time.sleep(5) 
        search_btn_image = pyautogui.locateOnScreen('static/images/search.png', confidence=0.7)
        time.sleep(5)
        srch_x, srch_y = pyautogui.center(search_btn_image)
        pyautogui.moveTo(srch_x, srch_y)
        pyautogui.click()
        time.sleep(5) 

        #duplicate tab
        pyautogui.hotkey('alt','shift', 'd') 
 

    else:
        print("Image not found.")
    time.sleep(2)