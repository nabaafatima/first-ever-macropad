import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import DirectPins
keyboard = KMKKeyboard()
keyboard.matrix = DirectPins(
    pins = (board.D9, board.D11, board.D10, board.D8),
    value_when_pressed = False,
    pull= True,
)
keyboard.keymap = [
    [
        KC.macro(KC.LCTRL, KC.C)
        KC.macro(KC.LCTRL, KC.V)
        KC.macro(KC.LCTRL, KC.Z)
        KC.macro(KC.LCTRL, KC.Y)
    ]
]
if __name__ == '__main__':
    keyboard.go()
