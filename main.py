# Resistor Color Code Decoder
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
    return resistance

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
    # Test case 1: : Red, Red, Orange = 22 × 1000 = 22,000Ω
    colors1 = ['red','red','orange']
    resistance1 = decode_resistor(colors1)
    formatted1 = format_resistance(resistance1)
    print(f'Colors: {colors1} → {formatted1}')

# Test case 2: Brown, Black, Red = 10 × 100 = 1,000Ω
    colors2 = ['brown', 'black', 'red']
    resistance2 = decode_resistor(colors2)
    formatted2 = format_resistance(resistance2)
    print(f'Colors: {colors2} → {formatted2}')
    
# Test case 3: Green, Blue, Yellow = 56 × 10,000 = 560,000Ω
    colors3 = ['green', 'blue', 'yellow']
    resistance3 = decode_resistor(colors3)
    formatted3 = format_resistance(resistance3)
    print(f"Colors: {colors3} → {formatted3}")

# Run the tests
if __name__ == "__main__":
    main()
