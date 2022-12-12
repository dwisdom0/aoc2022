def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()

  return lines[0].replace('\n' ,'')

def search_stream(stream):
  window = 4
  for i, c in enumerate(stream):
    if i < window:
      continue
    data = stream[i-window:i]
    if len(set(data)) == window:
      return i

  raise ValueError(f'no block of {window} non-repeating characters')


def main():
  stream = parse_input('input.txt')
  print(stream[:20])
  print(stream[-20:])
  res = search_stream(stream)
  print(res)

if __name__ == '__main__':
  main()
