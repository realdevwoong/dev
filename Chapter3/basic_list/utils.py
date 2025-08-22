from datetime import datetime

def format_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print("utils.py 직접 실행 테스트")
    print("현재 시간 =", format_now())

if __name__ == "__main__":
    main()

# datetime.now()
# 지금 시각을 datetime 객체로 가져옴
# : datetime.datetime(2025, 8, 9, 21, 35, 50)

# .strftime("%Y-%m-%d %H:%M:%S")
# → 날짜·시간을 원하는 형식의 문자열로 변환

# %Y → 4자리 연도 (예: 2025)

# %m → 2자리 월 (01~12)

# %d → 2자리 일 (01~31)

# %H → 24시간제 시 (00~23)

# %M → 분 (00~59)

# %S → 초 (00~59)