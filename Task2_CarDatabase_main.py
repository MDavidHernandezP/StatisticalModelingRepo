from Task2_CarDatabase_Class import Car

car_manager = Car()

while True:
    choose = input('Qué quieres hacer? add, edit, remove, query or exit? Escribelo: ')

    if choose == 'add':
        carname = input('Escribe el nombre del carro: ')
        car_manager.add(carname)

    elif choose == 'edit':
        carname = input('Escribe el nombre del carro a editar: ')
        car_manager.edit(carname)

    elif choose == 'remove':
        carname = input('Escribe el nombre del carro a eliminar: ')
        car_manager.remove(carname)

    elif choose == 'query':
        car_manager.query()

    elif choose == 'exit':
        print('Saliendo del programa. Hasta luego.')
        break

    else:
        print('Opción no válida. Intenta de nuevo.')

    # Imprimir la lista de carros después de las operaciones
    car_manager.display_cars()
