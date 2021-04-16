# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
""""
year = 365
week = 52
months = 12 

NoventaAnos = 90

user = int(age)

yearNov = NoventaAnos * year
weekNov = NoventaAnos * week
monthsNov = NoventaAnos * months

userYear = user * year
userWeek = user * week
userMonths = user * months

resulYear = yearNov - userYear
resulWeek = weekNov - userWeek
resulMonths = monthsNov - userMonths

print(f"You have {resulYear} days, {resulWeek} weeks, and {resulMonths} months left.")
"""

age_int = int(age)

anosRestantes = 90 - age_int

year = round(anosRestantes * 365)
week = round(anosRestantes * 54)
mounth = round(anosRestantes * 12)

print(f"You have {year} days, {week} weeks, and {mounth} months left.")








