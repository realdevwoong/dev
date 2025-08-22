import state

def delete_post():
    pid = input("삭제할 ID: ").strip()
    if not pid.isdigit():
        print("ID는 숫자입니다.\n")
        return
    pid = int(pid)

    before = len(state.posts)
    state.posts = [p for p in state.posts if p["id"] != pid]
    if len(state.posts) == before:
        print("삭제 대상이 없습니다.\n")
        return
    print("삭제 완료.\n")
    
#리스트 컴프리헨션
#[p for p in state.posts if p["id"] != pid]
