def main():
    n = int(input())
    students = []
    
    for _ in range(n):
        name, dd, mm, yyyy = input().split()
        dd, mm, yyyy = int(dd), int(mm), int(yyyy)
        students.append((name, yyyy, mm, dd))
    
    # 생일을 기준으로 정렬
    students.sort(key=lambda x: (x[1], x[2], x[3])) # 연도, 월, 일

    print(students[-1][0]) # 가장 나이가 적은 사람
    print(students[0][0])# 가장 나이가 많은 사람

if __name__ == "__main__":
    main()