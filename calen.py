import datetime

def main():
    explore_dt()


def explore_dt():
    today = datetime.date.today()
    print("Today's date:", today)

    # Create a specific date
    specific_date = datetime.date(2025, 12, 31)
    print("Specific date:", specific_date)

    # Calculate the difference between two dates
    delta = specific_date - today
    print("Days until specific date:", delta.days)

    # Get today's weekday
    weekday = today.strftime("%A")
    print("Today is a:", weekday)

if __name__ == "__main__":
    main()  