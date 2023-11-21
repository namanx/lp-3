
# recursive method : 
# def fibo(n):
#     if n <= 1:
#         return n
#     return (fibo(n-1) + fibo(n-2))

# non recursive method
# def fibo(n):
#     if(n <= 1):
#         return 1
#     a = 0
#     b = 1
#     num = n

#     while (num-2 > 0):
#         c = a+b
#         a = b
#         b = c
#         print(c)
#         num -= 1
#     return 

# if __name__ == "__main__":

#     n = int(input("Please enter the number : "))
#     print("The fibonacci series is as follows :")
#     fibo(n+1)


# Huffman encoding
# import heapq
# from collections import defaultdict

# def huffman_encoding(data):
#     # Step 1: Calculate frequencies of each character
#     frequency = defaultdict(int)
#     for char in data:
#         frequency[char] += 1

#     # Step 2: Build a priority queue (min heap) based on character frequencies
#     heap = [[weight, [char, ""]] for char, weight in frequency.items()]
#     heapq.heapify(heap)

#     # Step 3: Build the Huffman Tree
#     while len(heap) > 1:
#         lo = heapq.heappop(heap)
#         hi = heapq.heappop(heap)
#         for pair in lo[1:]:
#             pair[1] = '0' + pair[1]
#         for pair in hi[1:]:
#             pair[1] = '1' + pair[1]
#         heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

#     # Step 4: Create a dictionary to store Huffman codes
#     huffman_dict = dict(heap[0][1:])

#     # Step 5: Encode the input data
#     encoded_data = ''.join([huffman_dict[char] for char in data])

#     return encoded_data, huffman_dict

# def huffman_decoding(encoded_data, huffman_dict):
#     # Reverse the Huffman dictionary for decoding
#     reverse_dict = {code: char for char, code in huffman_dict.items()}
    
#     # Decode the encoded data
#     current_code = ""
#     decoded_data = ""
#     for bit in encoded_data:
#         current_code += bit
#         if current_code in reverse_dict:
#             decoded_data += reverse_dict[current_code]
#             current_code = ""

#     return decoded_data

# # Example Usage:
# data = "abracadabra"
# encoded_data, huffman_dict = huffman_encoding(data)
# decoded_data = huffman_decoding(encoded_data, huffman_dict)

# print("Original data:", data)
# print("Encoded data:", encoded_data)
# print("Decoded data:", decoded_data)


# Fractional Knapsack

# class Item:
#     def __init__(self,weight,value) -> None:
#         self.weight = weight
#         self.value = value
#         self.value_per_weight = value/weight

# def fractional_knapsack(capacity,items):
    
#     items.sort(key = lambda x : x.value_per_weight,reverse = True)

#     total_value = 0
#     knapsack = [0] * len(items)

#     for i,item in enumerate(items):
        
#         if item.weight <= capacity:
#             knapsack[i] = 1
#             capacity -= item.weight
#             total_value += item.value
#         else:
#             fraction = capacity / item.weight
#             knapsack[i] = fraction
#             total_value += item.value * fraction
#             break
    
#     return knapsack,total_value

# items = [Item(1,10),Item(2,20),Item(4,40),Item(7,70),Item(3,10),Item(5,50)]
# capacity = 10

# knapsack , total_value = fractional_knapsack(capacity,items)

# print(f"knapsack : {knapsack}")
# print(f"total price : {total_value}")

# 0 / 1 Knapsack 


class Nqueens:


    def solveNQueens(self, n: int):
        col = set()
        posDiag = set() # r+c
        negDiag = set() # r-c

        res =[]
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # r == n is out of bounds 
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
if __name__ == "__main__":
    obj = Nqueens()
    i = 1
    for x in obj.solveNQueens(4):
        print(f"==== Solution Number {i} ====")
        for y in x:
            print(y)
        i += 1
        

                        
            