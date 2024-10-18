def solution(my_string):
    return sorted([int(num) for num in str(my_string) if num.isdigit()])