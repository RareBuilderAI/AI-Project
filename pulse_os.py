import platform
import sys
from datetime import datetime


print("⚡ Pulse OS")
print("Pulse OS is starting...")


def show_status():
    print("\n🟢 System Status")
    print("----------------")
    print("Pulse OS: Online")
    print("System: Ready")
    print("Status: Operational")


def show_time():
    current_time = datetime.now()

    print("\n🕒 Current Time")
    print("----------------")
    print(current_time.strftime("%Y-%m-%d %H:%M:%S"))


def show_system_info():
    print("\n💻 System Information")
    print("---------------------")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Python Version: {sys.version.split()[0]}")


def menu():
    while True:
        print("\n" + "=" * 30)
        print("⚡ PULSE OS")
        print("=" * 30)

        print("1. Check system status")
        print("2. Show current time")
        print("3. Show system information")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_status()

        elif choice == "2":
            show_time()

        elif choice == "3":
            show_system_info()

        elif choice == "4":
            print("\nPulse OS shutting down. 👋")
            break

        else:
            print("\nInvalid option. Choose 1-4.")


menu()
