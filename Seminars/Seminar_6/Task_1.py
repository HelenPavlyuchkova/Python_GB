
# решение задачи из д.з. 3(перемножение первого и последнего эл)
def dlb(lst: list) -> list:
    count_dbl = (len(lst) + 1) // 2
    res_list = [lst[i] * lst[-i - 1] for i in range(count_dbl)]
    return res_list


list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6]]
print(list(map(dlb, list_1)))

# дописать по семинару
def f(a_1, a_2, a_3):
    print(a_1, a_2, a_3)



