from math import *
import pynput
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from imagesearch import *
import time, win32gui, win32con, win32com.client

_mouse = pynput.mouse.Controller()
_keyboard = pynput.keyboard.Controller()

ESC = Key.esc

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
    # print("[debug]pressed "+str(key))

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
    # print("[debug]clicked at ("+str(dx)+","+str(dy)+")") # debug

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
    # print("[debug]clicked at ("+str(dx)+","+str(dy)+")") # debug

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

def WindowExists(title):
    if win32gui.FindWindow(None, title) == 0:
        return False
    return True

def SwitchToWindow(title):
    if WindowExists(title):
        win32gui.ShowWindow(win32gui.FindWindow(None, title), win32con.SW_RESTORE)
        win32com.client.Dispatch("WScript.Shell").AppActivate(title)

def MoveWindow(title, x, y):
    if WindowExists(title):
        SwitchToWindow(title)
        hwnd = win32gui.FindWindow(None, title)
        rect = win32gui.GetWindowRect(hwnd)
        win32gui.MoveWindow(hwnd, x, y, rect[2]-rect[0], rect[3]-rect[1], True)

def FindImage(fn, x1, y1, x2, y2, precision):
    # SaveImage("[debug]prtscr at ("+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+")",x1,y1,x2,y2) # debug
    return imagesearcharea(fn, x1, y1, x2, y2, precision)

def SaveImage(fn, x1, y1, x2, y2):
    im = region_grabber(region=(x1, y1, x2, y2))
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    im.save(fn+".png")

def ClickOnImage(fn, x1, y1, x2, y2, precision):
    pos = FindImage(fn, x1, y1, x2, y2, precision)
    if pos[0] == -1:
      # print("[debug]"+fn+" not found in ("+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+")") # debug
      return False
    img = cv2.imread(fn)
    height, width, channels = img.shape
    # print("[debug]clicked at ("+str(pos[0])+","+str(pos[0])+")") # debug
    MouseLPress(pos[0]+width/2, pos[1]+height/2)
    return True

STATIC_DELAY = 0.1

def DictToObject(dict):
    return type('',(object,),dict)()

