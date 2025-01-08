from time import sleep

import pyautogui
import subprocess
from AppOpener import open
import logging
from pywinauto import Application, Desktop

# Move to object and scroll
def _scroll_center(target_window, title, auto_id, control_type):
    scroll_bar = target_window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    scroll_bar_rec = scroll_bar.rectangle()
    pyautogui.moveTo(scroll_bar_rec.left + 20, scroll_bar_rec.top - 20)
    sleep(5)
    pyautogui.scroll(-800)

# Function open app return target windows
def _open_app(app_name):
    open(app_name, match_closest=False)
    sleep(5)
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    return target_window

# Function click object exist
def _object_click(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    result = []
    if object_select.exists():
        object_select.click_input()
        result = [True,title, object_select]
    else:
        result = [False, title, None]
    sleep(2)
    return result

    # try:
    #     object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    #     if object_select.exists():
    #         object_select.click_input()
    #         logging.info(f"Clicked on the object: {title}")
    #     else:
    #         logging.warning(f"Object not found: {title}")
    #         object_select = title
    # except Exception as e:
    #     logging.error(f"An error occurred: {e}")
    #     object_select = None
    # sleep(2)
    # return object_select

# Function find object
def _object_find(window, title, auto_id, control_type):
    object_find = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    result =[]
    if not object_find.exists():
        result = [False, title, None ]
    else:
        result = [True, title, object_find]
    sleep(2)
    return result
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

# Function connected wifi
def get_connected_wifi():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
        result = result.decode("utf-8", errors="ignore")
        for line in result.split('\n'):
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                return ssid
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Hàm giả để nhấn nút trong nhóm phần tử
def _object_click_within_group(group, name, auto_id, control_type):
    # Lấy danh sách các phần tử con trong nhóm
    child_elements = group.descendants(control_type=control_type)
    print(child_elements)
    # Duyệt qua các phần tử con và nhấn nút "Run" dựa trên auto_id
    for element in child_elements:
        print(element.window_text())
        if element.window_text() == name and element.automation_id() == auto_id:
            print(element.window_text())
            return _object_click(element)
    return False


# target_window = _open_app('Settings')
# object = target_window.child_window(title='Accessibility', auto_id='', control_type='ListItem')
# object.click_input()