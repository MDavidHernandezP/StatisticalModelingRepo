import math as m
import scipy.special
from scipy.stats import gamma

#Función para el factorial
def factorial(n):
    if n==0 or n==1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n-1)
    return resultado

#Clase
class DiscreteDistributions:
    euler = m.e

    #Método poisson Distribution
    def poisson(self, averageniu, averagex):
        self.niu = averageniu
        self.x = averagex
        self.negativeniu = (averageniu * -1)

        part1 = (self.euler**self.negativeniu)
        part2 = (self.niu**self.x)
        part3 = (factorial(self.x))
        probability = (part1 * part2)/part3

        print("La probabilidad es de: ", probability)

    #Método Normal (Gaussian) Distribution
    def normal(self, averageniu, averagex, sd):
        self.niu = averageniu
        self.x = averagex
        self.sd = sd

        part1 = (self.x - self.niu)
        z = part1 / self.sd

        print("Z es igual a: ", z)

    #Método Exponential Distribution
    def exponential(self, valorx, ocurrencia):
        self.x = valorx
        self.lambd = ocurrencia

        part1 = (self.lambd * self.x * -1)
        total = 1 - (self.euler ** part1)

        print("La probabilidad de que ocurra un evento en un tiempo", self.x, "es de: ", total)
    
    #Método Beta Distribution
    def beta(self, valorx, valora, valorb):
        self.x = valorx
        self.a = valora
        self.b = valorb

        part1 = self.x ** (self.a - 1)
        part2 = (1 - self.x) ** (self.b - 1)
        part3 = scipy.special.beta(self.a, self.b)

        probabilidad = part1 * part2 / part3

        print("La probabilidad de que suceda", self.x, "es de: ", probabilidad)

    #Método Gamma Distribution
    def gammita(self, valorx, valora, valorb):
        self.x = valorx
        self.a = valora
        self.b = valorb

        probabilidad = gamma.pdf(self.x, a=self.a, scale=1/self.b)

        print("La probabilidad gamma es de: ", probabilidad)

    #Método Logistic Distribution
    def logistic(self, valorx, valorniu, valors):
        self.x = valorx
        self.niu = valorniu
        self.s = valors

        part1 = 1 / (self.s * m.pi)
        part2 = self.euler ** (-1 * (self.x - self.niu) / self.s)
        part3 = (1 + self.euler ** (-1 * (self.x - self.niu) / self.s)) ** 2
        
        total = part1 * (part2 / part3)

        print("La probabilidad es de: ", total)

#Objeto
poisson1 = DiscreteDistributions()

#"Código"
print("Escribe el valor de (niu) y de (x)")
poisson1.poisson(int(input()),int(input()))
