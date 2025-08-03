##글등록/출력(appendx)
notes = [None] * 100  # 최대 100개 저장
count = 0  # 현재 저장된 메모 수

while True:
    print("1. 메모 작성")
    print("2. 메모 보기")
    print("3. 종료")

    choice = input("번호 선택: ")

    if choice == "1":
        if count < 100:
            note = input("메모를 입력하세요: ")
            notes[count] = note  # append 없이 직접 저장
            count += 1
        else:
            print("더 이상 저장할 수 없습니다.")

    elif choice == "2":
        for i in range(count):
            print(f"{i+1}. {notes[i]}")

    elif choice == "3":
        print("종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")