# resistor_color_code_decoder.py
COLOR_VALUES = { 
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4, 
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'gray': 8, #Alternative spelling
    'white': 9
}

MULTIPLIERS = { 
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 1000,
    'yellow': 10000,
    'green': 100000,
    'blue': 1000000,
    'violet': 10000000,
    'grey': 100000000,
    'gray': 100000000,  #Alternative spelling
    'white':1000000000,
}

TOLERANCES = {
    'brown': '±1%',
    'red': '±2%',
    'green': '±0.5%',
    'blue': '±0.25%',
    'violet': '±0.1%',
    'gold': '±5%',
    'silver': '±10%'
}

def decode_resistor(colors):
    # Get the first two digits
    first_digit = COLOR_VALUES[colors[0]]
    second_digit = COLOR_VALUES[colors[1]]

    # Combine them into a two-digit number
    base_value = (first_digit * 10) + second_digit

    # Get the multiplier from the third color
    multiplier = MULTIPLIERS[colors[2]]

    # Calculate final resistance
    resistance = base_value * multiplier
    # Check if there's a 4th band for tolerance value
    if len(colors) == 4:
        tolerance = TOLERANCES[colors[3]]
        return resistance, tolerance
    else:
        return resistance, None

def format_resistance(ohms):
    if ohms >= 1000000:           # If >= 1 million, use Megaohms
        megaohms = ohms / 1000000
        return f'{megaohms}MΩ'
    elif ohms >= 1000:            # If >= 1 thousand, use Kilohms
        kilohms = ohms / 1000 
        return f'{kilohms}KΩ'
    else:
        return f'{ohms}Ω'         # Otherwise use Ohms

def main():
    # Test case 1: Red, Red, Orange, Gold = 22kΩ ±5%
    colors1 = ['red', 'red', 'orange', 'gold']
    resistance1, tolerance1 = decode_resistor(colors1)
    formatted1 = format_resistance(resistance1)
    print(f"Colors: {colors1} → {formatted1} {tolerance1}")
    
    # Test case 2: Brown, Black, Red, Brown = 1kΩ ±1%
    colors2 = ['brown', 'black', 'red', 'brown']
    resistance2, tolerance2 = decode_resistor(colors2)
    formatted2 = format_resistance(resistance2)
    print(f"Colors: {colors2} → {formatted2} {tolerance2}")
    
    # Test case 3: Green, Blue, Yellow, Silver = 560kΩ ±10%
    colors3 = ['green', 'blue', 'yellow', 'silver']
    resistance3, tolerance3 = decode_resistor(colors3)
    formatted3 = format_resistance(resistance3)
    print(f"Colors: {colors3} → {formatted3} {tolerance3}")
    
    # Test case 4: Without tolerance band (3 colors)
    colors4 = ['red', 'red', 'orange']
    resistance4, tolerance4 = decode_resistor(colors4)
    formatted4 = format_resistance(resistance4)
    if tolerance4:
        print(f"Colors: {colors4} → {formatted4} {tolerance4}")
    else:
        print(f"Colors: {colors4} → {formatted4}")

#Run
if __name__ == "__main__":
    main()
