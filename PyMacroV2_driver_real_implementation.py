from pynput.keyboard import *
from PyMacroV2 import *

_1_to_5 = {"x":680,"y":880,"d":150}
_f1_to_f8 = {"x":1568,"y":299,"d":55}

def macro_1():
    MouseLPress(_1_to_5["x"]+_1_to_5["d"]*0,_1_to_5["y"])

def macro_2():
    MouseLPress(_1_to_5["x"]+_1_to_5["d"]*1,_1_to_5["y"])

def macro_3():
    MouseLPress(_1_to_5["x"]+_1_to_5["d"]*2,_1_to_5["y"])

def macro_4():
    MouseLPress(_1_to_5["x"]+_1_to_5["d"]*3,_1_to_5["y"])

def macro_5():
    MouseLPress(_1_to_5["x"]+_1_to_5["d"]*4,_1_to_5["y"])

def macro_f1():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*0)

def macro_f2():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*1)

def macro_f3():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*2)

def macro_f4():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*3)

def macro_f5():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*4)

def macro_f6():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*5)

def macro_f7():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*6)

def macro_f8():
    MouseLPress(_f1_to_f8["x"],_f1_to_f8["y"]+_f1_to_f8["d"]*7)

# Map keys to the corresponding function
# Value of key at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
# Exmaple at https://pynput.readthedocs.io/en/latest/keyboard.html
combination_to_function = {
    frozenset([Key_('1')]): macro_1,
    frozenset([Key_('2')]): macro_2,
    frozenset([Key_('3')]): macro_3,
    frozenset([Key_('4')]): macro_4,
    frozenset([Key_('5')]): macro_5,
    frozenset([Key.f1]): macro_f1,
    frozenset([Key.f2]): macro_f2,
    frozenset([Key.f3]): macro_f3,
    frozenset([Key.f4]): macro_f4,
    frozenset([Key.f5]): macro_f5,
    frozenset([Key.f6]): macro_f6,
    frozenset([Key.f7]): macro_f7,
    frozenset([Key.f8]): macro_f8
}

current_keys = set()

def on_press(key):
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    try:
        current_keys.remove(key)
    except:
        pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()