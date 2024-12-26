import sys
import codecs

from PyQt6.QtWidgets import QTextBrowser
from PyQt6 import QtWidgets

from NPC_Auto.lib_common.common_lib import _object_click, _open_app, _object_is_exist
from PyQt6 import uic

# Initialize UI
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("setting_result_display.ui")
txt_result = window.findChild(QTextBrowser, 'txtResult')

# The list contain information show on UI
result_of_testcase = []

# Initialize the log file
with codecs.open("setting_logs.txt", "w", "utf-8") as file:
    file.write('LOG INFORMATION\n')

# Function to write logs
def write_log_setting(testcase_name,pass_list, fail_list):
    # Open log file and write
    with codecs.open("setting_logs.txt", "a", "utf-8") as file:
        file.write(f"*{testcase_name.upper()}\n")
        file.write("-List of pass: ")
        file.write(", ".join(pass_list))
        file.write("\n")
        if len(fail_list) > 0:
            result_of_testcase.append(f"-{testcase_name}: Fail")
            file.write("-List of fail: ")
            file.write(", ".join(fail_list))
            # for fail_ob in fail_list:
            #    file.write(f"{fail_ob}, ")
            file.write("\n")
        else:
            result_of_testcase.append(f"-{testcase_name}: Pass")

# Function to check if objects exist
def _setting(testcase_name, app, dic_object_list):
    # Open app settings
    target_window = _open_app(f"{app}")

    # Change title, control type, auto_id, object_handle to List
    titles = dic_object_list['title'].split(', ')
    control_types = dic_object_list['control_type'].split(', ')
    auto_ids = dic_object_list['auto_id'].split(', ')
    object_handles = dic_object_list['object_handle'].split(', ')
    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    # Check that the lengths of the lists match
    if len(titles) == len(control_types) == len(auto_ids) == len(object_handles):
        is_exist = True
        for title, auto_id, control_type, object_handle in zip(titles, auto_ids, control_types, object_handles):
            if object_handle == 'click':
                is_exist = _object_click(target_window, title, auto_id, control_type)
            elif object_handle == 'view':
                is_exist = _object_is_exist(target_window, title, auto_id, control_type)
            if is_exist:
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Dic object list không đồng nhất")

    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting(testcase_name, pass_list, fail_list)

# # Function test case setting 3
# def _setting_3():
#     # dictionaries
#     dic_of_objects = {
#         'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
#                  'Time & language, Gaming, Accessibility, Privacy & security, Windows Update',
#         'auto_id': ', , , , , , , , , , , , ',
#         'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem',
#         'object_handle': 'view, view, view, view, view, view, view, view, view, view, view, view, view'
#     }
#     _setting("Setting 3", "Settings", dic_of_objects)
#
# # Function test case setting 4
# def _setting_4():
#     # dictionaries
#     dic_of_objects = {
#         'title': 'Home, Recommended settings, Cloud storage, Bluetooth devices, Personalize your device, Try Microsoft 365',
#         'auto_id': ", TitleContent, , TitleContent, TitleContent, ",
#         'control_type': 'ListItem, Text, Text, Text, Text, Text',
#         'object_handle': 'click, view, view, view, view, view'
#     }
#     _setting("Setting 4", "Settings", dic_of_objects)
#
# # Function test case setting 5
# def _setting_5():
#     # dictionaries
#     dic_of_objects = {
#         'title': 'System, Display, Brightness & color, Scale & layout, Related settings',
#         'auto_id': ", , , , ",
#         'control_type': 'ListItem, Text, Text, Text, Text',
#         'object_handle': 'click, click, view, view, view'
#     }
#     _setting("Setting 5", "Settings", dic_of_objects)
#
# # Function test case setting 5
# def _setting_12():
#     # dictionaries
#     dic_of_objects = {
#         'title': 'System, Sound, Output, Input, Advanced',
#         'auto_id': ", , , , ",
#         'control_type': 'ListItem, Text, Text, Text, Text',
#         'object_handle': 'click, click, view, view, view'
#     }
#     _setting("Setting 12", "Settings", dic_of_objects)

# Function test case setting 13
def _setting_13():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Notifications, Do not disturb, Turn on do not disturb automatically, Set priority notifications, Focus, Notifications from apps and other senders',
        'auto_id': ", , , , , , ",
        'control_type': 'ListItem, Text, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view'
    }
    _setting("Setting 13", "Settings", dic_of_objects)

# Function test case setting 18
def _setting_18():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Power & battery, Power & battery',
        'auto_id': ", , ",
        'control_type': 'ListItem, Text, Text',
        'object_handle': 'click, click, view'
    }
    _setting("Setting 14", "Settings", dic_of_objects)
# Call function execute test case
# _setting_3()
# _setting_4()
# _setting_5()
# _setting_12()
# _setting_13()
_setting_18()
# Show result on UI
for result in result_of_testcase:
    txt_result.append(f"{result}\n")
window.show()
app.exec()

