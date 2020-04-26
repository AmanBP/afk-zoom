import pyautogui as gui
import time
gui.keyDown("winleft")
gui.keyUp("winleft")
time.sleep(2)
gui.write("zoom")
gui.keyDown("\n")
gui.keyUp("\n")
time.sleep(5)
active = gui.getActiveWindow()
active.width = 750
active.height = 950
print(active.topleft,active.title) #(x=541, y=82)
#817,314 38,129,242 #2681F2
cordx,cordy = active.topleft.x + ,active.topleft.y
gui.mouseDown()
gui.mouseUp()


