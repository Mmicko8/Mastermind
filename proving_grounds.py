# ####### Random combinatie:
#
# from random import randint
# ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")
#
#
# def create_combination(nb_elements):
#     """ Return a random combination involving the number of elements."""
#
#     combinatie_welke_kleuren = []
#
#     while nb_elements > 0:
#         a = randint(0,5)
#         combinatie_welke_kleuren.append(a)
#         nb_elements -= 1
#
#
#     combinatie_kleuren = [ALL_COLORS[combinatie_welke_kleuren[0]], ALL_COLORS[combinatie_welke_kleuren[1]],
#                           ALL_COLORS[combinatie_welke_kleuren[2]],ALL_COLORS[combinatie_welke_kleuren[3]]]
#
#     return (combinatie_kleuren)
#
# print(create_combination(4))
#
# combinatie_kleuren = (ALL_COLORS[combinatie_welke_kleuren[0]],ALL_COLORS[combinatie_welke_kleuren[1]],
#                       ALL_COLORS[combinatie_welke_kleuren[2]],ALL_COLORS[combinatie_welke_kleuren[3]])
# print(combinatie_kleuren)
#
# ######################################
#
# nist = ["blue", "yellow", "yellow", "blue"]
#
# print(nist.count('yellow'))

# MAX_NUMBER_OF_MOVES = 10
# for i in range(1, MAX_NUMBER_OF_MOVES + 1):
#     print(i)


# ovals = []

# for i in range(10):
#     for x in range(4):
#         ovals[i].append(10 + 40*x, 10 + 40*i, 40 + 40*x, 40 + 40*i)

# for i in range(10):
#     ovals.insert(0,[])
# for i in range(10):
#     ovals[i].append('abc')
# print (ovals)

# ovals = []
# def cuck ():
#
#     for i in range(10):
#         ovals.insert(0, [])
#
#     for i in range(10):
#
#         for x in range(4):
#             # canvas.create_oval(10 + 40 * x, 10 + 40 * i, 40 + 40 * x, 40 + 40 * i)
#             circle = [10 + 40 * x, 10 + 40 * i, 40 + 40 * x, 40 + 40 * i]
#             ovals[i].append(circle)
#
#     return ovals
#
# print(cuck())

# def is_sublist_of(sublist, given):
#     """ Returns whether the sublist is part of the given combination.
#     The order of the sublist must also correspond to the order of the
#     corresponding part in the given combination."""
#
#     occurences = 0
#
#     for element in given:
#         if [element] == sublist:
#             occurences += 1
#         print(element)
#
#     if occurences > 0:
#         return(True)
#     else:
#         return(False)
#
#
# simple_list = [1, 2, 3, 4]
# for element in simple_list:
#     assert is_sublist_of([element], simple_list)
# assert not is_sublist_of([5], simple_list)

# a = [[1,2,3], [4,5,6],[7,8,9]]
# print(a[0][1])



