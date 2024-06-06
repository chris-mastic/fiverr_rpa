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

log_msg = ""

with open(os.path.join(userprofile,'Documents\search_webpage.log'), 'a') as file:
    file.write(f"{datetime.datetime.now()}\n")

    codes = []
    with open(codes_path, 'r') as file:
        for line in file:
            codes.append(line.strip())

    try:
        iteration_counter = 0
        time.sleep(4)
        for code in codes:
            log_msg + code + '\n'
            image_position = pyautogui.locateOnScreen('naics.png', confidence=0.7)
            log_msg + image_position + '\n'
            print(f"code {code}")
            iteration_counter += 1
            if image_position:
                # Get the center coordinates
                x, y = pyautogui.center(image_position)
                file.write(f"NAICS found at {x}, {y}\n")
                log_msg + "NAICS found at " + x + ' ' + y +'\n'
                pyautogui.moveTo(x + 200, y)
                pyautogui.click()
                # clear text
                for x in range(10):
                    pyautogui.press('delete')
                for x in range(10):
                    pyautogui.press('backspace')
            
                time.sleep(1)
                pyautogui.typewrite(code, interval=0.2)
                search_btn_image = pyautogui.locateOnScreen('search.png', confidence=0.7)
                time.sleep(2)
                file.write(f"srch_x {srch_x} and srch_y {srch_y}\n")
                log_msg + 'srch_x ' + srch_x + ' ' + 'and srch_y ' + srch_y + '\n'
                srch_x, srch_y = pyautogui.center(search_btn_image)
                pyautogui.moveTo(srch_x, srch_y)
                pyautogui.click()
                time.sleep(2) 
            
                if iteration_counter != len(codes):
                    pyautogui.hotkey('alt','shift', 'd') 
        

                                 
    except:
        log_msg + "ERROR: Image not found \n"
        time.sleep(2)
    file.write(log_msg)