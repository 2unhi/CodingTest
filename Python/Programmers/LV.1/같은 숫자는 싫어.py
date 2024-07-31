def solution(arr):
    num = [arr[0]]
    for i in range(1, len(arr)):
        if (arr[i] != arr[i-1]):
            num.append(arr[i])
    return num