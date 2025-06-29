import pyautogui
print(pyautogui.size())
pyautogui.click(100,100)
print(pyautogui.position())
pyautogui.moveTo(100,100,duration=1)
print(pyautogui.position())
pyautogui.moveTo(190,190,duration=1)
print(pyautogui.position())

