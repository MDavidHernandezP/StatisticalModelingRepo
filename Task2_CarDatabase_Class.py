"""
You Just need to read the script with all comments that I already wrote and complete the last method Modify a product. As I described my methods and wrote my documentation you must replicate that one. 

// Please Check the last method called "DeleteCar" because it had an error and I explained that one in the script//
"""

class Car:
    def __init__(self):
        self.cars = [
                    {'name': 'car1', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car2', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car3', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car4', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car5', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car6', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car7', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car8', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car9', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': 'car10', 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'},
                    {'name': '', 'price': '', 'speed': '', 'windows': '', 'doors': ''},
                    {'name': '', 'price': '', 'speed': '', 'windows': '', 'doors': ''},
                    {'name': '', 'price': '', 'speed': '', 'windows': '', 'doors': ''},
                    {'name': '', 'price': '', 'speed': '', 'windows': '', 'doors': ''},
                    {'name': '', 'price': '', 'speed': '', 'windows': '', 'doors': ''}
                ]

    def add(self, name):
        self.cars.append({'name': name, 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'})
        print(f'{name} ha sido agregado.')
    
    def edit(self, name):
        for feature in self.cars:
            if feature['name'] == name:
                for key in feature.keys():
                    new_value = input(f'Escribe el nuevo valor para {key}: ')
                    feature[key] = new_value
                print(f'{name} ha sido editado.')
                break
        else:
            print(f'No se encontró el carro {name}.')

    def remove(self, name):
        for feature in self.cars:
            if feature['name'] == name:
                self.cars.remove(feature)
                print(f'{name} ha sido eliminado.')
                break
        else:
            print(f'No se encontró el carro {name}.')

    def query(self, name):
        for feature in self.cars:
            if feature['name'] == name:
                print(feature)
                break
    
    def display_cars(self):
        print(self.cars)