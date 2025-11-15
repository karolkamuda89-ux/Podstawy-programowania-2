###
# Credit card payment 
#
account_balance = 500
total_payment = (input('Podaj kwote zakupów:'))
total_payment1 = int(total_payment)

if total_payment1 < account_balance:
    print('Payment completed')
else:
    print('No funds')