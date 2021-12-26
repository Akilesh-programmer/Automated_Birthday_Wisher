import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "akileshpython@gmail.com"
PASSWORD = "Thilagu@123"

with open("birthdays.csv") as file:
    data = pandas.read_csv(file)

with open("./letter_templates/letter_1.txt") as letter:
    letter_1 = letter.read()
with open("./letter_templates/letter_2.txt") as letter:
    letter_2 = letter.read()
with open("./letter_templates/letter_3.txt") as letter:
    letter_3 = letter.read()
letters = [letter_1, letter_2, letter_3]

name = data["name"].to_dict()
email = data["email"].to_dict()
year = data["year"].to_dict()
month = data["month"].to_dict()
day = data["day"].to_dict()

data_dict = {}
for n in range(len(name)):
    new_set = {
        "email": email[n],
        "year": year[n],
        "month": month[n],
        "day": day[n],
    }
    data_dict[name[n]] = new_set

date_time = dt.datetime.now()
date = date_time.date()
month = date_time.month
year = date_time.year

for thing in data_dict:
    if data_dict[thing]["month"] == month:
        if f'{year}-{month}-{str(data_dict[thing]["day"])}' == str(date):
            random_letter = random.choice(letters)
            random_letter = random_letter.replace("[NAME]", thing)
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=f'{data_dict[thing]["email"]}',
                                msg=f"Subject:Birthday Wishes\n\n{random_letter}"
                                )
            connection.close()
