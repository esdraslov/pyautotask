import win32api, win32con
import time

def click(click_time = 0.1, pos: (int, int)):
    win32api.SetCursorPos((list(pos)[0], list(pos)[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(click_time)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    return 0
