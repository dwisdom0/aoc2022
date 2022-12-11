def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
  pairs = []
  for line in lines:
    p1, p2 = line.replace('\n', '').split(',')
    p1 = tuple(p1.split('-'))
    p2 = tuple(p2.split('-'))
    pairs.append((p1, p2))
  return pairs

def score_overlap(pair):
  p1, p2 = pair
  # p1 inside p2
  # ---***---
  # --*****--
  if int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
    return 1
  # p2 inside p1
  # --*****--
  # ---***---
  if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
    return 1

  # don't overlap completely
  return 0

def main():
  pairs = parse_input('input.txt')
  total_score = 0
  for pair in pairs:
    total_score += score_overlap(pair)
  print(total_score)

if __name__ == '__main__':
  main()
