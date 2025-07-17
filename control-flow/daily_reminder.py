task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
    
    case "low":
        if time_bound == "no":
            print(f"{task} is a low priority task. Consider completing it when you have free time.")     
            
    case "medium":
        if time_bound == "yes" or time_bound == "no":
            print(f"Then you need to see if {task} will affect tomorrow's activity")       
    
    case _:
        print("Invalid input")        