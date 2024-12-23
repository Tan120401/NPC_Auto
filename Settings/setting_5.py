from NPC_Auto.lib_common.common_lib import *

#Mở app settings
target_window = open_app('Settings')
# click system -> Display
object_click(target_window,'System','', 'ListItem')
object_click(target_window,'Display','', 'Text')
object_is_exist(target_window,'Brightness & color','', 'Text')
object_is_exist(target_window,'Scale & layout','', 'Text')
object_is_exist(target_window,'Related settings','', 'Text')


