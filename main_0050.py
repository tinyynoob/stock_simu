import math
from numpy import random as rnd
import matplotlib.pyplot as plt

now = 125.9 # 2023 September 3rd

total_month = 120
mon_grow = 0.65
mon_sigma = 4

result = []
case_num = 16
case_sqrt = int(math.sqrt(case_num))
for iter in range(case_num):
    rate = rnd.normal(mon_grow, mon_sigma, total_month)    # unit: month
    factor = 1 + (rate / 100)
    #print(factor)
    price = [now]
    for i in range(len(factor)):
        price.append(price[i] * factor[i])
    #print(price)
    plt.subplot(case_sqrt, case_sqrt, iter + 1)
    plt.plot(range(len(price)), price)
    result.append(math.trunc(price[-1]))
result.sort()
print(result)
plt.show()

