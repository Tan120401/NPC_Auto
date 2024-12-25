from time import sleep

from AppOpener import open
from pywinauto import Application, Desktop

def _open_app(app_name):
    open(app_name, match_closest=False)
    sleep(5)
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    return target_window

def _object_is_exist(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object_select.exists():
        print(title, 'viewed')
        sleep(2)
        is_exist = True
    return is_exist

def _object_click(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    is_exist = False
    if object_select.exists():
        object_select.click_input()
        print(title, 'clicked')
        is_exist = True
        sleep(2)
    return is_exist

# target_window = _open_app('Settings')
# object = target_window.child_window(title='Accessibility', auto_id='', control_type='ListItem')
# object.click_input()