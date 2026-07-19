'''
Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, 
return an array of the order the elevator should visit them to minimize number of floors traveled.

If tied, go up first
Floors with a request must be visited when the elevator first passes them

Testes:
Aguardando:1. elevator_stops(5, [2, 8, 3, 9]) should return [3, 2, 8, 9].
Aguardando:2. elevator_stops(6, [2, 10, 8, 3, 1, 9]) should return [8, 9, 10, 3, 2, 1].
Aguardando:3. elevator_stops(1, [4, 8, 3, 6, 9]) should return [3, 4, 6, 8, 9].
Aguardando:4. elevator_stops(12, [6, 10, 7, 3, 1, 4]) should return [10, 7, 6, 4, 3, 1].
Aguardando:5. elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]) should return [10, 9, 8, 6, 5, 2, 12, 19, 23].
'''

def elevator_stops(current_floor, stops):
    final_list=[]
    andar_mais_prox = stops[0]
    menor_diferenca = abs(current_floor-stops[0])

    for i in range(1, len(stops)):
        diferenca_i = abs(current_floor-stops[i])
        if (diferenca_i <= menor_diferenca):
            menor_diferenca = diferenca_i
            andar_mais_prox = stops[i]
    stops.remove(andar_mais_prox)
    final_list.append(andar_mais_prox)

    while(len(stops)!=0):
        andar_atual = final_list[len(final_list)-1]

        andar_mais_prox = stops[0]
        menor_diferenca = abs(andar_atual-stops[0])
        
        for i in range(1, len(stops)):
            diferenca_i = abs(andar_atual-stops[i])
            if (diferenca_i < menor_diferenca):
                menor_diferenca = diferenca_i
                andar_mais_prox = stops[i]
        
        stops.remove(andar_mais_prox)
        final_list.append(andar_mais_prox)
    return final_list

print(elevator_stops(5, [2, 8, 3, 9]))
print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
print(elevator_stops(1, [4, 8, 3, 6, 9]))
print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))
