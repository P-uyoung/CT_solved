# DFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

answer = 0
def dfs(idx, numbers, target, value):
    global answer
    if idx == len(numbers):
        if value == target:
            answer += 1
            return
        else:
            return 
        
    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])
        
def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer