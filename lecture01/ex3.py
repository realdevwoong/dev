# 최대 100개의 글을 저장할 수 있는 공간 준비
titles = [""] * 100
contents = [""] * 100
count = 0  # 현재 글 수

while True:
    print("\n=== 나만의 게시판 ===")
    print("1. 작성")
    print("2. 목록")
    print("3. 보기")
    print("4. 수정")
    print("5. 삭제")
    print("6. 종료")

    menu = input("메뉴 번호 선택: ")

    # 글 작성
    if menu == "1":
        if count >= 100:
            print("⚠️ 저장 공간이 부족합니다. (최대 100개)")
        else:
            title = input("제목: ")
            content = input("내용: ")
            titles[count] = title
            contents[count] = content
            count += 1
            print("✅ 글이 저장되었습니다.")

    # 목록 출력
    elif menu == "2":
        print("\n[ 글 목록 ]")
        has_post = False
        for i in range(count):
            if titles[i] != "":
                print(f"{i+1}. {titles[i]}")
                has_post = True
        if not has_post:
            print("※ 등록된 글이 없습니다.")

    # 글 보기
    elif menu == "3":
        idx = int(input("보고 싶은 글 번호: ")) - 1
        if 0 <= idx < count and titles[idx] != "":
            print("\n[ 글 상세 보기 ]")
            print(f"제목: {titles[idx]}")
            print(f"내용: {contents[idx]}")
        else:
            print("❌ 존재하지 않는 글 번호입니다.")

    # 글 수정
    elif menu == "4":
        idx = int(input("수정할 글 번호: ")) - 1
        if 0 <= idx < count and titles[idx] != "":
            new_title = input("새 제목: ")
            new_content = input("새 내용: ")
            titles[idx] = new_title
            contents[idx] = new_content
            print("🔄 글이 수정되었습니다.")
        else:
            print("❌ 수정할 수 없는 번호입니다.")

    # 글 삭제
    elif menu == "5":
        idx = int(input("삭제할 글 번호: ")) - 1
        if 0 <= idx < count and titles[idx] != "":
            titles[idx] = ""
            contents[idx] = ""
            print("🗑️ 글이 삭제되었습니다.")
        else:
            print("❌ 삭제할 수 없는 번호입니다.")

    # 종료
    elif menu == "6":
        print("👋 게시판을 종료합니다.")
        break

    else:
        print("⚠️ 잘못된 입력입니다. 1~6 중 선택하세요.")

        #