# 전역 상태 (메모리 저장)
posts = []   # {"id": int, "title": str, "content": str, "created_at": str}
seq = 0      # 자동 증가 ID
def main():
    print("state.py 직접 실행 테스트")
    print("posts =", posts)
    print("seq =", seq)

if __name__ == "__main__":
    main()