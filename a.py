""" 
Question_1 . Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary and house allowance rent is 20% of basic salary. Wrote program to calculate his gross salary. 


"""



basic_pay = int(input('Enter the salary '))
print('Dearness allowance 40% ', .4 * basic_pay)
print('House allowance %20 ', .2 * basic_pay)
print('His gross salary is ', (1 + .2 + .4) * basic_pay)
