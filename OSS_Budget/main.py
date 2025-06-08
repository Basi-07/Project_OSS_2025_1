from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 태그별 지출 비율 보기")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue

            tag_input = input("태그 입력 (쉼표로 구분, 생략 가능): ")
            tags = [tag.strip() for tag in tag_input.split(",") if tag.strip()] if tag_input else None

            budget.add_expense(category, description, amount, tags)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            tag = input("검색할 태그: ").strip()
            if tag:
                budget.tag_spending_ratio(tag)
            else:
                print("태그를 입력해주세요.\n")

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
