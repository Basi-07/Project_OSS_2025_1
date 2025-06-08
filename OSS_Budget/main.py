from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 지출 정산하기")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            try:
                total = int(input("정산할 금액(원): "))
                num_people = int(input("참여 인원 수: "))
            except ValueError:
                print("숫자를 정확히 입력해주세요.\n")
                continue

            if total <= 0 or num_people <= 0:
                print("금액과 인원 수는 1 이상이어야 합니다.\n")
                continue

            share = total / num_people
            print("=== 정산 결과 ===")
            print(f"총 금액: {total}원")
            print(f"인원 수: {num_people}명")
            print(f"1인당 부담 금액: {int(share)}원\n")  # 소수점 없이 정수로 출력

            print("👉 정산된 금액으로 지출 항목을 등록합니다.")
            category = input("카테고리: ")
            description = input("설명: ")
            budget.add_expense(category, description, int(share))

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
