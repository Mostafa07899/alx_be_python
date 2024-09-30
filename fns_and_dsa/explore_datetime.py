from datetime import datetime, timedelta

def display_current_datetime():
    current_date= datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"future date after {days} days: {formatted_future_date}")
    return future_date

def main():
    current_date = display_current_datetime()

    try:
        days = int(input("Enter the number of days to add: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("invalid input. please enter an integer number to proceed.")

if __name__ == "__main__":
    main()
