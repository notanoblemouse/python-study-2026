import os

def main():
    print("=== 파이썬 한 줄 메모장 ===")
    memo = input("저장할 내용을 입력하세요: ")
    
    # 파일을 열어서(open) 내용을 추가(a: append)합니다.
    # utf-8은 한글이 깨지지 않게 해주는 설정이에요.
    with open("memo.txt", "a", encoding="utf-8") as f:
        f.write(memo + "\n")
    
    print("성공적으로 저장되었습니다!")
    print(f"현재 위치: {os.getcwd()}") # 파일이 어디 저장됐는지 알려줘요.

if __name__ == "__main__":
    main()