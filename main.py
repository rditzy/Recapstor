# resistor_color_code_decoder.py

def decode_color_code(color_code):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9,
    }

    # Split the color code into individual colors
    colors = color_code.split()
    if len(colors) < 3:
        raise ValueError("Must provide at least three colors")

    # Decode the resistor value
    value = color_map[colors[0]] * 10 + color_map[colors[1]]
    multiplier = color_map[colors[2]]

    return value * (10 ** multiplier)

# Example usage
if __name__ == '__main__':
    print(decode_color_code('red orange yellow'))  # Output: 23
