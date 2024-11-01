# Define positions
W: tuple[int, int] = (0,  0)
A: tuple[int, int] = (0, -1)
S: tuple[int, int] = (1, -1)
D: tuple[int, int] = (1,  0)

STROKES: dict[str, list[tuple[int, int]]] = {
    '': [],
    'WA': [W, A],
    'WS': [W, S],
    'WD': [W, D],
    'DA': [D, A],
    'DS': [D, S],
    'SA': [S, A]
}