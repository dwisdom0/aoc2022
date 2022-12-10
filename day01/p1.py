def read_input(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  elves = []
  accumulator = 0
  for line in lines:
    if line == '\n':
      elves.append(accumulator)
      accumulator = 0
    else:
      accumulator += int(line)
  return elves


def main(filename):
  elves = read_input(filename)
  print(elves)
  print(max(elves))


if __name__ == '__main__':
  main('input.txt')
