def add_to_cars(num, cars):
    for i in range(num):
        cars_input = input().split("|")
        car = cars_input[0]
        mileage = int(cars_input[1])
        fuel = int(cars_input[2])

        if car not in cars:
            cars[car] = {'milige': mileage, 'fuel': fuel}

    return cars


def commands_for_cars(cars):
    while True:
        commands = input().split(" : ")
        command = commands[0]
        if command == "Stop":
            break
        elif command == "Drive":
            car = commands[1]
            distance = int(commands[2])
            fuel = int(commands[3])

            if cars[car]['fuel'] > fuel:
                cars[car]['milige'] = cars[car]['milige'] + distance
                cars[car]['fuel'] = cars[car]['fuel'] - fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car]['milige'] >= 100000:
                    del cars[car]
                    print(f"Time to sell the {car}!")
            else:
                print("Not enough fuel to make that ride")

        elif command == "Refuel":
            car = commands[1]
            fuel = int(commands[2])
            fuel_two = fuel + cars[car]['fuel']

            if fuel_two >= 75:
                fuel = 75 - cars[car]['fuel']
                cars[car]['fuel'] += fuel
                print(f"{car} refueled with {fuel} liters")
            else:
                fuel_one = fuel + cars[car]['fuel']
                cars[car]['fuel'] = fuel_one
                print(f"{car} refueled with {fuel} liters")

        elif command == "Revert":
            car = commands[1]
            kilometers = int(commands[2])

            cars[car]['milige'] = cars[car]['milige'] - kilometers
            if cars[car]['milige'] < 10000:
                cars[car]['milige'] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

    return cars


def print_cars(cars):
    for car in cars:
        print(f"{car} -> Mileage: {cars[car]['milige']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")


num = int(input())
cars = {}
add_to_cars(num, cars)
commands_for_cars(cars)
print_cars(cars)
