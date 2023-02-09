import math

def poisson_prob(lam, k):
    return math.pow(lam, k) * math.exp(-lam) / math.factorial(k)

lam = float(input("Enter the average number of events in an interval:")) # average number of events in an interval
k = int(input("Enter number of events to consider:"))      # number of events to consider

result = poisson_prob(lam, k)

print("The probability of exactly", k, "events in an interval with average", lam, "events is",result)