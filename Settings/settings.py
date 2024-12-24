import sys
import codecs

from PyQt6.QtWidgets import QTextBrowser
from PyQt6 import QtWidgets

from NPC_Auto.lib_common.common_lib import *
from PyQt6 import uic

# Khởi tạo giao diện hiển thị kết quả
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("setting_result_display.ui")
txt_result = window.findChild(QTextBrowser, 'txtResult')

# Mảng chứa danh sách kết quả pass fail
result_of_testcase = []

with codecs.open("setting_logs.txt", "w", "utf-8") as file:
    file.write('')
# Hàm ghi thông tin pass fail vào log
def write_log_setting(testcase_name,pass_list, fail_list):
    with codecs.open("setting_logs.txt", "a", "utf-8") as file:
        file.write(f"\n{testcase_name}\n")
        file.write("Danh sach pass.\n\t")
        for pass_ob in pass_list:
            file.write(f"{pass_ob}, ")
        if len(fail_list) > 0:
            result_of_testcase.append(f"{testcase_name} Fail")
            file.write("\nDanh sach fail.\n\t")
            for fail_ob in fail_list:
               file.write(f"{fail_ob}, ")
        else:
            result_of_testcase.append(f"{testcase_name} Pass")


# test case setting 3
def _setting_3():
    # Mở app settings
    target_window = open_app('Settings')
    # Danh sách các object
    dic_object_list = {
        'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
                 'Time & languagee, Gaming, Accessibility, Privacy & security, Windows Update',
        'auto_id:': '',
        'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem'
    }
    # chuyển tilte and control type thành mảng
    titles = dic_object_list['title'].split(', ')
    control_types = dic_object_list['control_type'].split(', ')

    # Mảng chứa thông tin các object pass fail
    pass_list = []
    fail_list = []

    # Kiểm tra xem độ dài của các danh sách có khớp nhau không
    if len(titles) == len(control_types):
        for title, control_type in zip(titles, control_types):
            is_exist = object_is_exist(target_window, title, '', control_type)
            if is_exist:
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Title và control type không đồng nhất")

    # Đóng app
    target_window.close()
    write_log_setting('Setting 3',pass_list,fail_list)

# Hàm test case setting 4
def _setting_4():
    # Mở app settings
    target_window = open_app('Settings')

    # Danh sách các object
    dic_object = {
        'title': 'Home, Recommended settings, Cloud storage, Bluetooth devices, Personalize your device, Try Microsoft 365',
        'auto_id': ['', 'TitleContent', '', 'TitleContent', 'TitleContent', ''],
        'control_type': 'ListItem, Text, Text, Text, Text, Text'
    }
    titles = dic_object['title'].split(', ')
    control_types = dic_object['control_type'].split(', ')
    auto_ids = dic_object['auto_id']

    # Mảng chứa thông tin các object pass fail
    pass_list = []
    fail_list = []

    # Kiểm tra xem độ dài của các danh sách có khớp nhau không
    if len(titles) == len(control_types):
        for title, auto_id, control_type in zip(titles, auto_ids, control_types):
            is_exist = object_is_exist(target_window, title, auto_id, control_type)
            if is_exist:
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Title và control type không đồng nhất")
    # Đóng app
    target_window.close()
    write_log_setting('Setting 4', pass_list, fail_list)

# Hiển thị kết quả lên giao diện
_setting_3()
_setting_4()
for result in result_of_testcase:
    txt_result.append(f"{result}\n")
window.show()
app.exec()

