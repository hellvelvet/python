def row_correct(sudoku: list, column_no: int):
    a = []
    b = 1
    c = 0
    d = 0
    for i in range(len(sudoku)):
        a.append(sudoku[i][column_no])
    for i in a:
        if i == 0:
            c += 1
    while d < c:
        a.remove(0)
        d += 1
    print(c)
    print(a)
    myset = set(a)
    if len(a) != len(myset):
        return False
    return True

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 7, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]


print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))