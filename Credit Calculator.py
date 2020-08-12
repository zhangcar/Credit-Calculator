import sys
import math

args = sys.argv

if len(args) != 5:  # Change it to 5 when it is done for just 4 parameters.
    print('Incorrect parameters')
    sys.exit()

Annu = False
Diff = False

principle = 0
interest = 0
month_payment = 0
period = 0

if '--type=annuity' in args:
    Annu = True
    #  print("This is a Annuity payment plan")
elif '--type=diff' in args:
    Diff = True
    #  print("This is a differential payment plan")
else:
    print('Incorrect parameters')
    sys.exit()

#   Check the principle
for i in range(1, len(args)):
    if '--principal=' in args[i]:
        principle = int(args[i].split("=")[1])
    if principle < 0:
        print('Incorrect parameters')
        sys.exit()


#   Check the interests
flag_ = False
for i in range(1, len(args)):
    if '--interest=' in args[i]:
        interest = float(args[i].split("=")[1]) / 1200
        flag_ = True
if not flag_ or interest < 0:
    print('Incorrect parameters')
    sys.exit()

#   Check the monthly payment
for i in range(1, len(args)):
    if '--payment=' in args[i]:
        month_payment = int(args[i].split("=")[1])
        if Diff or month_payment < 0:
            print('Incorrect parameters')
            sys.exit()

#   Check the period
for i in range(1, len(args)):
    if '--periods=' in args[i]:
        period = int(args[i].split("=")[1])
    if period < 0:
        print('Incorrect parameters')
        sys.exit()


#  Calculation for annuity
if Annu:

    #  To calculate the period:
    if principle and interest and month_payment:
        months_ = math.log((month_payment/(month_payment - principle * interest)), (1 + interest))
        months = math.ceil(months_)
        if months > 12:
            if months % 12 == 0:
                print("You need", int(months / 12), "years to repay this credit!")

            else:
                year = math.floor(months / 12)
                month = months - 12 * year
                print('You need', int(year),' years and ', int(month), 'months to repay this credit!')

        else:
            print('you need', math.ceil(months), 'months to repay this credit!')

        print("Overpayment = ", int(math.ceil(months * month_payment - principle)))
        sys.exit()

    # To calculate the annuity month payment:
    if principle and interest and period:
        exp_ = math.pow((1 + interest), period)
        month_payment = math.ceil(principle * (interest * exp_ / (exp_ - 1)))
        print("Your annuity payment =", int(month_payment), "!")
        print("Overpayment = ", math.ceil(period * int(month_payment) - principle))
        sys.exit()

    # To calculate the credit principal:

    if interest and period and month_payment:
        exp_ = math.pow((1 + interest), period)
        principle = month_payment / ((interest * exp_) / (exp_ - 1))
        print("Your credit principal = ", int(principle), "!")
        print("Overpayment = ", math.ceil(period * int(month_payment) - principle))
        sys.exit()


#  Calculation for Differential payment
if Diff:
    month_payment = []
    sum_ = 0
    for i in range(1, period + 1):
        month_pay = principle / period + interest * (principle - (principle * (i - 1)/period))
        month_payment.append(math.ceil(month_pay))
        sum_ += month_payment[i-1]
        print("Month ",i ,": paid out ", int(month_payment[i-1]))
    print("Overpayment = ", int(sum_ - principle))