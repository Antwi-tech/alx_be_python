# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority handling
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to address it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task with a deadline. Plan your time accordingly.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule it when convenient.")
    
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but still time-sensitive. Don’t forget it!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid input. Please enter priority as high, medium, or low.")
