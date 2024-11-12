print("\nWelcome to the BMI calculator, I need some info about it\n")
name = input(f"What is your name?")


weight = input(f"\nHi {name}, what is your weight in kg please?")
height = input(f"\nwhat is your height in cm please?")


weight = int(weight)
height = int(height)

bmi = weight/height**2 * 10000


if bmi<18.5: 
	message = f"You are under weighted, Eat More!"
elif bmi<25:
	message = f"You are healthy, so keep up with it!"
else:
	message = f"You are over-weighted! So FAT!"

print(f"\nYour bmi is {bmi}.\n{message}\n")




