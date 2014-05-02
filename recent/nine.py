def sort_a_list(myl):
    """
    >>> sort_a_list([])
    []

    >>> sort_a_list([1, 1, 1])
    [1, 1, 1]

    >>> sort_a_list([1, 2, 3])
    [1, 2, 3]

    >>> sort_a_list([3, 1, 2])
    [1, 2, 3]

    """
    if len(myl) > 1:
        middle = len(myl)//2
        left = myl[:middle]
        right = myl[middle:]

        sort_a_list(left)
        sort_a_list(right)
        i = 0        
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if int(left[i]) < int(right[j]):
                myl[k] = left[i]
                i = i + 1
            else:
                myl[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            myl[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            myl[k] = right[j]
            j = j + 1
            k = k + 1
    return myl

def binary_search(my_list, element):
    """
    >>> binary_search([], 1)
    -1

    >>> binary_search([1], 1)
    0

    >>> binary_search([1], 2)
    -1

    >>> binary_search([1,2,3,4], 2)
    1
    """
    left = 0
    right = len(my_list)

    while left < right:
        middle = (left + right) / 2
        if my_list[middle] < element:
            left = middle + 1
        elif my_list[middle] > element: 
            right = middle
        else:
            return middle
    return -1


if __name__ == '__main__':
    print binary_search(sort_a_list([1,53,5,2,6,0,21,54,2]), 5)