from NPC_Auto.lib_common.common_lib import *

#Mở app settings
target_window = open_app('Settings')

# click system -> Display
is_system = object_click(target_window,'System','', 'ListItem')
is_sound = object_click(target_window, 'Sound', '', 'Text')
is_output = object_is_exist(target_window, 'Output', '', 'Text')
is_input = object_is_exist(target_window, 'Input', '', 'Text')
is_advanced = object_is_exist(target_window, 'Advanced', '', 'Text')

print(is_system, is_sound)

# Đóng app
target_window.close()