import math

Pi = math.pi
X0 = 0
X1 = 1
X2 = -1

F_of_X0 = (1 / (math.sqrt(2 * Pi))) *  math.exp((-1 / 2) * (X0**2))
F_of_X1 = (1 / (math.sqrt(2 * Pi))) *  math.exp((-1 / 2) * (X1**2))
F_of_X2 = (1 / (math.sqrt(2 * Pi))) *  math.exp((-1 / 2) * (X2**2))

print('The value of the pdf at x = 0.0 is', F_of_X0)
print('The value of the pdf at x = 1.0 is', F_of_X1)
print('The value of the pdf at x = -1.0 is', F_of_X2)

