import random


def merge_sort(a_list):
    if len(a_list) <= 1:  # Basisfall
        return a_list
    else:
        middle = len(a_list) // 2
        first_halve = a_list[:middle]  # alles was vor der Mitte ist
        second_halve = a_list[middle:]  # alles was hinter der Mitte ist

        first_halve_sorted = merge_sort(first_halve)  # Funktion rekursiv immer wieder aufrufen
        second_halve_sorted = merge_sort(second_halve)

        return merge(first_halve_sorted, second_halve_sorted)  # am Ende einmal die beiden sortierten Hälften übergeben


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    # Stellen werden jeweils verglichen
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Teile zusammenführen
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


example = [random.randint(0, 100) for _ in range(100)]
print(example)
sorted_example = merge_sort(example)
print(sorted_example)
