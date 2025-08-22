import state 
from utils import format_now
from multiline_input import multiline_input

def create_post():
    # 제목 입력 (비울 수 없음)
    while True:
        title = input("\n[작성] 제목: ").strip()
        if title:
            break
        print("제목은 비울 수 없습니다.")
        
    # 내용 입력 (비울 수 없음)
    while True:
        content = multiline_input()
        if content:
            break
        print("내용은 비울 수 없습니다. 다시 입력해주세요.")
    
    state.seq += 1
    state.posts.append({
        "id": state.seq,
        "title": title,
        "content": content,
        "created_at": format_now(),
    })
    print("작성 완료.\n")

def main():
    print("create_post.py 직접 실행 테스트")
    create_post()
    print("현재 posts:", state.posts)

if __name__ == "__main__":
    main()