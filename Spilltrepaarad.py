board = [["0","1","2"],["3","4","5"],["6","7","8"]]

def printboard():
    for i in board:
        print(i) 

printboard()

def main():
    gamereset = 0
    while gamereset < 9:
        print("Velg din posisjon Spiller X:", end = "")
        x = int(input())
        print("Velg din posisjon Spiller Y:", end = "")
        y = int(input())
        
        print(board[x][y], end=' ')
        print(board)
    gamereset += 1
    
if __name__ == '__main__':
	main()





