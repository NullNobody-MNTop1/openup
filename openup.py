import ctypes
from time import sleep as s

def force_full_screen():
    try:
        user32 = ctypes.WinDLL('user32')
        kernel32 = ctypes.WinDLL('kernel32')

        hwnd = kernel32.GetConsoleWindow()
        while user32.GetParent(hwnd):
            hwnd = user32.GetParent(hwnd)

        user32.SetForegroundWindow(hwnd)
        s(0.1)


        user32.keybd_event(0x12, 0, 0, 0)
        user32.keybd_event(0x0D, 0, 0, 0)
        user32.keybd_event(0x0D, 0, 2, 0)
        user32.keybd_event(0x12, 0, 2, 0)
    except Exception:
        pass