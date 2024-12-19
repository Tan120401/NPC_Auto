from time import sleep

from AppOpener import open
from pywinauto import Application, Desktop

def object_is_exist(window, title, auto_id, control_type):
    object = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    if object.exists():
        print(f'{title} tồn tại --> Pass')
        sleep(2)
    else:
        print(f'{title} không tồn tại --> Fail')

def object_click(window, title, auto_id, control_type):
    object = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    if object.exists():
        object.click_input()
        print(f'{title} tồn tại --> Pass')
        sleep(2)
    else:
        print(f'{title} không tồn tại --> Fail')