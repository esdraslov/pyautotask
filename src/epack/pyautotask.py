import win32api, win32con
import time
from pynput.keyboard import Key, Controller
from pyautogui import write

def click(x: int, y: int, click_time = 0.1):
    try:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(click_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return 0
    except error as e:
        print("try install pywin32 because: " + e)
    return 4

def contextclick(x: int, y: int, click_time = 0.1):
    try:
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(click_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        return 0
    except error as e:
        print("try install pywin32 because: " + e)
    return 2

def press(key):
    keyboard = Controller()

    keyboard.press(key)
    keyboard.relase(key)
    return 0

def write(text: str):
    write(text)
    return 0
