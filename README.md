# Welcome to PyMacro
Platform: Windows  
Python: 3.7  
Description:  
It was deprecated due to compatability issues with pynput.  
Want to automate boring repeated actions? Here you can automate anything with ease.

# How to use
Basic keystrokes simulations:
- ```KeyDown(key)``` presses ```key```
- ```KeyUp(key)``` releases ```key```

Intermediate mouse simulations:
- ```KeyPress(key)``` pressess and releases ```key```

Note: Values of ```key``` can be found at [here](https://github.com/admin-ll55/PyMacro-for-game-automation-keystroke-simulation/blob/master/PyMacro.py#L7).

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
- ```SwitchToWindow(title)``` switches to the window with title ```title```
- ```Delay(sec)``` delays or waits for ```sec``` second(s)
- ```STATIC_DELAY``` is used between basic simulations in intermediate simulations

Example:
```python
from PyMacro import *
STATIC_DELAY = 1/3
SwitchToWindow("Untitled - Notepad")
Delay(1)
KeyDown("LSHIFT")
KeyPress("N")
KeyPress("I")
KeyUp("LSHIFT")
KeyPress("C")
KeyPress("E")
```
