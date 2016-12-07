length_three = [7, 3, 4]
length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

# brute force approach
def product_of_other_numbers(numbers):
    products = []
    array_length = len(numbers)
    # reusable_number_one = numbers[2..(array_length - 1)].reduce(:*)
    # reusable_number_two = numbers[0..(array_length - 3)].reduce(:*)

    # print("\n=================")
    # print("reusable_number_one: %s", % reusable_number_one")
    # print("reusable_number_two: %s", % reusable_number_two")
    # print("=================\n")

    products = []

    for current_number in numbers:
        product = 1

        for multiplying_number in numbers:
            if multiplying_number != 0 and current_number != multiplying_number:
                product *= multiplying_number

        products.append(product)

    print("\n==============")
    print("original array: %s" % numbers)
    print("products: %s" % products)
    # print("products: %s, original array: %s" % (products, numbers))
    print("==============")

    return products

product_of_other_numbers(length_three)
product_of_other_numbers(length_four)
product_of_other_numbers(length_five)
product_of_other_numbers(length_six)
