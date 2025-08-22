import state
from multiline_input import multiline_input

def update_post(self):
        pid = input("수정할 ID: ").strip()
        if not pid.isdigit():
            print("ID는 숫자입니다.\n")
            return
        pid = int(pid)
        idx = next((i for i, x in enumerate(self.posts) if x["id"] == pid), -1)
        if idx < 0:
            print("해당 글이 없습니다.\n")
            return
        
        cur = self.posts[idx]
        print(f"\n[수정] 현재 제목: {cur['title']}")
        new_title = input("새 제목(Enter면 유지): ").strip() or cur["title"]
        
        print("- 기존 내용 -")
        print(cur["content"])
        
        # 먼저 내용 수정 여부 확인
        edit_content = input("내용을 수정하시겠습니까? (y/n): ").strip().lower()
        
        if edit_content == 'y':
            print("- 새 내용 입력 (끝 입력 시 종료) -")
            new_content = self._multiline_input()
        else:
            new_content = cur["content"]
        
        cur["title"] = new_title
        cur["content"] = new_content
        print("수정 완료.\n")

def main():
    print("update_post.py 직접 실행 테스트")
    state.posts.append({"id": 1, "title": "원래 제목", "content": "원래 내용", "created_at": "2025-08-09 21:00:00"})
    update_post()
    print("현재 posts:", state.posts)

if __name__ == "__main__":
    main()

#enumerate
#fruits = ["apple", "banana", "pineapple"]

#for idx, fruit in enumerate(fruits):
#    print(idx, fruit)

#0 apple
#1 banana
#2 pineapple
