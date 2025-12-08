def cookie(x):
    typeV = type(x)

    if typeV is int or typeV is float:
        return 'Who ate the last cookie? It was Zach!'
    elif typeV is str:
        return 'Who ate the last cookie? It was Monica!' 
    else:
        return 'Who ate the last cookie? It was the dog!'
