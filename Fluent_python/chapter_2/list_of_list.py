# Building a Tic-Tac-Toe Board 

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

'''  
A list with three references to the same list is useless
'''
weired_board = [['_'] * 3] * 3
print(weired_board)


# This is why the above made error 
board = []

for i in range(3):
    row = ['_'] * 3
    board.append(row)

print(board)    


board[2][0] = 'X'
print(board)

