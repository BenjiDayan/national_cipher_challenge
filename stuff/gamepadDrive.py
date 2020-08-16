def calc(stickx, sticky):
    #one of the sticks is appropriately reversed
    xneg = False if stickx == stickx.__abs__() else True
    yneg = False if sticky == sticky.__abs__() else True

    if not xneg and not yneg:
        left = stickx**2 + sticky**2
        right = -stickx**2 + sticky**2
    elif xneg and not yneg:
        left = -stickx**2 + sticky**2
        right = stickx**2 + sticky**2
    elif not xneg and yneg:
        left = stickx**2 - sticky**2
        right = -stickx**2 - sticky**2
    elif xneg and yneg:
        left = -stickx**2 - sticky**2
        right = stickx**2 - sticky**2

    return([left, right])
