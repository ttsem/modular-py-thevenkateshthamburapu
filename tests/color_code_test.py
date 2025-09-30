
from utils.color_utils import get_color_from_pair_number, get_pair_number_from_color

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    return major_color == expected_major_color and minor_color == expected_minor_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    return pair_number == expected_pair_number
