score_board = {"W": 0, "D": 0, "L": 0}
name = input()
game_count = int(input())

for i in range(game_count):
    outcome = input()
    if outcome in score_board:
        score_board[outcome] += 1

if game_count == 0:
    print(f"{name} hasn't played any games during this season.")
else:
    points = (score_board["W"] * 3) + (score_board["D"] * 1) + (score_board["L"] * 0)
    win_rate = (score_board["W"]/game_count) * 100
    wins = score_board["W"]
    draws = score_board["D"]
    loses = score_board["L"]
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {win_rate:.2f}%")