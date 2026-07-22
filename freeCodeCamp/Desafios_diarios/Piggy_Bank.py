'''
Piggy Bank (22/07/2026)

Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".

The object may contain any of the following:

Coin	Value
pennies	$0.01
nickels	$0.05
dimes	$0.10
quarters $0.25

Testes:
Aprovado:1. piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}) should return "$1.98".
Aprovado:2. piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}) should return "$0.41".
Aprovado:3. piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}) should return "$2.25".
Aprovado:4. piggy_bank({}) should return "$0.00".
Aprovado:5. piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}) should return "$6.76".
'''

def piggy_bank(coins):
    total = 0

    for x in coins:
        if x == 'pennies':
            total+= (coins[x]*0.01)
        if x == 'nickels':
            total+= (coins[x]*0.05)
        if x == 'dimes':
            total+= (coins[x]*0.10)
        if x == 'quarters':
            total+= (coins[x]*0.25)
    return f'${total:.2f}'

print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))
print(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}))
print(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}))
print(piggy_bank({}))
print(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}))
