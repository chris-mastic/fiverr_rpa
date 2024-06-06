import datetime
import os
import pyautogui
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

userprofile = os.environ['USERPROFILE']
codes_path = os.path.join(userprofile,'Documents\search_codes.txt')

codes = []
with open(codes_path, 'r') as file:
    for line in file:
        codes.append(line.strip())

try:
    iteration_counter = 0
    file = open(os.path.join(userprofile,'Documents\search_webpage.log'), 'a') 
    file.write(f"{datetime.datetime.now()}\n")

    time.sleep(4)
    for code in codes:
        file.write(f'searching for NAICS.png...\n')
        image_position = pyautogui.locateCenterOnScreen('arrow.png', confidence=0.7)
        file.write(f'image_position {image_position}\n')
        print(f"code {code}")
        iteration_counter += 1
        if image_position:
            # Get the center coordinates
            #x, y = pyautogui.center(image_position)
            print("in if ")
            file.write(f"NAICS found at{image_position[0]}\n")
            pyautogui.moveTo(image_position[0] + 50, image_position[1])
            pyautogui.click()
            # clear text
            for x in range(10):
                pyautogui.press('delete')
            for x in range(10):
                pyautogui.press('backspace')
            
            time.sleep(1)
            pyautogui.typewrite(code, interval=0.2)
            file.write("Searching for serach.png...")
            search = pyautogui.locateCenterOnScreen('search.png')
            pyautogui.moveTo(search)
            # search_btn_image = pyautogui.locateOnScreen('search.png', confidence=0.7)
            # time.sleep(2)
            # file.write(f"srch_x {srch_x} and srch_y {srch_y}\n")
            # srch_x, srch_y = pyautogui.center(search_btn_image)
            # pyautogui.moveTo(srch_x, srch_y)
            pyautogui.click()
            time.sleep(2) 
            
            if iteration_counter != len(codes):
                pyautogui.hotkey('alt','shift', 'd') 
        

                                 
except BaseException as e: 
    file.write(f'ValueError {e.with_traceback}\n')
    time.sleep(2)
finally:
    file.close()
    