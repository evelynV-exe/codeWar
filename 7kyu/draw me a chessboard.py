def chess_board(rows, columns):
    solution = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i + j) % 2 == 0:
                row.append("O")
            else:
                row.append("X")
        solution.append(row)
    
    return solution

rows = 8
columns = 8

print(chess_board(rows, columns))