## 삭제 추가(popx)
notes = [None] * 100
count = 0

while True:
    print("1. 작성")
    print("2. 보기")
    print("3. 삭제")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        if count < 100:
            note = input("메모 입력: ")
            notes[count] = note
            count += 1
        else:
            print("공간 부족")

    elif choice == "2":
        for i in range(count):
            if notes[i] is not None:
                print(f"{i+1}. {notes[i]}")

    elif choice == "3":
        num = int(input("삭제할 번호: ")) - 1
        if 0 <= num < count:
            notes[num] = None  # 그냥 None으로 비우기
        else:
            print("존재하지 않음")

    elif choice == "4":
        break