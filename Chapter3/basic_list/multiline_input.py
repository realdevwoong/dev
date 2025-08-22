def multiline_input():
    print("내용 입력 (끝 입력 시 종료)")
    lines = []
    while True:
        line = input()
        if line.strip() == "끝":
            break
        lines.append(line)
    return "\n".join(lines).strip()

def main():
    print("multiline_input.py 직접 실행 테스트")
    content = multiline_input()
    print("저장된 내용:" + content)

if __name__ == "__main__":
    main()

#파이썬 명명 규칙 
#_는 관례상 내부적으로만 쓰라는 개발자들의 암묵적 약속 
#strip 좌우 공백을 뺀 문자 
#append 리스트의 마지막에 새로운 요소를 추가 
#list.append()
#str.join(iterable) #iterable -> 하나씩 차례대로 반복할 수 있는 객체를 의미
#__iter__() 메서드가 있거나, __getitem__() 메서드를 구현하여 인덱싱을 지원하는 객체
#iterable -> list, tuple, str, dict, set ->  for문을 쓸 수 있는 것
"""
fruits = ["apple", "banana", "cherry"]  # 리스트는 iterable
for fruit in fruits:
    print(fruit)
"""