"""A module with a single function that clears terminal after a prompt"""

def clear(propmt:str="Hit ENTER to clear...", no_prompt:bool=False):
    """Clears terminal after hitting `ENTER` if `no_prompt` is `False` otherwise, just clears terminal."""

    if not no_prompt:
        input(propmt)

    import os
    os.system("cls|clear")