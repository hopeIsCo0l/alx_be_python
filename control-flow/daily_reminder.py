def main():
    # Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority level"

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Provide the customized reminder
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
