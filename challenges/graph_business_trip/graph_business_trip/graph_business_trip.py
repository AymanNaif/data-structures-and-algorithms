def graph_business_trip(graph, lst):
    money = 0
    states = False

    for location in range(len(lst)-1):
        neighbors = graph.get_neighbors(lst[location])
        for i in neighbors:
            if lst[location + 1] == i.vertix:
                money += i.weight
                states = True

    if states == False:
        money = 0
        states = False
        return f'{states},${money}'

    return f'{states},${money}'
