from NPC_Auto.lib_common.common_lib import *

#Mở app settings
target_window = open_app('Settings')

# Ấn vào hôm
object_click(target_window,'Home', '','ListItem')
# Danh sách các object
dic_object = {
    'title': 'Recommended settings, Cloud storage, Bluetooth devices, Personalize your device, Try Microsoft 365',
    'auto_id': ['TitleContent', '' ,'TitleContent', 'TitleContent', ''],
    'control_type': 'Text, Text, Text, Text, Text'
}
titles = dic_object['title'].split(', ')
control_types = dic_object['control_type'].split(', ')
auto_ids = dic_object['auto_id']

# Kiểm tra các object có tồn tại hay không
# Kiểm tra xem độ dài của các danh sách có khớp nhau không
if len(titles) == len(control_types):
    for title,auto_id, control_type in zip(titles, auto_ids, control_types):
        # print(title,auto_id, control_type)
        object_is_exist(target_window, title, auto_id, control_type)
else:
    print("Title và control type không đồng nhất")
