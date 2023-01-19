from random import random

def randomHex():
    h1 = toHex(int(random() * 16))
    h2 = toHex(int(random() * 16))
    h3 = toHex(int(random() * 16))
    h4 = toHex(int(random() * 16))
    h5 = toHex(int(random() * 16))
    h6 = toHex(int(random() * 16))
    color = "#" + h1 + h2 + h3 + h4 + h5 + h6
    return color

def toHex(value):
    match value:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"
        case _:
            return str(value)
