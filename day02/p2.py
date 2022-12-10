def parse_input(fname):
  with open(fname, 'r') as f:
    lines = f.readlines()

  games = []
  for line in lines:
    games.append(tuple(line.replace('\n', '').split(' ')))

  return games

def choice_score(game):
  """
  game looks like
  (opp's move, game outcome)
  so figure out what move will create that outcome
  and score that move
  """
  rock = 1
  paper = 2
  scissors = 3

  rock_moves = {
    'X': scissors, # lose
    'Y': rock,     # draw
    'Z': paper     # win
  }
  paper_moves = {
    'X': rock,     # lose
    'Y': paper,    # draw
    'Z': scissors  # win
  }
  scissors_moves = {
    'X': paper,     # lose
    'Y': scissors,  # draw
    'Z': rock       # win
  }

  opp_move = game[0]
  outcome = game[1]
  if opp_move == 'A':
    return rock_moves[outcome]
  elif opp_move == 'B':
    return paper_moves[outcome]
  elif opp_move == 'C':
    return scissors_moves[outcome]
  else:
    raise ValueError(f'Unexpected move: {game}')

def score_game(game):
  """
  a game looks like
  (opponent's move, game outcome)
  """
  win_lose_score = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6,  # win
  }
  return win_lose_score[game[1]] + choice_score(game)

def main():
  games = parse_input('input.txt')
  total_score = 0
  for game in games:
    total_score += score_game(game)

  print(total_score)




if __name__ == '__main__':
  main()

