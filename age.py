import datetime

current_date = datetime.datetime.now()

def age_calculator():
    while True:
        try:
            user_date = input("Enter your date of birth in the format DD-MM-YYYY ")
            date_test = datetime.datetime.strptime(user_date, "%d-%m-%Y")
            user_day = user_date[:2]
            user_month = user_date[3:5]
            user_year = user_date[6:]
            user_age = current_date.year - int(user_year)
            break
        except:
            print("Please enter a valid date")
    if int(user_month) >= current_date.month:
        if int(user_day) > current_date.day:
            user_age -= 1
    return "You are " + str(user_age) + " years old"

print(age_calculator())

