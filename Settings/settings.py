import sys
import codecs
from time import sleep

from PyQt6.QtWidgets import QTextBrowser
from PyQt6 import QtWidgets
from pywinauto import mouse, Desktop, Application
from pywinauto.findwindows import find_window

from NPC_Auto.lib_common.common_lib import _object_click, _open_app, _object_find, _object_click_by_coordinates, \
    _find_open_window, _scroll_center, _object_find, get_connected_wifi
from PyQt6 import uic
import pyautogui

from NPC_Auto.main import target_window

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
                is_exist = _object_find(target_window, title, auto_id, control_type)
            if isinstance(is_exist, target_window.child_window().__class__):
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Dic object list not match")

    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting(testcase_name, pass_list, fail_list)

# Function test case setting 3
def _setting_3():
    # dictionaries
    dic_of_objects = {
        'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
                 'Time & language, Gaming, Accessibility, Privacy & security, Windows Update',
        'auto_id': ', , , , , , , , , , , , ',
        'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem',
        'object_handle': 'view, view, view, view, view, view, view, view, view, view, view, view, view'
    }
    _setting("Setting 3", "Settings", dic_of_objects)

# Function test case setting 4
def _setting_4():
    # dictionaries
    dic_of_objects = {
        'title': 'Home, Recommended settings, Cloud storage, Bluetooth devices, Personalize your device, Try Microsoft 365',
        'auto_id': ", TitleContent, , TitleContent, TitleContent, ",
        'control_type': 'ListItem, Text, Text, Text, Text, Text',
        'object_handle': 'click, view, view, view, view, view'
    }
    _setting("Setting 4", "Settings", dic_of_objects)

# Function test case setting 5
def _setting_5():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Display, Brightness & color, Scale & layout, Related settings',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    _setting("Setting 5", "Settings", dic_of_objects)

# Function test case setting 12
def _setting_12():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Sound, Output, Input, Advanced',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    _setting("Setting 12", "Settings", dic_of_objects)

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

# Function test case setting 31
def _setting_31():
    target_window = _open_app('Settings')
    _object_click(target_window, 'System', '', 'ListItem')

    # Scroll down
    _scroll_center(target_window, 'Storage', '', 'Group')
    # The List contains the pass fail objects
    pass_list = []
    fail_list = []
    titles = ['Activation', 'Activation state, Active', 'Upgrade your edition of Windows', 'Change product key']
    control_types = ['Group', 'Group', 'Group', 'Text']
    auto_ids = ['', '', '', '']
    object_handles = ['click', 'view', 'click', 'view']
    # Check that the lengths of the lists match
    if len(titles) == len(control_types) == len(auto_ids) == len(object_handles):
        is_exist = True
        for title, auto_id, control_type, object_handle in zip(titles, auto_ids, control_types, object_handles):
            if object_handle == 'click':
                is_exist = _object_click(target_window, title, auto_id, control_type)
            elif object_handle == 'view':
                is_exist = _object_find(target_window, title, auto_id, control_type)
            if isinstance(is_exist, target_window.child_window().__class__):
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Dic object list không đồng nhất")

    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 31', pass_list, fail_list)

