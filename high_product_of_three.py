# Given a numbers_of_ints, find the highest_product you can get from three of the integers.
# The input numbers_of_ints will always have at least three integers.

# test cases
one = [5, 10, 3, 12]
two = [1, 2, 3, 4, 5]
three = [5, 4, 3, 2, 1]
negatives = [-10, -10, 1, 3, 2]

def highest_product(numbers):
    print("\n===============")
    print("original list: %s" % numbers)

    biggest = numbers[0]
    second_biggest = numbers[1]
    third_biggest = numbers[2]

    biggest_negative = 0
    second_biggest_negative = 0

    if len(numbers) == 3:
        return (numbers[0] * numbers[1] * numbers[2])

    for item in numbers:
        if item < biggest_negative:
            biggest_negative = item
    if biggest_negative != 0:
        numbers.remove(biggest_negative)

    for item in numbers:
        if item < second_biggest_negative:
            second_biggest_negative = item
    if second_biggest_negative != 0:
        numbers.remove(second_biggest_negative)

    for item in numbers:
        if item > biggest:
            biggest = item
    numbers.remove(biggest)

    for item in numbers:
        if item > second_biggest:
            second_biggest = item
    numbers.remove(second_biggest)

    for item in numbers:
        if item > third_biggest:
            third_biggest = item
    numbers.remove(third_biggest)

    # if there are 2 negative numbers
    if biggest_negative != 0 and second_biggest_negative != 0:
        # and biggest_negative > biggest
        # and second_biggest_negative > second_biggest
        if abs(biggest_negative) > biggest and abs(second_biggest_negative) > second_biggest:
            # use the 2 negative numbers
            product = biggest_negative * second_biggest_negative * biggest
    else:
        product = biggest * second_biggest * third_biggest

    print("\nbiggest: %s, second_biggest: %s, third_biggest: %s" % (biggest, second_biggest, third_biggest))
    print("biggest_negative: %s, second_biggest_negative: %s" % (biggest_negative, second_biggest_negative))

    print("\nhighest product is: %d" % product)
    print("===============\n")

    return product

highest_product(one)
# highest_product(two)
# highest_product(three)
highest_product(negatives)
