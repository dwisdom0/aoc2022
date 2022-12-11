def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
  pairs = []
  for line in lines:
    p1, p2 = line.replace('\n', '').split(',')
    p1 = tuple(map(int, p1.split('-')))
    p2 = tuple(map(int, p2.split('-')))
    pairs.append((p1, p2))
  return pairs

def score_overlap(pair):
  p1, p2 = pair

  # p1 start inside p2
  if p1[0] >= p2[0] and p1[0] <= p2[1]:
    return 1
  # p1 end inside p2
  if p1[1] >= p2[0] and p1[1] <= p2[1]:
    return 1
  # p2 start inside p1
  if p2[0] >= p1[0] and p2[0] <= p1[1]:
    return 1
  # p2 end inside p1
  if p2[1] >= p1[0] and p2[1] <= p1[1]:
    return 1

  # don't overlap at all
  return 0

def main():
  pairs = parse_input('input.txt')
  total_score = 0
  for pair in pairs:
    total_score += score_overlap(pair)
  print(total_score)

if __name__ == '__main__':
  main()
