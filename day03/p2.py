from string import ascii_lowercase, ascii_uppercase
def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()

  packs = []
  for line in lines:
    line = line.replace('\n', '')
    packs.append(set(line))

  # group the packs into groups of 3
  group_size = 3
  groups = []
  for i in range(0, len(packs), group_size):
    groups.append(packs[i:i+group_size])

  return groups

def score_group(group):
  # convert to a list to get the element out of the set
  # problem guarantees only 1 overlapping element
  overlap = group[0].intersection(group[1]).intersection(group[2])
  overlapping_char = list(overlap)[0]
  yardstick = ascii_lowercase + ascii_uppercase
  return yardstick.index(overlapping_char) + 1

def main():
  groups = parse_input('input.txt')
  total_score = 0
  for group in groups:
    total_score += score_group(group)
  print(total_score)



if __name__ == '__main__':
  main()
