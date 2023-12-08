list1 = ["a", "b", "c"]
def example1(list):
    list.append(list[0])
    list.pop(0)
    return list
print(example1(list1))


cubes = [num**3 for num in range(3, 13)]
print(cubes)
reverse_cube = cubes[::-1]
print(reverse_cube)

list2 = [-1,-2,-3,-4,1,2,3,4,5,6]
def remove_negative(list):
    list3 = [num for num in list if num > 0]
    return list3
print(remove_negative(list2))


list3 = ["asd", "asdasd", "asdasdasd", "asdasdasdasd", "","","","",""]
def remove_empty(list):
    list33 = [string for string in list if string != ""]
    return list33
print(remove_empty(list3))


strange_list = [1, 2, [30, 40, [500, 600, 700], 80], 8] 
strange_list[2][2].append(800)
print(strange_list)




def sum_of_digits(number):
    return sum([int(i) for i in str(number)])

list44 = [5, 12, 20]
def order_by_sum(list):
    list.sort(key=sum_of_digits)
    return list
print(order_by_sum(list44))

list55 = [[1,2],[2],[2,3,4]]
list66 = [[1,2,2,3,4]]
def contains_sublist(lst):
    return any(isinstance(i, list) for i in lst)
def sum_of_length(list):
    if contains_sublist(list) == True:
        new = [sum(len(i) for i in list)]
    return new
print(sum_of_length(list55))
print(sum_of_length(list66))


list_of_single_digits = [3, 5, 7, 9]
list99 = [num for num in range(1, 1001) for i in list_of_single_digits if num % i == 0]
print(list99)
