# Linear Regression Simple Script.

# Remember that this script must be a Script with a class called Linear Regression. 
# This class must contain all methods and every method must be developed based on every step for the linear regression exercise shown in class. 

# Class named LinearRegression.
class LinearRegression:
    
    # Función init.
    def __init__(self, ntotal):
        self.data_xy = []
        self.ntotal = ntotal

    # First step, asking for the data in a table.
    def step1(self):
        # Part to obtain the values of the table, making a for loop through the (n) value we asked for before.
        for n in range(self.ntotal):    # For to iterate over our ntotal value.
            print("Ingresa los valores de (x) y (y). ")
            x = int(input("Valor de x: "))    # Obtaining the values of (x) and (y).
            y = int(input("Valor de y: "))
            self.data_xy.append([x, y])    # Appending our new values to our table as list to make it a list of lists.
        # Printing the values to check if it's all right.
        print(self.data_xy)

    # Second step (Canonically not), making the summatories of (x) and (y) individually.
    def step2(self):
        # Part of summatory of (x) and (y).
        self.sum_data_x = 0    # Initializing variables of (x) and (y) for the summatories.
        self.sum_data_y = 0
        for n in self.data_xy:    # For loop to iterate over our table of values.
            self.sum_data_x += n[0]    # Adding the values in each iteration.
            self.sum_data_y += n[1]    
        # Printing the values to check if it's all right.
        print(f"The sum of X is: {self.sum_data_x}")
        print(f"The sum of Y is: {self.sum_data_y}")
    
    # Third step making the next column of the table with the multiplication of the column (x) and (y).
    def step3(self):
        self.sum_mul_data_xy = 0    # Variable of the summatory of the multiplications.
        for n in range(self.ntotal):    # For loop to make all the multiplications and additions.
            mul_xy = self.data_xy[n][0] * self.data_xy[n][1]
            self.sum_mul_data_xy += mul_xy
            self.data_xy[n].append(mul_xy)    # Adding multiplicated value to the table.
        # Printing the values to check if it's all right.
        print(f"The new table with the extra column: {self.data_xy}")
        print(f"The sum of the multiplications of X and Y is: {self.sum_mul_data_xy}")

    # Fourth step making the next column withe square of (x) and its summatory.
    def step4(self):
        self.sum_pow_data_x = 0    # Variable of the summatory of the square (x).
        for n in range(self.ntotal):    # For loop again because we're doing the same as before.
            pow_x = self.data_xy[n][0] * self.data_xy[n][0]    # In this case we just want the square of (x).
            self.sum_pow_data_x += pow_x
            self.data_xy[n].append(pow_x)    # Adding squared value to the table.
        # Printing the values to check if it's all right.
        print(f"The new table with the extra column: {self.data_xy}")
        print(f"The sum of the squares of X is: {self.sum_pow_data_x}")

    # Fifth step getting the average values of (x) and (y).
    def step5(self):
        self.avg_x = self.sum_data_x / self.ntotal    # The average value of the (x) and then (y).
        self.avg_y = self.sum_data_y / self.ntotal
        print(f"The average of X is {self.avg_x}")    # Printing the values to check if it's all right.
        print(f"The average of Y is {self.avg_y}")

    # Sixth step getting (m) value.
    def step6(self):
        # Here I'm doing the formula of (m) in two parts, not because I'm pussy, it's beacuse I wanted the code looks good.
        self.m1 = (self.ntotal * self.sum_mul_data_xy) - (self.sum_data_x * self.sum_data_y)
        self.m2 = (self.ntotal * self.sum_pow_data_x) - (self.sum_data_x * self.sum_data_x)
        self.m = self.m1 / self.m2
        print(f"The values of m is: {self.m}")    # Printing the values to check if it's all right.

    # Seventh step doing the formula to get the (b) value.
    def step7(self):
        self.b = self.avg_y - (self.m * self.avg_x)    # Doing the formula.
        print(f"The value of b is: {self.b}")    # Printing the values to check if it's all right.

    # Eighth step getting the value of (y).
    def step8(self):
        self.y = (self.m * self.data_xy[-1][0]) + self.b    # Formula of y.
        print(f"The value of (y) is: {self.y}")    # Printing the values to check if it's all right.

# Instancing an object and using the methods to get the Linear Regression.
print("Define el número total de valores que ingresaras de tu tabla de datos. ")
regresionsita = LinearRegression(int(input("Valor de n: ")))    # Object instance
regresionsita.step1()    # All the steps.
regresionsita.step2()
regresionsita.step3()
regresionsita.step4()
regresionsita.step5()
regresionsita.step6()
regresionsita.step7()
regresionsita.step8()