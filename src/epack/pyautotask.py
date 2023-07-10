import win32api, win32con
import time
from pynput.keyboard import Key, Controller

def click(click_time = 0.1, pos: (int, int)):
    try:
        win32api.SetCursorPos((list(pos)[0], list(pos)[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(click_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return 0
    except error as e:
        print("try install pywin32 because: " + e)
    return 4

def contextclick(click_time = 0.1, pos: (int, int)):
    try:
        win32api.SetCursorPos((list(pos)[0], list(pos)[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(click_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        return 0
    except error as e:
        print("try install pywin32 because: " + e)
    return 2