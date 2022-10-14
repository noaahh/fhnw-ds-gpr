input = None
with open('input.txt') as file:
    input = [line.strip() for line in file.readlines()]

subsystem_numbers = input[0].split(',')

def create_boards_array(boards_input, dimension=5):
    boards = []
    for i in range(0, len(boards_input), dimension + 1):
        board = []
        for y in range(i, i + dimension):
            if boards_input[y] != '':
                board.append(
                    list(filter(lambda x: (x != ''), boards_input[y].split(' '))))

        boards.append(board)
    return boards

boards = create_boards_array(input[2:])

def is_board_winner(board, chosen_numbers):
    for i in range(0, len(board)):
        row_matches = []
        for y in range(0, len(board[i])):
            row_matches.append(board[i][y] in chosen_numbers)

        if all(row_matches):
            return True

        for col in range(0, len(board[0])):
            col_matches = []
            for row in range(0, len(board)):
                col_matches.append(board[row][col] in chosen_numbers)

            if all(col_matches):
                return True
        
    return False


def get_board_score(board, chosen_numbers, winner_number):
    unchosen_sum = 0
    for i in range(0, len(board)):
        for y in range(0, len(board[i])):
            unchosen_sum += int(board[i][y]
                                ) if board[i][y] not in chosen_numbers else 0

    return unchosen_sum * int(winner_number)


last_winner = None
for i in range(0, len(subsystem_numbers)):
    last_winners = list(filter(lambda x: (is_board_winner(x, subsystem_numbers[:i + 1])), boards))

    if len(last_winners) >= 1:
        print(len(last_winners))
        last_winner = (i, last_winners[-1])

    boards = list(filter(lambda x: (x not in last_winners), boards))
   
        
print('done')
print(f'winner board score: {get_board_score(last_winner[1], subsystem_numbers[:last_winner[0] + 1], subsystem_numbers[last_winner[0]])}')