# Analyserer en million desimaler av pi og en milion tilfeldige tall
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Returnerer antall forekomster av tall i en array
def ant(hpi):
    return np.bincount(hpi)

# Lager histogram
def histogram(hpi, x):
    a, b, c = 0, 0, 0
    if x == 4:
        c = 'en million tilfeldige tall(0-9)'
        a = 101000
        b = 98000
    elif x == 3:
        c = 'en million desimaler av pi'
        a = 101000
        b = 98000

    plt.hist(hpi, 20, facecolor="green", alpha=0.75)
    plt.xlabel('Tall')
    plt.ylabel('Antall forekomster')
    plt.title("Antall forekomster av 0-9 i "+c)
    plt.axis([0, 9, b, a])
    plt.grid(1)
    plt.show()

# Printer ut array med indeks
def printarr(arr):
    for i, val in enumerate(arr):
        print("%g: %g" % (i, val))

# Returnerer array med integraler fra fil
def lesfrafil(txt):
    return np.loadtxt(txt, int)

# Skriver ut gjennomsnitt forekomster og median på forekomster
def printinfo(arr):
    printarr(arr)
    print("Gjennomsnittlig ant per tall: %g" % (np.average(arr)))
    print("Median tall: %g" % (np.median(arr)))
    print("Varians: %g" % (np.var(arr)))
    print("Standard avik: %g" % (np.std(arr)))
    x = stats.normaltest(arr)
    print("Score skewtest: %g  Score kurtosistest: %g" % (x[0], x[1]))

# Leser inn arrays
millpi = (lesfrafil("enmillpi.txt"))
tilfeldig = np.random.randint(0, 10, 1000000)
histogram(millpi, 3)
histogram(tilfeldig, 4)

# 1.000.000 desimaler
print("Antall av hvert tall i en million desimaler av pi: ")
printinfo(ant(millpi))

# 1.000.000 tilfeldige tall
print("Antall av hvert tall av en million tilfeldige tall: ")
printinfo(ant(tilfeldig))
