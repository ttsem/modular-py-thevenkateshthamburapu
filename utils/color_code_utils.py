from constants.colors import MAJOR_COLORS, MINOR_COLORS

class ColorCodeError(Exception):
    pass

def color_pair_to_string(major_color, minor_color):
    return f"{major_color} {minor_color}"

def get_color_from_pair_number(pair_number):
    if pair_number < 1 or pair_number > len(MAJOR_COLORS) * len(MINOR_COLORS):
        raise ColorCodeError("Pair number out of valid range")
    zero_based = pair_number - 1
    major_index = zero_based // len(MINOR_COLORS)
    minor_index = zero_based % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError as e:
        raise ColorCodeError(str(e))
    return major_index * len(MINOR_COLORS) + minor_index + 1
