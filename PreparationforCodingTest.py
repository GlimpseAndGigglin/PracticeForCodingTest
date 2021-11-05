# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# 문제 설명
#
# 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다. 점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요. 단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.
# 제한사항
# v는 세 점의 좌표가 들어있는 2차원 배열입니다.
# v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
# 좌표값은 1 이상 10억 이하의 자연수입니다.
# 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.
#
# v	result
# [[1, 4], [3, 4], [3, 10]]	[1, 10]
# [[1, 1], [2, 2], [1, 2]]	[2, 1]
# 입출력 예 설명
# 입출력 예 #1
# 세 점이 [1, 4], [3, 4], [3, 10] 위치에 있을 때, [1, 10]에 점이 위치하면 직사각형이 됩니다.
# 입출력 예 #2
# 세 점이 [1, 1], [2, 2], [1, 2] 위치에 있을 때, [2, 1]에 점이 위치하면 직사각형이 됩니다.

# Let's say the bottom left corner of a rectangle is located at [a,b] and 
# width/height is [w,h]
# Then all coordinates of the rectagular will be
# [a,b]  
# [a+w,b]
# [a,b+h]
# [a+w, b+h]
#
# we can see sum of all x coordinates is 4*a + 2*w 
# and sum of all y coordinates is 4*b + 2*h
#
# Let's say any 3 of these 4 coordinates are given as a list v
# v=[
#     [x1,y1],
#     [x2,y2],
#     [x3,y3],
# ]
# coordinates of the bottom left corner [a,b] = [min(x1,x2,x3), max(y1,y2,y3)]
# width/height of the rectangle is [w,h] = [max(x1,x2,x3)-a, max((y1,y2,y3)-b)]
#
# So, now we know all 4 coordinates of the rectangle. 
# How can I find which one is missing in the given 3 coordinates? 
# Let's say the missing coordinate is [x4,y4]
# x4 = 4*a + 2*w - (x1 + x2 + x3)
# y4 = 4*b + 2*h - (y1 + y2 + y3)
#
#

# +
# Test
import numpy as np
v=np.array([[1, 4], [3, 4], [3, 10]])
print(f'v = {v}')
print(f'v[:,0] = {v[:,0]}')
print(f'v[:,1] = {v[:,1]}')

a = min(v[:,0])
b = min(v[:,1])
w = max(v[:,0]) - a
h = max(v[:,1]) - b

print(f'v.sum(axis=1) = {v.sum(axis=0)}')
print(f'v.sum(axis=0)[0] = {v.sum(axis=0)[0]}')
print(f'v.sum(axis=0)[1] = {v.sum(axis=0)[1]}')

x4 = 4*a + 2*b - v.sum(axis=0)[0]
y4 = 4*b + 2*b - v.sum(axis=0)[1]


# def solution(v):
#     answer = []

#     print('Hello Python')

#     return answer

# -

def solution(v):
    a = min(v[:,0])
    b = min(v[:,1])
    w = max(v[:,0]) - a
    h = max(v[:,1]) - b
    print(f'The coordinate of the bottom left corner of this rectangle is {a},{b}')
    print(f'Width of this rectangle is {w}')
    print(f'Width of this rectangle is {h}')
    x4 = 4*a + 2*b - v.sum(axis=0)[0]
    y4 = 4*b + 2*b - v.sum(axis=0)[1]
    answer = [x4,y4]
    
    return answer


# +
# damn, the input was a list, not a Numpy array
v= [[1, 4], 
    [3, 4], 
    [3, 10]]
type(v)

print(v[0])
print(v[0][0])
print(v[0][1])

# -

# if v is list
def solution(v):
    
    a = min(v[0][0],v[1][0],v[2][0])
    b = min(v[0][1],v[1][1],v[2][1])
    w = max(v[0][0],v[1][0],v[2][0]) - a
    h = max(v[0][1],v[1][1],v[2][1]) - b
    print(f'The coordinate of the bottom left corner of this rectangle is {a},{b}')
    print(f'Width of this rectangle is {w}')
    print(f'Width of this rectangle is {h}')
    x4 = 4*a + 2*w - sum([v[0][0],v[1][0],v[2][0]])
    y4 = 4*b + 2*h - sum([v[0][1],v[1][1],v[2][1]])
    answer = [x4,y4]
    
    return answer


print(solution(v))
