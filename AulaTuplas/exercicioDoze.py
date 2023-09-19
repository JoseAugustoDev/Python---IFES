import operator

datas = ((9, 2, 2023), (10, 2, 2024), (22, 11, 2020), (6, 3, 2005))

ordenado = sorted(datas, key= operator.itemgetter(2, 1, 0))

print(ordenado)

# if datas[0][2] > datas[1][2]:
#     print(f"{datas[0]} é mais novo que {datas[1]}.")

# elif datas[1][2] > datas[0][2]:
#     print(f"{datas[1]} é mais novo que {datas[0]}.")

# elif datas[1][2] == datas[0][2]:
#     if datas[1][1] > datas[0][1]:
#         print(f"{datas[1]} é mais novo que {datas[0]}.")

#     elif datas[0][1] > datas[1][1]:
#         print(f"{datas[0]} é mais novo que {datas[1]}.")

#     elif datas[0][1] == datas[1][1]:
#         if datas[1][0] > datas[0][0]:
#             print(f"{datas[0]} é mais novo que {datas[1]}.")

#         elif datas[0][0] > datas[1][0]:
#             print(f"{datas[1]} é mais novo que {datas[0]}.")

#         elif datas[0][0] == datas[1][0] and datas[0][1] == datas[1][1] and datas[0][2] == datas[1][2]:
#             print("Mesmo Dia")