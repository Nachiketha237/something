import math

def normal_prob(mu, sigma, x):
    return float(1/math.sqrt(2*math.pi*math.pow(sigma, 2)) * math.exp(-math.pow(x-mu, 2) / (2 * math.pow(sigma, 2))))

#mu = 0    mean
#sigma = 1   standard deviation
#x = 1      the value to consider

mu=input("Enter value of mean:")
sigma=input("Enter value of standard diviation:")
x=input("Enter value of x:")
mu=float(mu)
sigma=float(sigma)
x=float(x)
result = normal_prob(mu, sigma, x)

print("The probability of x =", x, "with mean =", mu,
      "and standard deviation =", sigma, "is", result)