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
      # subtract 450 from the horizontal value
      rock_node[0] -= 450
      rock_path.append(tuple(rock_node))
    rock_paths.append(rock_path)

  return rock_paths

def build_grid(rock_paths):
  # happen to know that my rocks fit
  # on a grid with dimensions
  # 70 x 166

  # make a grid that doesn't fall into Python traps
  height = 167
  width = 71
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
      break
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
  for rock_path in sorted(rock_paths):
    print(rock_path)

  # what are the dimensions of the grid?
  max_0 = 0
  min_0 = 500
  max_1 = 0
  min_1 = 500
  for rock_path in rock_paths:
    for coord in rock_path:
      if coord[0] > max_0:
        max_0 = coord[0]
      if coord[0] < min_0:
        min_0 = coord[0]
      if coord[1] > max_1:
        max_1 = coord[1]
      if coord[1] < min_1:
        min_1 = coord[1]
  print(f'{max_0=}')  # 519
  print(f'{min_0=}')  # 451
  print(f'{max_1=}')  # 166
  print(f'{min_1=}')  # 14

  # so probably do like 1 larger than that
  # I could subtract the min from every coord
  # to map it to a more reasonable range
  # can't do that for the vertical dimension
  # but I think it should be okay for the horizontal dim

  # yeah I'm going to subtract 450 from every horizontal value



  # search all the possible starting points
  # for debugging
  grid = build_grid(rock_paths)
  print_grid(grid)
  totals = []
  for i in range(len(grid[0])):
    grid = build_grid(rock_paths)
    totals.append(sim_sand(grid, i))

  print(totals)


  # do a real run at the right starting point
  grid = build_grid(rock_paths)
  real_score = sim_sand(grid, 50)
  print_grid(grid)
  print('\n')
  print(real_score)

if __name__ == '__main__':
  main()
