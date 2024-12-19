from time import sleep

from AppOpener import open
from pywinauto import Application, Desktop

from NPC_Auto.lib_common.common_lib import *

#Mở app settings
open('Settings', match_closest=False)
sleep(2)
app = Application(backend='uia').connect(title_re='Settings')
target_window = app.window(title_re='Settings')

# List all window
# all_window_active = Desktop(backend='uia').windows()
# for win in all_window_active:
#     print(win.window_text())
object_click(target_window,'Cloud storage', '','Text')
print(target_window.print_control_identifiers())