# Function test case setting 32
def _setting_32():
    target_window = _open_app('Settings')
    _object_click(target_window, 'System', '', 'ListItem')

    # Scroll down
    _scroll_center(target_window, 'Storage', '', 'Group')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_troubleshoot = _object_click(target_window, 'Troubleshoot', '', 'Text')
    is_other_troubleshoot = _object_click(target_window, 'Other troubleshooters', '', 'Text')

    # Assess object pass/fail
    list_of_object = [is_troubleshoot, is_other_troubleshoot]
    for obj in list_of_object:
        if isinstance(obj, target_window.child_window().__class__):
            pass_list.append(obj.window_text())
        else:
            fail_list.append(obj)

    # Click troubleshoot audio
    is_audio = _object_click(target_window, 'Audio', '', 'Text')
    if is_audio:
        _object_click_by_coordinates(2448, 314, 2708, 378)
        sleep(2)
        is_audio_troubleshoot = _find_open_window('Get Help')
        if is_audio_troubleshoot:
            pass_list.append('Audio Troubleshoot normally')
        else:
            fail_list.append('Audio Troubleshoot abnormally')

    # Click troubleshoot audio
    is_network = _object_click(target_window, 'Network and Internet', '', 'Text')
    if is_network:
        _object_click_by_coordinates(2448, 458, 2708, 522)
        sleep(2)
        is_audio_troubleshoot = _find_open_window('Get Help')
        if is_audio_troubleshoot:
            pass_list.append('Network and Internet Troubleshoot normally')
        else:
            fail_list.append('Network and Internet Troubleshoot abnormally')

    #Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 32', pass_list, fail_list)

# Function test case setting 33
def _setting_33():
    target_window = _open_app('Settings')
    _object_click(target_window, 'System', '', 'ListItem')

    # Scroll down
    _scroll_center(target_window, 'Storage', '', 'Group')

    # dictionaries
    dic_of_objects = {
        'title': 'Recovery, Reset this PC, Advanced startup',
        'auto_id': ", , ",
        'control_type': 'Text, Text, Text',
        'object_handle': 'click, view, view'
    }
    _setting("Setting 33", "Settings", dic_of_objects)

# Function test case setting 38
def _setting_38():
    target_window = _open_app('Settings')
    _object_click(target_window, 'System', '', 'ListItem')

    # Scroll down
    _scroll_center(target_window, 'Storage', '', 'Group')

    # dictionaries
    dic_of_objects = {
        'title': 'About, Device specifications, Windows specifications, Support, Related',
        'auto_id': ", , , , ",
        'control_type': 'Group, Group, Group, Group, Text',
        'object_handle': 'click, view, view, view, view'
    }
    _setting("Setting 38", "Settings", dic_of_objects)

# Function test case setting 41
def _setting_41():
    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, View more devices, Bluetooth, Other devices, Related settings',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Button, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }

    _setting("Setting 41", "Settings", dic_of_objects)

# Function test case setting 42
def _setting_42():

    target_window = _open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_bluetooth_device = _object_click(target_window, 'Bluetooth & devices', '', 'ListItem')
    is_add_device = _object_click(target_window, 'Add device', '', 'Text')

    # Focus add device window

    window_handle = find_window(title_re='.*Add a device.*', backend='uia')
    app_bluetooth = Application(backend='uia').connect(handle=window_handle)
    bluetooth_window = app_bluetooth.window(handle=window_handle)

    print(bluetooth_window.print_control_identifiers())
    is_bluetooth = _object_find(bluetooth_window, 'Bluetooth', 'BluetoothDevicesButton', 'Button')
    is_wireless = _object_find(bluetooth_window, 'Wireless display or dock', 'DisplayDevicesButton', 'Button')
    is_everything = _object_find(bluetooth_window, 'Everything else', 'OtherDevicesButton', 'Button')

    list_objects_check = [is_bluetooth_device, is_add_device, is_bluetooth, is_wireless, is_everything]
    # Check that the lengths of the lists match

    for obj in list_objects_check:
        if isinstance(obj, target_window.child_window().__class__):
            pass_list.append(obj.window_text())
        else:
            fail_list.append(obj)
    bluetooth_window.close()
    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 42', pass_list, fail_list)

