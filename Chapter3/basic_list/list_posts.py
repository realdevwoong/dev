import state

def list_posts():
    if not state.posts:
        print("\n[목록] 글이 없습니다.\n")
        return
    print("\n[목록]")
    for p in sorted(state.posts, key=lambda x: x["id"]):
        print(f"- {p['id']:>3} | {p['title']} | {p['created_at']}")
    print()

def main():
    print("list_posts.py 직접 실행 테스트")
    state.posts.append({"id": 1, "title": "테스트 글", "content": "내용", "created_at": "2025-08-09 21:00:00"})
    state.posts.append({"id": 2, "title": "테스트 글", "content": "내용", "created_at": "2025-08-10 21:00:00"})
    list_posts()

if __name__ == "__main__":
    main()

#lambda
#이름이 없는 간단한 함수
#lambda 매개변수:표현식 
# def f(x):
#    return x + 10

#print(f(5))  # 15

#f = lambda x: x+10
#print(f(5)) # 15

#간결성
#익명성
#메모리 절약
#sorted(), map(), filter() 등 내장 함수의 인자로 간단한 처리 함수를 넘겨주기 편리
#sorted()
#numbers = [1, 2, 3, 4]
#print(sorted(numbers))          # [1, 2, 3, 4]  (기본 오름차순 정렬)
#print(sorted(numbers, reverse=True))  # [4, 3, 2, 1]  (내림차순 정렬)