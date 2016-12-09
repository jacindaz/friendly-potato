length_three = [7, 3, 4, 0]
length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

test = [1, 2, 6, 5, 9]

# brute force approach
def product_of_other_numbers(numbers):
    reusable_components = { 1: { 'before': 1, 'after': 1 },
                            2: { 'before': 1, 'after': 1 },
                            6: { 'before': 1, 'after': 1 },
                            5: { 'before': 1, 'after': 1 },
                            9: { 'before': 1, 'after': 1}
                            }

    products = []
    for current_number in numbers:
        # 2*6*5*9
        product = 1

        num_is_before = True
        before_product = 1

        for num in numbers:
            if current_number == num:
                num_is_before = False
                reusable_components[num]['before'] = before_product
                print("current_number: %d" % current_number)
                print("num: %d" % num)
                print("reusable_components: %s" % reusable_components)
                print("\n")
            elif num_is_before:
                before_product *= num

            product *= num

        if current_number == 1:
            reusable_components[current_number]['after']

        products.append(product)

product_of_other_numbers(test)
# product_of_other_numbers(length_three)
# product_of_other_numbers(length_four)
# product_of_other_numbers(length_five)
# product_of_other_numbers(length_six)
