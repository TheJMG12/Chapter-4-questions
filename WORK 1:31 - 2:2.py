# Q1
'''
rate = 5.0
initial_balance = 10000.0
target = 3 * initial_balance

balance = initial_balance
year = 0

while balance < target:
    year = year + 1
    interest = balance * rate/100
    balance = balance + interest
print("The investment doubled after a year", year, "years.")
'''
#Answer:The investment doubled after a year 23 years.
# Q2
'''
rate = 10.0
initial_balance = 10000.0
target = 3 * initial_balance

balance = initial_balance
year = 0

while balance < target:
    year = year + 1
    interest = balance * rate/100
    balance = balance + interest
print("The investment doubled after a year", year, "years.")
'''
#Answer: The investment doubled after a year 12 years.
#Q3
'''
rate = 5.0
initial_balance = 10000.0
target = 2 * initial_balance

balance = initial_balance
year = 0
while balance < target:
    year = year +1
    interest = balance*rate/100
    balance = balance + interest
    print("The balance is", balance,)
'''
'''
Answer:
The balance is 10500.0
The balance is 11025.0
The balance is 11576.25
The balance is 12155.0625
The balance is 12762.815625
The balance is 13400.95640625
The balance is 14071.0042265625
The balance is 14774.554437890625
The balance is 15513.282159785156
The balance is 16288.946267774414
The balance is 17103.393581163135
The balance is 17958.56326022129
The balance is 18856.491423232354
The balance is 19799.31599439397
The balance is 20789.28179411367
'''
#Q4
rate = 5.0
initial_balance = 10000.0
target = 2 * initial_balance

balance = initial_balance
year = 0
while balance <= target:
    year = year +1
    interest = balance*rate/100
    balance = balance + interest
    print("The balance is", balance,)
#Q5
'''
n = 1

while n < 100 :

    n = 2 * n

    print(n)

#It prints "2 4 8 16 32 64 128"
'''
