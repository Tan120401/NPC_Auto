import os
import sys

from NPC_Auto.lib_common.common_lib import *
from AppOpener import open
from pywinauto import Application, Desktop



#Mở app settings
open('Settings', match_closest=False)
sleep(2)
app = Application(backend='uia').connect(title_re='Settings')
target_window = app.window(title_re='Settings')

# Danh sách các object
dic_object_list = {
    'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
             'Time & language, Gaming, Accessibility, Privacy & security, Windows Update',
    'auto_id:': '',
    'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem'
}

titles = dic_object_list['title'].split(', ')
control_types = dic_object_list['control_type'].split(', ')
# auto_id = dic_object_list['auto_id']

# Kiểm tra xem độ dài của các danh sách có khớp nhau không
if len(titles) == len(control_types):
    for title, control_type in zip(titles, control_types):
        object_is_exist(target_window, title, '', control_type)
else:
    print("Title và control type không đồng nhất")
