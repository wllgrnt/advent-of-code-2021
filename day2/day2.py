"""day2.py

Take a series of commands, and find the final position.
"""

from typing import List, Tuple

def parse_input(input_str: str) -> List[Tuple[int, int]]:
    """
    Take the raw input, return a set of translations.
    
    E.g. forward 5 -> (5,0)
    down 4 -> (0,4)
    """
    input_list = [line.split(" ") for line in input_str.split("\n") if line]
    parsed_list = []
    for direction, magnitude in input_list:
        mag = int(magnitude)
        match direction:
            case "forward":
                parsed_list.append((mag, 0))
            case "back":
                parsed_list.append((-mag, 0))
            case "down":
                parsed_list.append((0, mag))
            case "up":
                parsed_list.append((0, -mag))
            case _:
                raise ValueError(f"found {_}, expected forward, back, up, or down")
    assert len(parsed_list) == len(input_list)
    return parsed_list

def get_final_position(directions: List[Tuple[int, int]]) -> Tuple[int, int]:
    """ go through the directions, incrementing the cursor."""
    position = [0, 0]
    for forward_mag, down_mag in directions:
        position[0] += forward_mag
        position[1] += down_mag
    return tuple(position)

def get_final_position_2(directions: List[Tuple[int, int]]) -> Tuple[int, int]:
    position = [0,0]
    aim = 0
    for forward_mag, down_mag in directions:
        if down_mag:
            aim += down_mag
        elif forward_mag:
            position[0] += forward_mag
            position[1] += aim*forward_mag
        else:
            raise ValueError("shouldn't ever be both forward and down")
    return tuple(position)

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

expected_parsed = [(5,0), (0,5), (8,0), (0, -3), (0,8), (2, 0)]

assert parse_input(test_input) == expected_parsed

assert get_final_position(parse_input(test_input)) == (15,10), get_final_position(parse_input(test_input))

assert get_final_position_2(parse_input(test_input)) == (15,60), get_final_position_2(parse_input(test_input))


if __name__ == "__main__":
  with open('input.txt') as flines:
    input_str = flines.read()

  input_parsed = parse_input(input_str)
  # part 1
  final_position = get_final_position(input_parsed)
  print(final_position)
  print(final_position[0]*final_position[1])
  # part 2
  final_position_2 = get_final_position_2(input_parsed)
  print(final_position_2)
  print(final_position_2[0]*final_position_2[1])
