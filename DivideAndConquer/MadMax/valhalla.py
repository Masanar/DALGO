from sys import stdin, stdout


def enough_tank(capacity: float, events: list, consume: list[int]):
    dist = 0
    count = 0
    leak = 0
    current_tank_capacity = capacity
    return_value = True
    for event in events:
        km = event[0] - dist
        dist = event[0]
        consumption = km * (consume[count] / 100 + leak)
        current_tank_capacity -= consumption
        if current_tank_capacity < 0:
            return_value = False
            break
        if event[1] == "Oasis": current_tank_capacity = capacity
        elif event[1] == "Guarida": leak = 0
        elif event[1] == "Disparo": leak += 1
        elif event[1] == "consumo": count += 1

    return return_value


def main():
    line = stdin.readline().strip().split()
    while (line[-1] != '0'):
        events = []
        consume = [int(line[-1])]
        while (line[1] != 'Valhalla'):
            line = stdin.readline().strip().split()
            events.append([int(line[0]), line[1]])
            if (line[1] == 'consumo'):
                consume.append(int(line[-1]))
        # In this case I set maximum_tank_capcity to be 10_000 just
        # because I knew that is the upper bound, in your case you
        # have to simulate the whole travel without taking in to account
        # nor the Guardia nor the Oasis, just the Disparo and Consumo
        # this would give you and upper bound for each case, this can be
        # done in linear time.
        minimum_tank_capacity, maximum_tank_capacity, ans = 0, 10_000, 0
        almost_zero = 10**(-9)
        while (abs(minimum_tank_capacity - maximum_tank_capacity)
               > almost_zero):
            current_tank_capacity = (minimum_tank_capacity +
                                     maximum_tank_capacity) / 2
            if (enough_tank(current_tank_capacity, events, consume)):
                ans = current_tank_capacity
                maximum_tank_capacity = current_tank_capacity
            else:
                minimum_tank_capacity = current_tank_capacity
        print(f"{ans:.3f}")
        line = stdin.readline().strip().split()


if __name__ == '__main__':
    main()
