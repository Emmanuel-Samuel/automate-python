# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 24/03/2023
# REVISED DATE: 24/03/2023
# PURPOSE: Drawing with Python

# import our functions from the classes
import pyautogui
from mss import mss, tools

# prints position of mouse
print(pyautogui.position())

# moves mouse position to draw on app
pyautogui.moveTo(74, 218, duration=1)
pyautogui.click()

#
# Down 200px
dur = 0.3
pyautogui.drag(0, 200, duration=dur, button='left')
# right 60px
pyautogui.drag(60, 0, duration=dur, button='left')
# up 3 px
pyautogui.drag(0, -3, duration=dur, button='left')
# down 6px
pyautogui.drag(0, 6, duration=dur, button='left')
# right 60 px
pyautogui.drag(60, 0, duration=dur, button='left')
# up 6px
pyautogui.drag(0, -6, duration=dur, button='left')
# left 60px
pyautogui.drag(-60, 0, duration=dur, button='left')


# right back 60px
pyautogui.move(60, 0, duration=dur)
# down back 3 px
pyautogui.move(0, 3, duration=dur)


# right 100px
pyautogui.drag(100, 0, duration=dur, button='left')
# up 120px
pyautogui.drag(0, -120, duration=dur, button='left')


# skip 40px
pyautogui.move(0, -40, duration=dur)
# up 40px
pyautogui.drag(0, -40, duration=dur, button='left')


# left 220px
pyautogui.drag(-220, 0, duration=dur, button='left')
pyautogui.move(-50, -50)

# screenshot portion of image drawn and save
with mss() as screen:
    part = {'top': 208, 'left': 64, 'width': 240, 'height': 220}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='draw.png')
