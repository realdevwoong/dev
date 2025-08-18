posts = [] 
seq = 0 
from utils import format_now
from multiline_input import multiline_input

def create_post():
    global seq
    while True:
        title = input("\n[작성] 제목: ").strip()
        if title:
            break
        print("제목은 비울 수 없습니다.")

    content = multiline_input()
    if not content:
        print("내용은 비울 수 없습니다.\n")
        return

    seq += 1
    posts.append({
        "id": seq,
        "title": title,
        "content": content,
        "created_at": format_now(),
    })
    print("작성 완료.\n")

def main():
    print("create_post.py 직접 실행 테스트")
    create_post()
    print("현재 posts:", posts)

if __name__ == "__main__":
    main()

#코드 흐름 추적 어려움
#함수 안에서 전역 변수가 언제 어떻게 바뀌는지 파악하기 어려움#
#버그 발생 가능성↑
#여러 함수에서 같은 전역 변수를 수정하면 의도치 않은 값이 들어갈 수 있음
#재사용성↓
#함수가 전역 변수에 의존하면 독립적으로 테스트하기 어려움

#state.py 모듈 분리 
#class Board:
#   def __init__(self):
#        self.posts = []
#        self.seq = 0

#    def create_post(self, title, content):
#        self.seq += 1
#        self.posts.append({"id": self.seq, "title": title, "content": content})