import numpy as np
from itertools import permutations

le = list(range(55))
le.append(0)

je = [0] + list(list(permutations(le[1:-1]))[6]) + [0]


# N = 8
# tarj = je[1:je.index(N)-1] + je[je.index(N)+2:-1]
# print(tarj)


def perm_generator(lst):
    if len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in perm_generator(lst[:i] + lst[i+1:]):
                yield [lst[i]] + perm


my_generator = perm_generator(le)
print(list(my_generator)[3])







# for i in trajet :
#                 for j in trajet[1:trajet.index(i)-1] + trajet[trajet.index(i)+2:-1] :