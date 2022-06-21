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
