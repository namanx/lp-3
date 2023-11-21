class Solution:
    def SolveMatrix(self,n : int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."]*n for _ in range(n)]
    

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

                board[r][c] = "."
        backtrack(0)
        return res

o = Solution()

i=0
print("Lets place the queen :")
r = int(input("Enter the number of row :"))
c = int(input("Enter the number of column :"))
for x in o.SolveMatrix(8): 
    if x[r-1][c-1] == "Q":
        print(f"Solution {i+1}")
        i+=1
        for y in x:
            print(y)



