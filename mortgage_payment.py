# 1) How much would the monthly payment be for a 30 year mortgage (30 * 12 = 360 month term) with a 400,000 dollar principal and a 3% APR (interest rate with fees included)?
# 2) How much is the monthly payment if the interest rate is 6%? (use the same term length and principle)
# Sources: geeksforgeeks.org, pythonguides, mortgagecalculator (to ensure proper answer)
# Desired answers: $1686.42 @ 3% - 2398.20 @ 6%
# Attempt 1: Using formula (P * r * t) / 100

P = 400000 # Principal
r = 0.06 # Rate
t = 30 # Term

mortgage = (P * r * t) / 100
print(mortgage)
# End result $3600/7200 (3%/6%, respectively) - Seems excessive for a monthly payment. Not correct

# Use formula given P * r(1 + r)t / (1 + r)t - 1
# Remember exponents are denoted by **
# Order of operations would complicate answer, would separating numerator & denominator work?
# Attempt 2

P = 400000 # Principal
r = 0.03 / 12 # Rate
t = 360 # Term (Payments)

num = int(0.03 / 12 * (1 + 0.03 / 12)**360)
den = int((1 + 0.03 / 12)**360 - 1)
mortgage = P * (num / den)
print(mortgage)
pass

# This method did not work - Kept running into int 'object' not callable
# Added multiplication in num - answer came out to 0.0...interesting...

# Formula: P * r(1 + r)t / (1 + r)t - 1
# Removed int
# Attempt 3

P = 400000 # Principal
r = 0.03 / 12 # Rate
t = 360 # Term (Payments)

num = (0.03 / 12 (1 + 0.03 / 12)**360)
den = (1 + (0.03 / 12)**360 - 1)
mortgage = P * (num /den)
print(mortgage)
pass

# Ran into 'int' object not callabe again - feel like I'm getting closer

# Formula: P * r(1 + r)t / (1 + r)t - 1
# Attempt 4
# Wait......I think I realized the issue
# Defined all the variables, but needed to USE the variables instead of what defined them

P = 400000 # Principal
r = 0.03 / 12 # Rate
t = 360 # Term (Payments)

num = (r(1 + r)**t)
den = ((1 + r)**t - 1)
mortgage = P * (num / den)
print(mortgage)

# Ran into 'float' ojbect not callable