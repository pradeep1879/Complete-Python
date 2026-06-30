import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [15, 20, 10, 45, 30]
# print(x)
# plt.plot(x, y)
# plt.show()

## plt.plot(x, y color='color name', linestyle='', linewidth='', marker='marker symbol', label='label name')

months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1800]
plt.plot(months, sales, color='red', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
plt.title('Monthly sales data record')
plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.legend(loc='upper left')
plt.show()