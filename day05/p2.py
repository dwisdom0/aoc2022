from collections import deque
from string import ascii_uppercase, ascii_lowercase

def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()
    # happen to know that the diagram is 8 lines tall
    diagram = lines[:9]
    # 2 empty lines, then commands
    commands = lines[10:]

  return diagram, commands

def idx_to_stack(idx):
  # 1, 5, 9, 13, 17, 21, 25, ...
  # 1, 2, 3,  4,  5,  6,  7, ...
  return (idx - 1)  // 4

def parse_diagram(diagram):
  # set up 9 stacks
  stacks = []
  for _ in range(9):
    stacks.append(deque())
  # load the data into the stacks
  for line in diagram:
    for i, c in enumerate(line):
      if c in ascii_uppercase:
        stack_idx = idx_to_stack(i)
        stacks[stack_idx].appendleft(c)

  return stacks

def parse_command(command):
  parsed_command = []
  cmd = command.replace('\n', '').split(' ')
  return tuple(map(int, (cmd[1], cmd[3], cmd[5])))

def apply_command(stacks, command):
  print('\n')
  print(command)
  steps = parse_command(command)
  count = steps[0]
  src_idx = steps[1] - 1
  dst_idx = steps[2] - 1

  to_add = []
  for _ in range(count):
    to_add.append(stacks[src_idx].pop())
  stacks[dst_idx].extend(reversed(to_add))

  for stack in stacks:
    print(stack)

  return stacks


def main():
  diagram, commands = parse_input('input.txt')
  stacks = parse_diagram(diagram)
  for l in diagram:
    print(l, end='')
  print()
  for stack in stacks:
    print(stack)

  for command in commands:
    stacks = apply_command(stacks, command)

  # get the final answer
  for stack in stacks:
    print(stack)

  # get the final answer
  print()
  for stack in stacks:
    print(stack.pop(), end='')
  print()



if __name__ == '__main__':
  main()
