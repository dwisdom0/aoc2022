from enum import Enum

class E(Enum):
  AIR = 0
  ROCK = 1
  SAND = 2

def parse_input(fname):
  with open(fname, 'r') as f:
    text_lines = f.readlines()

  rock_paths = []
  for text_line in text_lines:
    rock_path = []
    for coord in text_line.replace('\n', '').split(' -> '):
      rock_node = list(map(int, coord.split(',')))
      rock_path.append(tuple(rock_node))
    rock_paths.append(rock_path)

  # add a floor
  rock_paths.append([(0, 168), (999, 168)])

  return rock_paths

def build_grid(rock_paths):
  # make it a full 1000 wide
  # so that there's room for the sand

  height = 169
  width = 1000
  grid = [[E.AIR] * width]
  for _ in range(height):
    grid.append([E.AIR] * width)

  for rock_path in rock_paths:
    grid = add_rock_path(grid, rock_path)

  return grid


def add_horizontal_rock(grid, start, end):
  # put start and end in sorted order
  i = start[1]
  j1 = start[0]
  j2 = end[0]
  j1, j2 = sorted((j1, j2))
  for j in range(j1, j2+1):
    if grid[i][j] != E.ROCK:
      grid[i][j] = E.ROCK

  return grid


def add_vertical_rock(grid, start, end):
  # put start and end in sorted order
  j = start[0]
  i1 = start[1]
  i2 = end[1]
  i1, i2 = sorted((i1, i2))
  for i in range(i1, i2+1):
    if grid[i][j] != E.ROCK:
      grid[i][j] = E.ROCK

  return grid


def add_rock_path(grid, rock_path):
  prev_node = rock_path[0]
  for cur_node in rock_path[1:]:
    if prev_node[0] == cur_node[0]:
      grid = add_vertical_rock(grid, prev_node, cur_node)
    elif prev_node[1] == cur_node[1]:
      grid = add_horizontal_rock(grid, prev_node, cur_node)
    else:
      raise ValueError(f'non-orthogonal rock path: {prev_node} -> {cur_node}')
    prev_node = cur_node

  return grid


def is_empty(val):
  # have to say 0 for my test grid
  if val == E.AIR or val == 0:
    return True
  return False


def drop_sand(grid, drop_idx):
  sand_loc = (0, drop_idx)
  while True:
    sand_loc, sand_stopped = tick_sand(grid, sand_loc)
    if sand_stopped:
      print(sand_loc)
      break
  # if we stopped at the origin, raise an IndexError
  # to show that we're done
  if sand_loc[0] == 0 and sand_loc[1] == 500:
    raise IndexError

  grid[sand_loc[0]][sand_loc[1]] = E.SAND
  return grid

def tick_sand(grid, sand_loc):
  # check below
  below = grid[sand_loc[0] + 1][sand_loc[1]]
  if is_empty(below):
    return (sand_loc[0] + 1, sand_loc[1]), False

  # check left
  left = grid[sand_loc[0] + 1][sand_loc[1] - 1]
  if is_empty(left):
    return (sand_loc[0] + 1, sand_loc[1] - 1), False

  # check right
  left = grid[sand_loc[0] + 1][sand_loc[1] + 1]
  if is_empty(left):
    return (sand_loc[0] + 1, sand_loc[1] + 1), False

  return sand_loc, True

def sim_sand(grid, drop_loc):
  total = 0
  while True:
    try:
      drop_sand(grid, drop_loc)
      total += 1
    except IndexError:
      return total

def print_grid(grid):
  to_print = ''
  for i, row in enumerate(grid):
    for j, cell in enumerate(row):
      if i == 0:
        to_print += str(j % 10)
        continue
      if j == 0:
        to_print += str(i % 10)
        continue
      if cell == E.AIR or cell == 0:
        to_print += '.'
      elif cell == E.ROCK or cell == 1:
        to_print += '#'
      elif cell == E.SAND or cell == 2:
        to_print += 'o'
    to_print += '\n'
  print(to_print)


def main():
  rock_paths = parse_input('input.txt')

  grid = build_grid(rock_paths)
  print_grid(grid)


  grid = build_grid(rock_paths)
  real_score = sim_sand(grid, 500)
  print_grid(grid)
  print('\n')
  print(real_score + 1)

if __name__ == '__main__':
  main()
