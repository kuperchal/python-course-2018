import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_excel('kri.xlsx')
x = table.values[:, 0]
y = table.values[:, 1]
y1 = table.values[:, 2]
plt.figure(figsize=(15, 10))
plt.plot(x, y, 'r', x, y1, 'b')
plt.title("спектр")
plt.xlabel("частота")
plt.ylabel("поглощение")
lgnd = plt.legend(['графен', 'графен в жидком стекле'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')
plt.show()