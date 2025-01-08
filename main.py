from time import sleep

from AppOpener import open
from pywinauto import Application, Desktop

from NPC_Auto.lib_common.common_lib import _object_click

# Mở app settings
# open('Settings', match_closest=False)
# sleep(2)
# app = Application(backend='uia').connect(title_re='Settings')
# target_window = app.window(title_re='Settings')
#
# # List all window
# all_window_active = Desktop(backend='uia').windows()
# for win in all_window_active:
#     print(win.window_text())
#     # if win.window_text() == 'Get Help':
#     #     print(win.window_text())
#     # else:
#     #     print('khong co')
# # _object_click(target_window,'Bluetooth & devices', '','ListItem')
# # _object_click(target_window,'Cameras', '','Group')
# # _object_click(target_window,'Search for cameras', '','Button')
# _object_click(target_window,'System', '','ListItem')
# _object_click(target_window,'Storage', '','Group')
# print(target_window.print_control_identifiers())