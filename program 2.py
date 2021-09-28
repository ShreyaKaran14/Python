#create a python program to input name and age of user and give them the year in which they will turn 100 year of age.
name = input("Enter your name: ") # user input
current_age = int(input("Enter your age: ")) # user input
#calculating the 100th year, considering 2020 as the current year
hundredth_year = 2020 + (100 - current_age)
print(f'{name} will become 100 years old in the year {hundredth_year}.')
