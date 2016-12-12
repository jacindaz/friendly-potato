# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

# test cases
one = [5, 10, 3, 12]
two = [1, 2, 3, 4, 5]
three = [5, 4, 3, 2, 1]
negatives = [5, 4, -3, 2, 1, 100]

def highest_product(list):
    biggest = list[0]
    second_biggest = list[1]
    third_biggest = list[2]

    if len(list) == 3:
        return (list[0] * list[1] * list[2])

    for item in list:
        if item > biggest:
            biggest = item
    list.remove(biggest)

    for item in list:
        if item > second_biggest:
            second_biggest = item
    list.remove(second_biggest)

    for item in list:
        if item > third_biggest:
            third_biggest = item
    list.remove(third_biggest)

    product = biggest * second_biggest * third_biggest

    print("\nbiggest: %s, second_biggest: %s, third_biggest: %s" % (biggest, second_biggest, third_biggest))
    print("highest product is: %d" % product)
    return product

highest_product(one)
highest_product(two)
highest_product(three)
highest_product(negatives)
