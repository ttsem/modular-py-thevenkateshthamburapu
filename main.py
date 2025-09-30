from color_code_utils import get_color_from_pair_number, color_pair_to_string

def print_color_code_table():
    print("Pair Number | Major Color | Minor Color")
    print("----------------------------------------")
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        print(f"{pair_number:11} | {major_color:11} | {minor_color}")

def generate_reference_manual():
    print("\nReference Manual for Wiring Personnel")
    print("-------------------------------------")
   _number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        color_name = color_pair_to_string(major_color, minor_color)
        print(f"{pair_number:02d}: {color_name}")

if __name__ == '__main__':
    print_color_code_table()
    generate_reference_manual()
