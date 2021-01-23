import matplotlib.pyplot as plt
import numpy as np

#описание оси y
plt.ylabel("Amount test cases")

#описание оси x
plt.xlabel("Folders")

#диапазон осей x и y
plt.axis([0, 20, 0, 20])

#столбцы с координатами x и y
plt.bar([2], [10])
plt.bar([2.5], [8])

#подпись к столбцам по x
plt.xticks([2.2], ["folder name"])

#показать форму
plt.show()

#index = ["0"]
#values = [5]
#plt.bar(index,values)
#plt.show()

"""
    cat_par = ["P1"]
    g1 = [10] 
    g2 = [17]
    width = 0.3
    x = np.arange(len(cat_par))
    fig, ax = plt.subplots()
    ax.set_ylim([0,20])
    #rects1 = ax.bar(x - width/2, g1, width, label='g1')
    #rects2 = ax.bar(x + width/2, g2, width, label='g2')
    rects1 = ax.bar(x, g1, width, label='g1')
    rects2 = ax.bar(x-5, g2, width, label='g2')
    ax.set_title('Пример групповой диаграммы')
    ax.set_xticks(x)
    ax.set_xticklabels(cat_par)
    ax.legend()
    plt.show()
"""