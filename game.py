# Tic-Tac-Toe AI using Minimax


def print_board(board):
    """Display the current Tic-Tac-Toe board."""

    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board):
    """Return the winner if there is one."""

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c]:

            if board[a] != " ":
                return board[a]

    return None


def is_board_full(board):
    """Check whether the board is full."""

    return " " not in board


def minimax(board, is_maximizing):
    """
    Minimax algorithm.

    AI (O) tries to maximize the score.
    Human (X) tries to minimize the score.
    """

    winner = check_winner(board)

    # AI wins
    if winner == "O":
        return 1

    # Human wins
    if winner == "X":
        return -1

    # Draw
    if is_board_full(board):
        return 0

    # AI's turn - maximize score
    if is_maximizing:

        best_score = -float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # Human's turn - minimize score
    else:

        best_score = float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def get_best_move(board):
    """Find the best move for the AI."""

    best_score = -float("inf")
    best_move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def get_player_move(board):
    """Get a valid move from the player."""

    while True:

        try:

            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already occupied.")
                continue

            return move

        except ValueError:

            print("Please enter a valid number.")


def main():

    board = [" "] * 9

    print("=" * 35)
    print("       TIC-TAC-TOE AI")
    print("=" * 35)

    print("\nYou are X")
    print("AI is O")

    print("\nBoard positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:

        # Human turn
        player_move = get_player_move(board)

        board[player_move] = "X"

        print_board(board)

        winner = check_winner(board)

        if winner == "X":
            print("🎉 You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")

        ai_move = get_best_move(board)

        board[ai_move] = "O"

        print_board(board)

        winner = check_winner(board)

        if winner == "O":
            print("AI wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()