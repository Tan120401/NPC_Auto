from time import sleep

from AppOpener import open
from pywinauto import Application, Desktop

def open_app(app_name):
    open(app_name, match_closest=False)
    sleep(3)
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    return target_window

def object_is_exist(window, title, auto_id, control_type):
    object = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object.exists():
        # print(f'{title} tồn tại --> Pass')
        sleep(2)
        is_exist = True
    # else:
    #     print(f'{title} không tồn tại --> Fail')
    return is_exist

def object_click(window, title, auto_id, control_type):
    object = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object.exists():
        object.click_input()
        # print(f'{title} tồn tại --> Pass')
        is_exist = True
        sleep(2)
    # else:
    #     print(f'{title} không tồn tại --> Fail')
    return is_exist