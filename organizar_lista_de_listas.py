list0 = [5, 3, 9, 10, 8, 2, 7]
list1 = [6, 7, 8, 15, 3, 1, 0]
list2 = [12, 23, 59, 110, 28, 12, 7]
lista_anidada = [list0,list1,list2]

def min_list(list):
    if len(list) == 1:
        return list[0]
    elif list[0] >= list[1]:
        return min_list(list[1:])
    return min_list([list[0]] + list[2:])

def min_list2(list):
    if list==[]:
        return []
    return [min_list(list[0])]+min_list2(list[1:])

print min_list(list0)
print min_list2(lista_anidada)

