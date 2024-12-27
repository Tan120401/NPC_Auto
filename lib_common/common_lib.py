from time import sleep

import pyautogui
from AppOpener import open
from pywinauto import Application, Desktop

def _open_app(app_name):
    open(app_name, match_closest=False)
    sleep(5)
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    return target_window

# Function view object exist
def _object_is_exist(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object_select.exists():
        # print(title, 'viewed')
        sleep(2)
        is_exist = True
    return is_exist

# Function click object exist
def _object_click(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object_select.exists():
        object_select.click_input()
        # print(title, 'clicked')
        is_exist = True
        sleep(2)
    return is_exist

# Function click object by coordinates
def _object_click_by_coordinates(left, top, right, bottom):
    # Define BoundingRectangle
    bounding_rectangle = {'l': left, 't': top, 'r': right, 'b': bottom}

    # Calculate the central coordinates
    center_x = (bounding_rectangle['l'] + bounding_rectangle['r']) // 2
    center_y = (bounding_rectangle['t'] + bounding_rectangle['b']) // 2

    # Move to the central coordinates and click
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()

# Function to find open windows
def _find_open_window(app):
    # List all window
    all_window_active = Desktop(backend='uia').windows()
    is_app = False
    for win in all_window_active:
        if win.window_text() == app:
           is_app = True
           sleep(2)
           win.close()
    return is_app

# target_window = _open_app('Settings')
# object = target_window.child_window(title='Accessibility', auto_id='', control_type='ListItem')
# object.click_input()