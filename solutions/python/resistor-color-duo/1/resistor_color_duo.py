def value(colors):
    number = ''.join(color_codes[color] for color in colors[:2])
    return int(number)

color_codes = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9"
}