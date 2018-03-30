import sys

# mealCost = 12
# tip_percent = mealCost*20/100
# tax_percent = mealCost*8/100

# totalCost = mealCost + tip_percent + tax_percent
# print(totalCost)

if __name__ == '__main__':
	meal_cost = float(input())
	tip_percent = int(input())
	tax_percent = int(input())

	tip = meal_cost * tip_percent/100
	tax = meal_cost * tax_percent/100

	totalCost = meal_cost + tip + tax

	print('The total meal cost is {} dollars.'.format(round(totalCost)))