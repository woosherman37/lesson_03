#small to calculate the BMI based on the user input


print("Welcome to the BMI Calculator! I need some info from you.")

name = input(f"What is your name?")
weight = input(f"Hi {name}, what is you weight?")
height = input(f"What is your height?")


weight = int(weight)
height = int(height)


BMI = round(weight/height**2*10000, 2)



if BMI < 18: 
	msg = "You are under-weighted! EAT MORE!"

elif BMI < 25:
	msg = "You are healthy, so keep up!"

else:
	msg = "You are a FAT ASS!"


print(f"Hey {name}, your BMI is {BMI}. {msg}")





