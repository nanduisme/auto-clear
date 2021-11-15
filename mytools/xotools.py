def check_win(board: list, player_marker) -> bool:
    """Checks win on a given tic-tac-toe board.
    - `board` must be a 3x3 nested `list` or `tuple`.
    - `player_marker` must be the marker of the player that has to be checked for the win.
    - Returns `True` if `player_marker` has got 3 in a row, either veritcally, horizontally or diagonal.
    - Return `False` in all other cases."""

    type_check_successful = False

    # Type check
    if isinstance(board, (tuple, list)) and len(board) == 3:
        for row in board:
            if isinstance(row, (tuple, list)) and len(row) == 3:
                type_check_successful = True

    if not type_check_successful:
        raise TypeError("arugment board must be a 3x3 nested list or tuple")

    # Row case
    for row in board:
        if row == [player_marker for _ in range(3)]:
            return True

    # Column case
    for i in range(3):
        column = [row[i] for row in board]
        if column == [player_marker for _ in range(3)]:
            return True

    # Diagonal case [Returns False as default case as well]
    return (
        board[0][0] == board[1][1] == board[2][2] == player_marker
        or board[0][2] == board[1][1] == board[2][0] == player_marker
    )
