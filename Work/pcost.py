# pcost.py

# Exercise 1.27

portfolio_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        # DEBUG print('reading: ' , line, end='')
        name, shares, price = line.split(',')
        shares = int(shares)
        price = float(price)
        cost = shares * price
        portfolio_cost += cost
        # DEBUG print(name, shares, price, round(cost, 2), portfolio_cost )

print('Total cost', portfolio_cost)

import gzip

portfolio_cost = 0
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    headers = next(f)
    for line in f:
        # print('reading: ' , line, end='')
        name, shares, price = line.split(',')
        shares = int(shares)
        price = float(price)
        cost = shares * price
        portfolio_cost += cost
        # print(name, shares, price, round(cost, 2), portfolio_cost )
print('Total cost', portfolio_cost)


