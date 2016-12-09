length_three = [7, 3, 4, 0]
length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

test = [1, 2, 6, 5, 9]
la = [3, 1, 2, 5, 6, 4]

def product_of_other_numbers(numbers):
    products_of_all_ints_before_index = [None] * len(numbers)
    product_so_far = 1
    for i in xrange(len(numbers)):
        products_of_all_ints_before_index[i] = product_so_far
        product_so_far *= numbers[i]

        print("product_so_far: %d" % product_so_far)

    print("\nproducts_of_all_ints_before_index: %s" % products_of_all_ints_before_index)

product_of_other_numbers(la)
# product_of_other_numbers(length_three)
# product_of_other_numbers(length_four)
# product_of_other_numbers(length_five)
# product_of_other_numbers(length_six)
