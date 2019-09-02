from math import *
import pynput
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
import time, win32gui, win32con, win32com.client

_mouse = pynput.mouse.Controller()
_keyboard = pynput.keyboard.Controller()

def Key_(char):
    return KeyCode(char=char)

def KeyDown(key):
    _keyboard.press(key)

def KeyUp(key):
    _keyboard.release(key)

def KeyPress(key):
    KeyDown(key)
    Delay(STATIC_DELAY)
    KeyUp(key)

def MoveMouse(dx, dy):
    _mouse.position = (dx, dy)

def MouseLDown():
    _mouse.press(pynput.mouse.Button.left)

def MouseLUp():
    _mouse.release(pynput.mouse.Button.left)

def MouseLPress(dx, dy):
    MoveMouse(dx, dy)
    Delay(STATIC_DELAY)
    MouseLDown()
    Delay(STATIC_DELAY)
    MouseLUp()

def MouseLDrag(dx1, dy1, dx2, dy2):
    MoveMouse(dx1, dy1)
    Delay(STATIC_DELAY)
    MouseLDown()
    Delay(STATIC_DELAY)
    MoveMouse(dx2, dy2)
    Delay(STATIC_DELAY)
    MouseLUp()

def MouseRDown():
    _mouse.press(pynput.mouse.Button.right)

def MouseRUp():
    _mouse.release(pynput.mouse.Button.right)

def MouseRPress(dx, dy):
    MoveMouse(dx, dy)
    Delay(STATIC_DELAY)
    MouseRDown()
    Delay(STATIC_DELAY)
    MouseRUp()

def MouseRDrag(dx1, dy1, dx2, dy2):
    MoveMouse(dx1, dy1)
    Delay(STATIC_DELAY)
    MouseRDown()
    Delay(STATIC_DELAY)
    MoveMouse(dx2, dy2)
    Delay(STATIC_DELAY)
    MouseRUp()

def Delay(sec):
    time.sleep(sec)

def SwitchToWindow(title):
    win32gui.ShowWindow(win32gui.FindWindow(None, title), win32con.SW_RESTORE)
    win32com.client.Dispatch("WScript.Shell").AppActivate(title)

def MoveWindow(title, x, y):
    SwitchToWindow(title)
    hwnd = win32gui.FindWindow(None, title)
    rect = win32gui.GetWindowRect(hwnd)
    win32gui.MoveWindow(hwnd, x, y, rect[2]-rect[0], rect[3]-rect[1], True)

STATIC_DELAY = 0.1
