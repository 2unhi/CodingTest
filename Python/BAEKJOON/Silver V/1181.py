import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    
    words = set(data[1:]) # 중복 제거
    sorted_words = sorted(words, key=lambda x: (len(x), x)) # 기준: (단어의 길이, 단어)

    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
