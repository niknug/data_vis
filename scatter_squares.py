from shutil import which

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5, c=y_values, cmap=plt.cm.Blues)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares.png', bbox_inches='tight')
