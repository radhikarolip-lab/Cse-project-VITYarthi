def main():
    print("✅ Program started")   # test line

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        print("You entered choice:", choice)  # test line

        if choice == '6':
            print("Exiting...")
            break
        else:
            print("Looping back to menu...")

if __name__ == "__main__":
  main()
