import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()									# Aktiviert Seaborn

plt.axis([0, 50, 0, 50])					# Skaliert Achsen (0 bis 50)
plt.xticks(fontsize=15)						# Legt Teilstriche der x-Achse fest
plt.yticks(fontsize=15)						# Legt Teilstriche der y-Achse fest
plt.xlabel("Reservations", fontsize=30)		# Legt Beschriftung der x-Achse fest
plt.ylabel("Pizzas", fontsize=30)			# Legt Beschriftung der y-Achse fest

X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True) # L�dt Daten

plt.plot(X, Y, "r+")						# Stellt Daten im Diagramm dar
plt.show()									# Zeigt das Diagramm an