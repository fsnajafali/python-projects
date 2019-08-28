from datetime import date

# Input values from user
Year = int(input("What's your year of birth?: "))
Month = int(input("What's your month of birth?: "))
Day = int(input("What's your day of birth?: "))

print("Your Date of Birth is {}/{}/{}".format(Month, Day, Year))

# Retriving today's date
today_day = date.today()
todays_date = today_day.strftime("%m/%d/%Y")
print("Today's date is {}".format(todays_date))

# Age is calculated using Birth Year and Today's date
age = today_day.year - Year
print("You are", age, "years old")

# Figuring out your Zodiac Sign
if ((Month == 12 and Day >= 22) or (Month == 1 and Day <= 19)):
    sign = ("Capricorn")
elif ((Month == 1 and Day >= 20) or (Month == 2 and Day <= 18)):
    sign = ("Aquarius")
elif ((Month == 2 and Day >= 19) or (Month == 3 and Day <= 20)):
    sign = ("Pisces")
elif ((Month == 3 and Day >= 21) or (Month == 4 and Day <= 19)):
    sign = ("Aries")
elif ((Month == 4 and Day >= 20) or (Month == 5 and Day <= 20)):
    sign = ("Taurus")
elif ((Month == 5 and Day >= 21) or (Month == 6 and Day <= 20)):
    sign = ("Gemini")
elif ((Month == 6 and Day >= 21) or (Month == 7 and Day <= 22)):
    sign = ("Cancer")
elif ((Month == 7 and Day >= 23) or (Month == 8 and Day <= 22)):
    sign = ("Leo")
elif ((Month == 8 and Day >= 23) or (Month == 9 and Day <= 22)):
    sign = ("Virgo")
elif ((Month == 9 and Day >= 23) or (Month == 10 and Day <= 22)):
    sign = ("Libra")
elif ((Month == 10 and Day >= 23) or (Month == 11 and Day <= 21)):
    sign = ("Scorpio")
elif ((Month == 11 and Day >= 22) or (Month == 12 and Day <= 21)):
    sign = ("Sagittarius")

print("Your Zodiac Sign is:", sign)
