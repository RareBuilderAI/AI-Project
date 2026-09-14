print("🏗️ Data Forge")
print("Data Forge is ready.")


def process_data(name, numbers):
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    sorted_numbers = sorted(numbers)

    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (
            sorted_numbers[middle - 1] + sorted_numbers[middle]
        ) / 2

    print(f"\n📊 {name} Results")
    print("---------------------")
    print(f"Count: {len(numbers)}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Median: {median}")
    print(f"Sorted data: {sorted_numbers}")


def analyze_data():
    print("\nEnter the name of your data group.")

    group_name = input("Group name: ")

    print("\nEnter numbers separated by spaces.")

    user_input = input("Numbers: ")

    numbers = []

    for value in user_input.split():
        try:
            number = float(value)
            numbers.append(number)

        except ValueError:
            print(f"Skipped invalid value: {value}")

    if numbers:
        process_data(group_name, numbers)

    else:
        print("\nNo valid numbers were entered.")


def menu():
    while True:
        print("\n" + "=" * 30)
        print("🏗️ DATA FORGE")
        print("=" * 30)

        print("1. Analyze data")
        print("2. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            analyze_data()

        elif choice == "2":
            print("\nData Forge shutting down. 👋")
            break

        else:
            print("\nInvalid option. Choose 1 or 2.")


menu()
