def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, num in enumerate(english):
        if num in s:
            s = s.replace(num, str(index))
    return int(s)