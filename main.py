#small to calculate the BMI based on the user input

#modules that need installing
import pandas as pd


print("Welcome to the BMI Calculator! I need some info from you.")

table = {"name":["sherman", "tom", "bobo"],
	 "age": [34, 48, 10],
	 "skill":["smile", "eat", "sleep"]	
	}

table_df = pd.DataFrame(table)

print(table_df)
