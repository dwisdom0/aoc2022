def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
  # convert them all to integers
  for i, line in enumerate(lines):
    lines[i] = list(map(int, line.replace('\n', '')))
  return lines

def score_left(forest, tree):
  score = 0
  # reverse to search from right to left
  for h in reversed(forest[tree[1]][0:tree[0]]):
    if h >= tree[2]:
      # count the tree that blocks the view
      return score + 1
    score += 1
  return score

def score_right(forest, tree):
  score = 0
  for h in forest[tree[1]][tree[0]+1:]:
    if h >= tree[2]:
      # count the tree that blocks the view
      return score + 1
    score += 1
  return score

def score_up(forest, tree):
  score = 0
  # reversed to search from bottom to top
  for i in range(len(forest[:tree[1]])-1, -1, -1):
    h = forest[i][tree[0]]
    if h >= tree[2]:
      # count the tree that blocks the view
      return score + 1
    score += 1
  return score


def score_down(forest, tree):
  score = 0
  for i, row in enumerate(forest[tree[1]+1:]):
    for j, h in enumerate(row):
      if j != tree[0]:
        continue
      if h >= tree[2]:
        # count the tree that blocks the view
        return score + 1
      score += 1
  return score

def visibility_score(forest, tree):
  """
  forest is a grid
  tree is tuple of a tree's x, y postition in the grid
  plus the tree's height
  like (x, y, height)
  """
  total_score = 1
  for score in [
    score_left,
    score_right,
    score_up,
    score_down
  ]:
    total_score *= score(forest, tree)
  return total_score

def max_score_forest(forest):
  max_score = 0
  # skip the edges since we know those are all score 0
  for i, row in enumerate(forest[1:-1]):
    for j, h in enumerate(row[1:-1]):
      # (x, y, height)
      # (j, i, height) <-- Swapping the indexes like this was a mistake.
      #                    It really messed with my head when I tried
      #                    to debug this code.
      # add 1 back since we skipped the edges
      score = visibility_score(forest, (j+1, i+1, h))
      if score > max_score:
        max_score = score
  return max_score

def main():
  forest = parse_input('input.txt')
  print(max_score_forest(forest))

if __name__ == '__main__':
  main()
