from picarx import Picarx
from time import sleep
from pynput import keyboard

#User manual to be printed in console
manual = '''
Press keys on keyboard to control PiCar-X!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    ctrl+c: Quit
'''

#Clears console and prints manual
def show_info():
    print("\033[H\033[J",end='')
    print(manual)
       
#Resets all moving parts of the robot to 0
def reset():
    px.stop()
    sleep(.1)
    px.set_dir_servo_angle(0)
    sleep(.1)
    px.set_cam_pan_angle(0)
    sleep(.1)
    px.set_cam_tilt_angle(0)
    sleep(.1)

def key_pressed(key):
    try:
        # Agregar tecla a la lista de teclas presionadas
        teclas_presionadas.add(key.char)

        if 'w' in teclas_presionadas:
            px.forward(POWER)
        if 'a' in teclas_presionadas:
            px.set_dir_servo_angle(LEFT)
        if 'd' in teclas_presionadas:
            px.set_dir_servo_angle(RIGHT)
        if 's' in teclas_presionadas:
            px.backward(POWER)
        if 'q' in teclas_presionadas:
            reset()

    except AttributeError:
        pass

    show_info()

def key_released(key):
    try:
        if key.char == 'w' or key.char == 's':
            px.forward(0)

        if key.char == 'a' or key.char == 'd':
            px.set_dir_servo_angle(0)

        #quita la tecla de la lista 'teclas_presionadas'
        teclas_presionadas.remove(key.char)

    except KeyError:
        pass

def keyboard_control():
    with keyboard.Listener(on_press=key_pressed, on_release=key_released) as listener:
        listener.join()


if __name__ == "__main__":
    try:
        px = Picarx()
        POWER = 100
        RIGHT = 25
        LEFT = -25
        teclas_presionadas = set()

        keyboard_control()

    except KeyboardInterrupt:
        print('quit')

    finally:
        reset()
    