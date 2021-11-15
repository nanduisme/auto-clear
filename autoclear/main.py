def clear(propmt:str="Hit ENTER to clear..."):
    """Clears terminal after hitting `ENTER`"""

    import os
    
    input(propmt)
    os.system("cls|clear")