# Welcome to PyMacroV2
Platform: Windows  
Python: 3.7  
Description: Want to automate boring repeated actions? Here you can automate anything with ease.

PyMacro was deprecated due to compatability issues with pynput.  
After a while, PyMacroV2 is introduced for replacement of PyMacro.  

# How to use PyMacroV2.py
Basic keystrokes simulations:
- ```KeyDown(key)``` presses ```key```
- ```KeyUp(key)``` releases ```key```

Intermediate mouse simulations:
- ```KeyPress(key)``` pressess and releases ```key```

Note: Values of ```key``` can be found at [here](https://pynput.readthedocs.io/en/latest/keyboard.html).

Basic mouse simulations:
- ```MoveMouse(dx, dy)``` moves to (```dx```,```dy```) coordinate in terms of pixels
- ```MouseLDown()``` presses left click at current mouse position
- ```MouseLUp()``` releases left click at current mouse position
- ```MouseRDown()``` presses right click at current mouse position
- ```MouseRUp()``` releases right click at current mouse position

Intermediate mouse simulations:
- ```MouseLPress(dx, dy)``` presses and releases left click at (```dx```,```dy```) coordinate in terms of pixels
- ```MouseLDrag(dx1, dy1, dx2, dy2)``` uses left click to drag an object located at (```dx1```,```dy1```) to (```dx2```,```dy2```) in terms of pixels
- ```MouseRPress(dx, dy)``` presses and releases right click at (```dx```,```dy```) coordinate in terms of pixels
- ```MouseRDrag(dx1, dy1, dx2, dy2)``` uses right click to drag an object located at (```dx1```,```dy1```) to (```dx2```,```dy2```) in terms of pixels

MISC:
- ```Key_(char)``` is used for key translations, see the simple example for the usage.
- ```SwitchToWindow(title)``` switches to the window with title ```title```
- ```Delay(sec)``` delays or waits for ```sec``` second(s)
- ```STATIC_DELAY``` is used between basic simulations in intermediate simulations

Simple example:
```python
from PyMacroV2 import *
STATIC_DELAY = 1/3
SwitchToWindow("Untitled - Notepad")
Delay(1)
KeyPress(Key_('N'))
KeyPress(Key_('I'))
KeyDown(Key.shift_l)
KeyPress(Key_('c'))
KeyPress(Key_('e'))
KeyUp(Key.shift_l)
```

Key binding macro example (refer to PyMacroV2_driver.py):
- In this part, macros are stored in each individual function:
```python
# Your macros & normal py codes
_1 = {"x":680,"y":880}

def macro_1():
    MouseLPress(_1["x"],_1["y"])

def macro_f1():
    MouseLPress(_1["x"]*1.1,_1["y"]*1.1)
```
- In this part, keys are mapped and binded to the corresponding function:
```python
# Map keys to the corresponding function
# Value of key at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
combination_to_function = {
    frozenset([Key_('1')]): macro_1, # Pressing key "1" executes "macro_1"
    frozenset([Key.f1]): macro_f1 # Pressing key "F1" executes "macro_f1"
}
```
- More example:
```python
def macro_s1():
    MouseLDrag(_1["x"],_1["y"],_1["x"]+100,_1["y"])

combination_to_function = {
    frozenset([Key.shift_l, Key_('1')]): macro_s1 # Pressing key "1" and "left shift" executes "macro_s1"
}
```
