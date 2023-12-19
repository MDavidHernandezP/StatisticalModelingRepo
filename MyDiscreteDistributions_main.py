from DiscreteDistributions import DiscreteDistributions

distributions = DiscreteDistributions()

#Método Normal (Gaussian) Distribution
print("Escribe el valor de (niu), de (x) y de la desviación estándar (sd)")
distributions.normal(int(input()),int(input()),int(input()))

#Método Exponential Distribution
print("Escribe el valor de (x) y de la ocurrencia o lambda")
distributions.exponential(int(input()),int(input()))

#Método Beta Distribution
print("Escribe el valor de (x), de (a) y de (b)")
distributions.beta(int(input()),int(input()),int(input()))

#Método Gamma Distribution
print("Escribe el valor de (x), de (a) y de (b)")
distributions.gammita(int(input()),int(input()),int(input()))

#Método Logistic Distribution
print("Escribe el valor de (x), de (niu) y de (s)")
distributions.logistic(int(input()),int(input()),int(input()))

#Método poisson Distribution
print("Escribe el valor de (niu) y de (x)")
distributions.poisson(int(input()),int(input()))