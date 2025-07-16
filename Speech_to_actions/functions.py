import pyautogui

function_associations = {}


def up():
    pyautogui.press('up')

def down():
    pyautogui.press('down')

def winkey():
    pyautogui.press('winleft')

def soundclose():
    pyautogui.press("volumemute")


true_associations = {"up-key":up, "down-key":down, "window-key":winkey, "sound-mute":soundclose}