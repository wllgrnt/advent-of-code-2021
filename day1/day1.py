from typing import List

def parse_input(input_str: str) -> List[int]:
  parsed_input = [int(line) for line in input_str.split('\n') if line]
  return parsed_input

def count_increases(input_ints: List[int]) -> int:
  increases = -1  # to account for first val 
  prev_val = 0
  for val in input_ints:
    if val > prev_val:
      increases += 1
    prev_val = val
  return increases 

def count_window_increases(input_ints: List[int]) -> int:
  """Get rolling windows"""
  prev_sum = 0
  increases = -1
  for i in range(3, len(input_ints)+1):
    rolling_sum = sum(input_ints[i-3:i])
    if rolling_sum > prev_sum:
      increases += 1
    prev_sum = rolling_sum
  return increases



test_input = """199
200
208
210
200
207
240
269
260
263
"""

assert parse_input(test_input) == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

assert count_increases(parse_input(test_input)) == 7, count_increases(parse_input(test_input))

assert count_window_increases(parse_input(test_input)) == 5, count_window_increases(parse_input(test_input))

if __name__ == "__main__":
  with open('day1/input.txt') as flines:
    input_str = flines.read()

  # part 1
  increases = count_increases(parse_input(input_str))
  print(increases)

  # part 2
  rolling_increases = count_window_increases(parse_input(input_str))
  print(rolling_increases)