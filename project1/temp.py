import csv

employees = csv.reader(open("employees.csv", "rU"))

for emp in employees:
	print(emp)
