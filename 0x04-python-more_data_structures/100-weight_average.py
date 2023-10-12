#!/usr/bin/python3
def weight_average(my_list=[]):
    nom = 0
    denom = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        nom += i[0] * i[1]
        denom += i[1]
    return (nom/denom)
