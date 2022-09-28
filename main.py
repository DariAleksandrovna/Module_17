list = list(map(int, input('Введите числа через пробел от 1 до 100 в любой последовательности: ').split()))

while True:
    try:
        num = int(input('Введите число: '))
        if not 0 < num < 100:
            raise ValueError("Не верный диапазон. Введите число от 1 до 100.")
        break
    except ValueError as e:
        print(e)

for i in range(len(list)):
    idx_min = i
    for j in range(i, len(list)):
        if list[j] < list[idx_min]:
            idx_min = j
    if i != idx_min:
        list[i], list[idx_min] = list[idx_min], list[i]

print(list)


def binary_search(list, num, left, right):
    if left > right:
        return right
    mid = (left + right) // 2
    if list[mid] == num:
        return mid
    if list[mid] > num:
        return binary_search(list, num, left, mid - 1)
    else:
        return binary_search(list, num, mid + 1, right)


print(binary_search(list, num, 0, len(list)))
