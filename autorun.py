import pyautogui
import time
def down_wk():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('p')
def down_sdx():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('m')
def up_all():
    pyautogui.keyUp('alt')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('p')
    pyautogui.keyUp('m')
def run():
    down_wk()
    time.sleep(0.5)
    down_sdx()
    time.sleep(0.5)
    up_all()
while True:
  tNow = time.strftime("%H:%M:%S", time.localtime())
  print("wait")
  time.sleep(1.5)
  if tNow == "18:45:00":
    run()
    time.sleep(5)