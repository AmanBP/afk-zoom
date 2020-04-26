import pyautogui as gui
import time
gui.keyDown("winleft")
gui.keyUp("winleft")
time.sleep(2)
gui.write("zoom")
gui.keyDown("\n")
gui.keyUp("\n")
time.sleep(5)
gui.keyDown("winleft")
cheat = ["up","up","down","left","up"]
for code in cheat:
    gui.keyDown(code)
    gui.keyUp(code)
gui.keyUp("winleft")
time.sleep(2)
gui.click(331,254)
#331,245 38,129,242
