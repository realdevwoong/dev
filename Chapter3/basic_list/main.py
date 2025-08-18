from menu import menu
from list_posts import list_posts
from view_post import view_post
from create_post import create_post
from update_post import update_post
from delete_post import delete_post

def main():
    while True:
        menu()
        choice = input("선택: ").strip()
        if choice == "1": list_posts()
        elif choice == "2": view_post()
        elif choice == "3": create_post()
        elif choice == "4": update_post()
        elif choice == "5": delete_post()
        elif choice == "0":
            print("종료합니다."); break
        else:
            print("메뉴를 다시 선택하세요.\n")

if __name__ == "__main__":
    main()