# Function test case setting 43
def _setting_43():

    target_window = _open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_printers_scanners = _object_click(target_window, 'Printers & scanners', '', 'Text')
    is_add_printer = _object_find(target_window, 'Add a printer or scanner', '', 'Text')
    is_printer_preferences = _object_find(target_window, 'Printer preferences', '', 'Text')
    is_related_settings = _object_find(target_window, 'Related settings', '', 'Text')
    is_print_server_properties = _object_find(target_window, 'Print server properties', '', 'Text')

    #Focus add device window
    list_objects_check = [is_printers_scanners, is_add_printer, is_printer_preferences, is_related_settings, is_print_server_properties]

    for obj in list_objects_check:
        if isinstance(obj, target_window.child_window().__class__):
            pass_list.append(obj.window_text())
        else:
            fail_list.append(obj)

    # get value on or off
    is_manage_my_default_printer = target_window.child_window(title='Let Windows manage my default printer',control_type='Button')
    is_default_printer_state = is_manage_my_default_printer.get_toggle_state()
    if is_default_printer_state == 1:
        pass_list.append(f'{is_manage_my_default_printer.window_text()} default is ON')
    else:
        fail_list.append(f'{is_manage_my_default_printer.window_text()} default is OFF')

    is_download_drivers = target_window.child_window(title='Download drivers and device software over metered connections', control_type='Button')
    is_default_is_download_driver_state = is_download_drivers.get_toggle_state()
    if is_default_is_download_driver_state == 0:
        pass_list.append(f'{is_manage_my_default_printer.window_text()} default is OFF')
    else:
        fail_list.append(f'{is_manage_my_default_printer.window_text()} default is ON')



    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 43', pass_list, fail_list)

# Function test case setting 53
def _setting_53():

    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Cameras, Search for cameras, Connected cameras, Related settings',
        'auto_id': ", , SystemSettings_Camera_DeviceAdd_Button, SystemSettings_Camera_DeviceList_GroupTitleTextBlock, ",
        'control_type': 'ListItem, Group, Button, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    _setting("Setting 53", "Settings", dic_of_objects)

# Function test case setting 54
def _setting_54():
    _open_app('Settings')
    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Mouse, Primary mouse button, Mouse pointer speed, Enhance pointer precision, Scrolling, Related settings',
        'auto_id': ", , , , , , ",
        'control_type': 'ListItem, Group, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view'
    }
    _setting("Setting 54", "Settings", dic_of_objects)

# Function test case setting 55
def _setting_55():
    target_window =  _open_app('Settings')

    is_bluetooth_devices = _object_click(target_window, 'Bluetooth & devices', '', 'ListItem')

    _scroll_center(target_window, 'Cameras', '', 'Group')

    is_touchpad = _object_click(target_window, 'Touchpad', '', 'Group')

    is_touchpad_in = _object_find(target_window, 'Touchpad', '', 'Group')

    is_gestures = _object_find(target_window, 'Gestures & interaction', '', 'Text')

    is_related_settings = _object_find(target_window, 'Related settings', '', 'Text')


    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    #Focus add device window
    list_objects_check = [is_bluetooth_devices, is_touchpad, is_touchpad_in, is_gestures, is_related_settings]

    for obj in list_objects_check:
        if isinstance(obj, target_window.child_window().__class__):
            pass_list.append(obj.window_text())
        else:
            fail_list.append(obj)

    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 55', pass_list, fail_list)

# Function test case setting 57
def _setting_57():
    target_window =  _open_app('Settings')


    is_bluetooth_devices = _object_click(target_window,'Bluetooth & devices', '', 'ListItem')
    _scroll_center(target_window, 'Cameras', '', 'Group')

    is_auto_play = _object_click(target_window, 'AutoPlay', '', 'Text')
    print(target_window.print_control_identifiers())
    is_auto_play_in = _object_find(target_window, 'Use AutoPlay for all media and devices', 'SystemSettings_Autoplay_IsEnabled_ToggleSwitch', 'Button')
    is_auto_play_default = _object_find(target_window, 'Choose AutoPlay defaults', 'SettingsGroupControlTemplate_DisplayName', 'Text')
    is_related_settings = _object_find(target_window, 'Related settings', 'RelatedLinksGroupHeader', 'Text')



    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    # Focus add device window
    list_objects_check = [is_bluetooth_devices, is_auto_play, is_auto_play_in, is_auto_play_default, is_related_settings]

    for obj in list_objects_check:
        if isinstance(obj, target_window.child_window().__class__):
            pass_list.append(obj.window_text())
        else:
            fail_list.append(obj)

    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 57', pass_list, fail_list)

