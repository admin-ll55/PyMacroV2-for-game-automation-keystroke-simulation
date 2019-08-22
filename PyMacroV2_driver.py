# imports
from pynput.keyboard import *
from PyMacroV2 import *

# Your macros & normal py codes
_1 = {"x":680,"y":880}

def macro_1():
    MouseLPress(_1["x"],_1["y"])

def macro_f1():
    MouseLPress(_1["x"]*1.1,_1["y"]*1.1)

# Map keys to the corresponding function
# Value of key at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
combination_to_function = {
    frozenset([Key_('1')]): macro_1, # Pressing key "1" executes "macro_1"
    frozenset([Key.f1]): macro_f1 # Pressing key "F1" executes "macro_f1"
}

# Main program

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