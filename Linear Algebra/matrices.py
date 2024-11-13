





friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # user9
                 ] 
from typing  import List


Matrix =List[List[float]]

def shape(A:Matrix):
    num_row    = len(A)
    num_column = len(A[0])
    return num_row,num_column


# print(shape(friend_matrix))

def get_row(A:Matrix , i:int):
    return A[i]
# print(get_row(friend_matrix , 9))

def get_column(A:Matrix , j:int):
    return [i[j] for i in A]

# print(get_column(friend_matrix , 5))

def find_friends(A:Matrix , i:int):
    return [ index for index , j in enumerate(A[i]) if j ]

print(find_friends(friend_matrix , 5))

