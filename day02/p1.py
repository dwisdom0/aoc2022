def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()

  games = []
  for line in lines:
    games.append(tuple(line.replace('\n', '').split(' ')))

  return games

def win_lose_score(game):
  """
  rock beats scissors
  scissors beat paper
  paper beats rock
  """
  i_lose = 0
  draw = 3
  i_win = 6
  rock_results = {
    'X': draw,    # rock
    'Y': i_win,   # paper
    'Z': i_lose   # scissors
  }
  paper_results = {
    'X': i_lose,  # rock
    'Y': draw,    # paper
    'Z': i_win    # scissors
  }
  scissors_results = {
    'X': i_win,   # rock
    'Y': i_lose,  # paper
    'Z': draw     # scissors
  }

  opp_move = game[0]
  my_move = game[1]
  if opp_move == 'A':
    return rock_results[my_move]
  elif opp_move == 'B':
    return paper_results[my_move]
  elif opp_move == 'C':
    return scissors_results[my_move]
  else:
    raise ValueError(f'Unexpected move: {game}')

def score_game(game):
  """
  a game looks like
  (opponent's move, my move)
  """
  choice_score = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
  }
  return win_lose_score(game) + choice_score[game[1]]

def main():
  games = parse_input('input.txt')
  total_score = 0
  for game in games:
    total_score += score_game(game)

  print(total_score)




if __name__ == '__main__':
  main()

