import argparse

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
    'gold': 0.1,
    'silver': 0.01
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
if len(colors) == 3 or len(colors) == 4:
        # 3 or 4 bands: 2 significant digits
        first_digit = COLOR_VALUES[colors[0]]
        second_digit = COLOR_VALUES[colors[1]]
        base_value = (first_digit * 10) + second_digit
        multiplier = MULTIPLIERS[colors[2]]
        
        resistance = base_value * multiplier
        tolerance = TOLERANCES[colors[3]] if len(colors) == 4 else None
        
    elif len(colors) == 5:
        # 5 bands: 3 significant digits
        first_digit = COLOR_VALUES[colors[0]]
        second_digit = COLOR_VALUES[colors[1]]
        third_digit = COLOR_VALUES[colors[2]]
        base_value = (first_digit * 100) + (second_digit * 10) + third_digit
        multiplier = MULTIPLIERS[colors[3]]
        
        resistance = base_value * multiplier
        tolerance = TOLERANCES[colors[4]]
        
    return resistance, tolerance

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
    parser = argparse.ArgumentParser(
        description="Decode 3, 4, or 5-band resistor color codes into resistance values.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'colors', 
        metavar='COLOR', 
        type=str, 
        nargs='+',
        help="The colors of the resistor bands from left to right.\nExample: red red orange gold"
    )

    args = parser.parse_args()

    # Normalize inputs to lowercase
    input_colors = [color.lower() for color in args.colors]

    if len(input_colors) not in [3, 4, 5]:
        print("❌ Error: Please provide exactly 3, 4, or 5 colors.")
        return

    try:
        resistance, tolerance = decode_resistor(input_colors)
        formatted_res = format_resistance(resistance)
        
        print("\n--- Resistor Details ---")
        print(f"Bands:  {'-'.join(input_colors).title()}")
        
        if tolerance:
            print(f"Value:  {formatted_res} ±{tolerance}%")
            
            # Calculate the range
            variance = resistance * (tolerance / 100)
            min_res = format_resistance(resistance - variance)
            max_res = format_resistance(resistance + variance)
            print(f"Range:  {min_res} to {max_res}")
        else:
            print(f"Value:  {formatted_res} (No tolerance band)")
        print("------------------------\n")
            
    except KeyError as e:
        print(f"\n❌ Error: Unknown color {e}. Please check your spelling and use standard colors.\n")


#Run
if __name__ == "__main__":
    main()
