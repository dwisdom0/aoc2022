def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
  # convert them all to integers
  for i, line in enumerate(lines):
    lines[i] = list(map(int, line.replace('\n', '')))
  return lines

def is_visible_left(forest, tree):
  for h in forest[tree[1]][0:tree[0]]:
    if h >= tree[2]:
      return False
  return True

def is_visible_right(forest, tree):
  for h in forest[tree[1]][tree[0]+1:]:
    if h >= tree[2]:
      return False
  return True

def is_visible_up(forest, tree):
  for i, row in enumerate(forest[:tree[1]]):
    for j, h in enumerate(row):
      if j != tree[0]:
        continue
      if h >= tree[2]:
        return False
  return True

def is_visible_down(forest, tree):
  for i, row in enumerate(forest[tree[1]+1:]):
    for j, h in enumerate(row):
      if j != tree[0]:
        continue
      if h >= tree[2]:
        return False
  return True

def is_visible(forest, tree):
  """
  forest is a grid
  tree is tuple of a tree's x, y postition in the grid
  plus the tree's height
  like (x, y, height)
  """
  for check in [
    is_visible_left,
    is_visible_right,
    is_visible_up,
    is_visible_down
  ]:
    if check(forest, tree):
      return 1
  return 0

def score_forest(forest):
  total_visible = (len(forest) - 1 )* 4
  # skip the edges since we know all of those are visible
  for i, row in enumerate(forest[1:-1]):
    for j, h in enumerate(row[1:-1]):
      # (x, y, height)
      # (j, i, height)
      # add 1 back since we skipped the edges
      total_visible += is_visible(forest, (j+1, i+1, h))
  return total_visible

def main():
  forest = parse_input('input.txt')
  print(score_forest(forest))

if __name__ == '__main__':
  main()
