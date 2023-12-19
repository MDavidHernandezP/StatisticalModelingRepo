"""
-We have an exciting task ahead of us: efficient car data management. We have 15 cars, each with five key attributes: Name, Price, Speed, Windows and Doors. 
Our mission is to develop a robust and efficient code that allows:

Add a car to the corresponding list (example: the name is added to 'CarNames').
Edit the data of an existing car.
Remove a car from the list.
Query cars (print data from one position).

Our goal is to make this task an example of excellence in data management. Let's work together to create an elegant and efficient solution that demonstrates our commitment to quality.
"""

# Car list is a list of dictionaries.
cars = [
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


while True:
    # Choosing whatever you want to do with the list.
    choose = input('Qué quieres hacer? add, edit, remove, query o exit (si quieres acabar)? Escribelo: ')

    # Option add.
    if choose == 'add':
        carname = input('Escribe el nombre del carro a agregar: ')
        cars.append({'name': carname, 'price': 'unknown', 'speed': 'unknown', 'windows': 'unknown', 'doors': 'unknown'})

    # Option edit.
    elif choose == 'edit':
        carname = input('Escribe el nombre del carro a editar: ')
        for feature in cars:
            if feature['name'] == carname:
                for key in feature.keys():
                    new_value = input(f'Escribe el nuevo valor para {key}: ')
                    feature[key] = new_value
                print(f'{carname} ha sido editado.')
                break
            else:
                print(f'No se encontró el carro {carname}.')

    # Option remove.
    elif choose == 'remove':
        carname = input('Escribe el nombre del carro a eliminar: ')
        for feature in cars:
            if feature['name'] == carname:
                cars.remove(feature)
                print(f'{carname} ha sido eliminado.')
                break
            else:
                print(f'No se encontró el carro {carname}.')

    # Option query. 
    elif choose == 'query':
        carname = input('Escribe el nombre del carro que quieras consultar: ')
        for feature in cars:
            if feature['name'] == carname:
                print(feature)
                break
    
    # Option exit.
    elif choose == 'exit':
        print('Saliendo del programa. Hasta luego.')
        break

    # No existing option. 
    else:
        print('Opción no válida. Intenta de nuevo.')

print(cars)