# Function test case setting 58
def _setting_58():
    target_window =  _open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_bluetooth_devices = _object_click(target_window,'Bluetooth & devices', '', 'ListItem')
    _scroll_center(target_window, 'Cameras', '', 'Group')

    is_auto_play = _object_click(target_window, 'AutoPlay', '', 'Text')

    is_auto_play_default = target_window.child_window(title='Use AutoPlay for all media and devices',auto_id='SystemSettings_Autoplay_IsEnabled_ToggleSwitch', control_type='Button')
    is_auto_play_default_state = is_auto_play_default.get_toggle_state()
    if is_auto_play_default_state == 1:
        pass_list.append(f'{is_auto_play_default.window_text()} default is ON')
    else:
        fail_list.append(f'{is_auto_play_default.window_text()} default is OFF')

    is_removable_drive = target_window.child_window(title="Removable drive", auto_id="SystemSettings_Autoplay_StorageHandler_ComboBox", control_type="ComboBox")
    removable_drive_value = is_removable_drive.selected_text()
    if removable_drive_value is None:
        pass_list.append('Removable drive is Select default app')
    else:
        fail_list.append('Removable drive is not Select default app')

    is_memory_card = target_window.child_window(title="Memory card", auto_id="SystemSettings_Autoplay_CameraStorageHandler_ComboBox", control_type="ComboBox")

    memory_card_value = is_memory_card.selected_text()
    if memory_card_value is None:
        pass_list.append('Memory card is Select default app')
    else:
        fail_list.append('Memory card is not Select default app')

    is_default_app = target_window.child_window(title="Default app settings",auto_id="SystemSettings_XLinks_Local_System_Defaults_Link_HyperlinkButton",control_type="Hyperlink")
    if is_default_app.exists():
        pass_list.append(is_default_app.window_text())
    else:
        fail_list.append(is_default_app.window_text())
    # Focus Home settings
    home_click = target_window.child_window(title='Home', auto_id='', control_type='ListItem')
    home_click.click_input()
    write_log_setting('Setting 57', pass_list, fail_list)

# Function Test case setting 63
def _setting_63():
    connected_wifi = get_connected_wifi()

    _open_app('Settings')
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Wi-Fi, Wi-Fi, {connected_wifi} properties, Show available networks, Manage known networks, Hardware properties, Random hardware addresses',
        'auto_id': ", , , , , , , ",
        'control_type': 'ListItem, Group, Button, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view, view'
    }
    _setting("Setting 63", "Settings", dic_of_objects)

# Function Test case setting 64
def _setting_64():
    connected_wifi = get_connected_wifi()

    target_window = _open_app('Settings')

    is_network = _object_click(target_window)
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Wi-Fi, Wi-Fi, {connected_wifi} properties, Show available networks, Manage known networks, Hardware properties, Random hardware addresses',
        'auto_id': ", , , , , , , ",
        'control_type': 'ListItem, Group, Button, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view, view'
    }
    _setting("Setting 63", "Settings", dic_of_objects)
# Call function execute test case
# _setting_3()
# _setting_4()
# _setting_5()
# _setting_12()
# _setting_13()
# _setting_18()
# _setting_31()
# _setting_32()
# _setting_33()
# _setting_38()
# _setting_41()
# _setting_42()
# _setting_43()
# _setting_53()
# _setting_54()
# _setting_55()
# _setting_57()
# _setting_58()
_setting_63()

# Show result on UI
for result in result_of_testcase:
    txt_result.append(f"{result}\n")
window.show()
app.exec()

