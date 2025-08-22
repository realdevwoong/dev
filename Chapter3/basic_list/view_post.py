import state

def view_post():
    pid = input("조회할 ID: ").strip()
    if not pid.isdigit():
        print("ID는 숫자입니다.\n")
        return
    pid = int(pid)
    p = next((x for x in state.posts if x["id"] == pid), None)
    if not p:
        print("해당 글이 없습니다.\n")
        return
    print("\n[상세]")
    print(f"ID: {p['id']}")
    print(f"제목: {p['title']}")
    print(f"작성일: {p['created_at']}")
    print("-"*40)
    print(p["content"])
    print()

def main():
    print("view_post.py 직접 실행 테스트")
    state.posts.append({"id": 1, "title": "테스트 글", "content": "내용", "created_at": "2025-08-09 21:00:00"})
    view_post()

if __name__ == "__main__":
    main()


#문자열에 숫자가  있니?
#pid = "123"
#print(pid.isdigit())   # True

#pid = "12a3"
#print(pid.isdigit())   # False

#pid = "１２３"  # 전각 숫자(유니코드)
#print(pid.isdigit())   # True  (전각 숫자도 True)

#next()는 이터레이터/제너레이터에서 다음 값을 꺼내오는 함수
#next((x for x in state.posts if x["id"] == pid), None)
#(x for x in state.posts if x["id"] == pid)

#제네레이터 표현식 
#실행하면 제네레이터 객체를 반환 
#리스트와 달리 값을 하나씩 만듬 
#(())로 만드는 컴프리헨션은 generator 타입
#컴프리헨션(Comprehension)은 파이썬에서 리스트, 딕셔너리, 집합, 제너레이터 등의 자료구조를 간결하게 생성할 수 있는 문법 기능 

#List Comprehension
#nums = [1, 2, 3, 4, 5]
#squares = [x**2 for x in nums]  # 각 원소 제곱
#print(squares)  # [1, 4, 9, 16, 25]

#제러레이터 
#제너레이터는 yield 키워드를 사용한 함수에서 생성
#결과를 하나씩 생성한다
#def my_generator():
#    yield 1
#    yield 2
#    yield 3

#gen = my_generator()
#print(next(gen))  # 1
#print(next(gen))  # 2
#print(next(gen))  # 3

#이터레이터 
#이터러블: for문에서 하나씩 꺼낼 수 있지만, 직접 next()로 꺼낼 수 없음
#이터레이터: 반드시 next() (또는 next()) 메서드가 있음
#nums = [10, 20, 30]          # 리스트는 '이터러블'
#it = iter(nums)              # 이터레이터 객체로 변환

#print(next(it))  # 10
#print(next(it))  # 20
#print(next(it))  # 30


#메모리를 효율적으로 쓸 수 있다.



