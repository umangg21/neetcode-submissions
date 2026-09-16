class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            my_dict = {str(x): False for x in range(1, 10)}
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if my_dict[val] is True:
                        return False
                    my_dict[val] = True
        

        for i in range(9):
            my_dict = {str(x): False for x in range(1, 10)}
            for j in range(9):
                val = board[j][i]
                if val != ".":
                    if my_dict[val] is True:
                        return False
                    my_dict[val] = True


        for i in [0,3,6]:
            count=0
            my_dict = {str(x): False for x in range(1, 10)}
            for k in range(9):
                for j in range(3):
                    count+=1
                    # print("count",count)
                    val = board[k][j+i]
                    if val != ".":
                        if my_dict[val] is True:
                            return False
                        my_dict[val] = True
                    # print(k,j+i)
                    if count == 9:
                        count=0
                        my_dict = {str(x): False for x in range(1, 10)}

        return True
        


        