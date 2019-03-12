import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
#pradiniai duomenis namo dydis namo kaina
house_price = [245, 400, 355, 220, 354, 300]
size = [1400, 1800, 1700, 1300, 1650, 1550]
size2 = np.array(size).reshape((-1,1))
print(size2)


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)



#naudojama linijine regresija
regr = linear_model.LinearRegression()
regr.fit(size2, house_price)
#regresijos atsakymai
print('Coefficients:\n', regr.coef_)
print('intercept:\n', regr.intercept_)


#grafikas
graph('regr.coef_*x + regr.intercept_', range(1000, 2250))
plt.scatter(size, house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
plt.show()
