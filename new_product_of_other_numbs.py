length_three = [7, 3, 4, 0]
length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

test = [1, 2, 6, 5, 9]
la = [3, 1, 2, 5, 6, 4]
# => expected answer: [240, 720, 360, 144, 120, 180]

def product_of_other_numbers(numbers):
    products_of_all_ints_before_index = [None] * len(numbers)
    product_so_far_before = 1

    for i in xrange(len(numbers)):
        products_of_all_ints_before_index[i] = product_so_far_before
        product_so_far_before *= numbers[i]

    product_so_far_after = 1
    max_index = len(numbers) - 1
    current_index = max_index
    while current_index >= 0:
        current_number_orig_array = numbers[current_index]
        current_number_products = products_of_all_ints_before_index[current_index]

        products_of_all_ints_before_index[current_index] = current_number_products * product_so_far_after
        product_so_far_after *= current_number_orig_array
        current_index -= 1

    print("Original array: %s, Products: %s" % (numbers, products_of_all_ints_before_index))

    return products_of_all_ints_before_index


product_of_other_numbers(la)
product_of_other_numbers(length_three)
product_of_other_numbers(length_four)
product_of_other_numbers(length_five)
product_of_other_numbers(length_six)

# expected answers
# original array: [7, 3, 4], products: [12, 28, 21]
# original array: [1, 7, 3, 4], products: [84, 12, 28, 21]
# original array: [1, 7, 3, 4, 2], products: [168, 24, 56, 42, 84]
# original array: [1, 7, 3, 4, 2, 8], products: [1344, 192, 448, 336, 672, 168]
# original array: [3, 1, 2, 5, 6, 4], products: [240, 720, 360, 144, 120, 180]
