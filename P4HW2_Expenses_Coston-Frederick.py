#CTI-110
#P4HW2-Expenses
# Your Name
# Date


#enter an starting amount in account

amount = float(input("Enter starting amount in account: "))
print()
keep_going = "y"

total = 0
count = 0 #initialize count

while keep_going.lower() == "y": #(TEMP CONVERSION)
   count += 1 #count = count + 1
   expense = float(input("Enter expense " + str(count) + ": "))
   total += expense
   
   keep_going = input("Do you want to enter another expense?(y/n) ")

subtracted_amount = amount - total
print("Amount: ", amount)
print("Number: ",count)
print("Subtracted_Amount", subtracted_amount)
