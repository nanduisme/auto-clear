CHANGELOG
=========

v0.0.1 (15 Nov 2021)<br>
- `clear()` added.

<br>

v0.0.2 (15 Nov 2021)<br>
- Rebranded to `mytools`.

- `mytools.autoclear.clear()` takes a `prompt` of type `str` and `no_prompt` of type `bool` as arguments.

- Argument `no_prompt` is optional. If not provided, it defaults to `False`. If `True`, the `prompt` is not printed for conformation.

- Added `mytools.xotools` to the `mytools` package with one function `check_win`.

- `mytools.xotools.check_win()` takes in 2 arguments, `board` which is a nested `list`/`tuple` and `player_marker` which can be of any type denotin the marker of the player to be checked, on the `board`.

- `mytools.xotools.check_win()` returns `True` if the player has won the game, according to traditional tic-tac-toe rules, `False` otherwise.