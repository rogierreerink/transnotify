globalVars = dict()


def setGlobal(name: str, obj: object) -> None:
    """
    Set a global variable.
    """
    global globalVars
    globalVars[name] = obj


def getGlobal(name: str) -> object:
    """
    Get a global variable.
    """
    global globalVars
    return globalVars[name]
