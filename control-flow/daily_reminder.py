task = input("enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("is it time-bound? (yes/no) ")

match priority:
    case "high":
        reminder = f"task: '{task}' is high priority!"
    case "medium":
        reminder = f"task: '{task}' is medium priority!"
    case "low":
        reminder = f"task: '{task}' is low priority!"
    case _:
        reminder = f"task: '{task}' has no priority!"

if time_bound == "yes":
    reminder = reminder + "this is a time-bound task that requires immediate attention today."
else:
    reminder = reminder + "this task is not time-bound that doesn't require immediate attention."

print(reminder)