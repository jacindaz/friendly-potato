# Given a numbers_of_ints, find the highest_product you can get from three of the integers.
# The input numbers_of_ints will always have at least three integers.

# test cases
one = [5, 10, 3, 12, 5]
two = [1, 2, 3, 4, 5]
three = [5, 4, 3, 2, 1]
negatives = [-10, -10, 1, 3, 2]
more_negs = [-10, -8, 9, 2, 10]

def new_high_product(numbers):
    biggest = None
    second_biggest = None

    biggest_negative = None
    second_biggest_negative = None

    high_product_so_far = 1

    for number in numbers:

        if biggest == None and number > 0:
            biggest = number
        elif number >= biggest and number > 0:
            second_biggest = biggest
            biggest = number
        elif number < biggest and number > 0 and (second_biggest == None or number > second_biggest):
            second_biggest = number

        if biggest_negative == None and number < 0:
            biggest_negative = number
        elif number < 0 and number <= biggest_negative:
            second_biggest_negative = biggest_negative
            biggest_negative = number
        elif number < 0 and number > biggest_negative and second_biggest_negative == None:
            second_biggest_negative = number
        elif number < 0 and number > biggest_negative and number < second_biggest_negative: # number -7, second_big_neg -8. number > second_big_neg
            second_biggest_negative = number

        # print("\ncurrent number: %s" % number)
        # print("biggest: %s, second_biggest: %s" % (biggest, second_biggest))
        # print("biggest_negative: %s, second_biggest_negative: %s" % (biggest_negative, second_biggest_negative))

    # positives_product = biggest * second_biggest
    # negatives_product = biggest_negative * second_biggest_negative
    # if positives_product > negatives_product:
    #     high_product_so_far = positives_product
    # elif negatives_product > positives_product:
    #     high_product_so_far = negatives_product


    print("\noriginal array: %s" % numbers)
    print("biggest: %s, second_biggest: %s" % (biggest, second_biggest))
    print("biggest_negative: %s, second_biggest_negative: %s" % (biggest_negative, second_biggest_negative))

# doesn't work
new_high_product(three)
new_high_product(negatives)
new_high_product(more_negs)

# works
# new_high_product(one)
# new_high_product(two)



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

# highest_product(one)
# highest_product(two)
# highest_product(three)
# highest_product(negatives)
