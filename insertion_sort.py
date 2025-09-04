def sort_descending(array):
    """
    Sorts the list in descending order using insertion sort.
    """
    for current_index in range(1, len(array)):
        current_value = array[current_index]
        position = current_index - 1

        # Shift smaller elements to the right
        while position >= 0 and array[position] < current_value:
            array[position + 1] = array[position]
            position -= 1

        array[position + 1] = current_value
    return array


if __name__ == "__main__":
    data = [9, 3, 5, 2, 8, 1]
    sort_descending(data)
    print("Descending sort:", data)
