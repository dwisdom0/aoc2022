from string import ascii_lowercase, ascii_uppercase
def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()

  packs = []
  for line in lines:
    line = line.replace('\n', '')
    compartment_split = len(line) // 2
    packs.append((set(line[:compartment_split]), set(line[compartment_split:])))

  return packs

def score_pack(pack):
  # convert to a list to get the element out of the set
  # problem guarantees only 1 overlapping element
  overlapping_char = list(pack[0].intersection(pack[1]))[0]
  yardstick = ascii_lowercase + ascii_uppercase
  return yardstick.index(overlapping_char) + 1

def main():
  packs = parse_input('input.txt')
  total_score = 0
  for pack in packs:
    total_score += score_pack(pack)
  print(total_score)



if __name__ == '__main__':
  main()
