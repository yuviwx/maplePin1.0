import pyautogui, keyboard, sys, time
from PIL import Image

def quit():
    global exitProgram
    exitProgram = False

def press(number):
    
    photo = Image.open(number)
    print("searching the number on the screen")
    location = pyautogui.locateCenterOnScreen(photo, confidence=0.95)
    print("found the number")
    print(location)
    print("centering")
    pyautogui.click(location)
    print("clicking")
    photo.close()

def start():
    print("start")
    print("press Esc to end the program")

    keyboard.add_hotkey('Esc', lambda: quit())
    keyboard.add_hotkey('0', lambda: press('./images/0.jpg'))
    keyboard.add_hotkey('1', lambda: press('./images/1.jpg'))
    keyboard.add_hotkey('2', lambda: press('./images/2.jpg'))
    keyboard.add_hotkey('3', lambda: press('./images/3.jpg'))
    keyboard.add_hotkey('4', lambda: press('./images/4.jpg'))
    keyboard.add_hotkey('5', lambda: press('./images/5.jpg'))
    keyboard.add_hotkey('6', lambda: press('./images/6.jpg'))
    keyboard.add_hotkey('7', lambda: press('./images/7.jpg'))
    keyboard.add_hotkey('8', lambda: press('./images/8.jpg'))
    keyboard.add_hotkey('9', lambda: press('./images/9.jpg'))
    keyboard.add_hotkey('delete', lambda: press('./images/delete.jpg'))
    keyboard.add_hotkey('enter', lambda: press('./images/enter.jpg'))

    global exitProgram
    exitProgram = True
    while exitProgram:
        print("still running")
        time.sleep(10)
    sys.exit()
        
start()