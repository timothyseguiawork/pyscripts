# mouse mover
import pyautogui, sys
print(pyautogui.size())
print(pyautogui.position())

print('Press CTRL-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionSTR = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pyautogui.moveTo(1, 1, 1)
        pyautogui.moveTo(1918, 1, 1)
        pyautogui.moveTo(1, 1078, 1)
        pyautogui.moveTo(1918,1078, 1)
        print(positionSTR, end='')
        print('\b' *len(positionSTR), end='', flush=True)
except KeyboardInterrupt:
    print('\n')