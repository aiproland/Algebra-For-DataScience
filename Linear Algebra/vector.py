vector1=[ 53,160 ,30 ]
vector2=[ 53,150 ,40 ]

from typing import List
def add(V:List ,W:List):
    assert len(V) ==len(W)
    return [ v+w for v,w in zip(V,W)]

# print(add(vector1,vector2))

def subtraction(V:List ,W:List):
    assert len(V) ==len(W)
    return [ v-w for v,w in zip(V,W)]

# print(subtraction(vector1,vector2))


def multiply(c:float , V:List):
    return [v*c for v in V]

# print(multiply(3,vector1))

def dotproduct(V:List , W:List):
    assert len(V) ==len(W)
    return sum([v*w for v,w in zip(V,W)])

# print(dotproduct([2,0,0],[3,1,0]))

import math
def magnitude(V:List):
    return math.sqrt(sum([v**2 for v in V]))

# print(magnitude([1,1,0]))

def distance(V:List , W:List):
        assert len(V) ==len(W)
        difference = subtraction(V,W)
        return magnitude(difference)


print(distance([0.1 ,0,0.9] ,[0,0,1]))