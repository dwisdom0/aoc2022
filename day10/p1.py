def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
  ixns = []
  for line in lines:
    if line == 'noop\n':
      ixns.append(('noop',))
    else:
      ixn, amount = line.replace('\n', '').split(' ')
      ixns.append((ixn, int(amount)))
  return ixns


def add_score_if_clock_20(state):
  if (state['clock'] + 20) % 40 == 0:
    this_score = state['clock'] * state['reg']
    print(f"{state['clock']}: {this_score}")
    return this_score
  return 0


def simulate(ixns):
  state = {
    'reg': 1,
    'clock': 0,
  }

  score = 0

  for ixn in ixns:
    if ixn[0] == 'noop':
      state['clock'] += 1
      score += add_score_if_clock_20(state)

    elif ixn[0] == 'addx':
      state['clock'] += 1
      score += add_score_if_clock_20(state)
      state['clock'] += 1
      score += add_score_if_clock_20(state)
      state['reg'] += ixn[1]

    else:
      raise ValueError(f'Unsupported instruction: {ixn}')

  return score


def main():
  ixns = parse_input('input.txt')
  score = simulate(ixns)
  print(score)


if __name__ == '__main__':
  main()
