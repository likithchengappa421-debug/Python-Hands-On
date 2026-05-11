count = 0
while True:
    user_input = input(f"Enter 'n' for Next, 'r' for Reset, 'q' for Quit: ").strip().lower()

    # These must all align with the line above
    if user_input == 'n':
        count += 1
        print(f"{count}")
    elif user_input == 'r':
        count = 0
        print(f"{count}")
    elif user_input == 'q':
        print(f"Exiting... See you!")
        break
    else:
        print(f"Invalid input")