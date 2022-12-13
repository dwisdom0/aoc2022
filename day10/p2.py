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


def pchar(char):
  print(char, end='')


def print_pixel(state):
  #print(f'{state["clock"]=} {state["sprite"]=}')
  if state['clock'] != 0 and state['clock'] % 40 == 0:
    pchar('\n')

  if (
    state['clock'] % 40 >= state['sprite'] - 1 and
    state['clock'] % 40 <= state['sprite'] + 1
  ):
    pchar('#')
    #print(' ON ')
  else:
    pchar('.')
    #print(' OFF ')


def simulate(ixns):
  state = {
    'sprite': 1,
    'clock': 0,
  }

  for ixn in ixns:
    if ixn[0] == 'noop':
      print_pixel(state)
      state['clock'] += 1

    elif ixn[0] == 'addx':
      print_pixel(state)
      state['clock'] += 1
      print_pixel(state)
      state['clock'] += 1
      state['sprite'] += ixn[1]

    else:
      raise ValueError(f'Unsupported instruction: {ixn}')

def main():
  ixns = parse_input('input.txt')
  simulate(ixns)


if __name__ == '__main__':
  main()
