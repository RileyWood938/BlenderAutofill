import bpy
from pynput import keyboard
logFile = open(r'logFile.txt', 'w')

logFile.write("test Write")


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        logFile.write('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        logFile.write('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    logFile.write('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

logFile.close()


readFile = open(r"logFile.txt", 'r')

print(readFile.readline())

readFile.close()