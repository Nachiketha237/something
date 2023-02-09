import math

def exponential_prob(lam, x):
    return 1 - math.exp(-lam * x)

lam =float(input("Enter value of rate of events:")) # rate of events
x=float(input("Enter the time interval:"))# time interval

result = float(exponential_prob(lam, x))

print("The probability of an event happening in the first",
      x, "seconds with rate", lam, "per second is", result)