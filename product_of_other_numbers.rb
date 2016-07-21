def product_of_other_numbers(numbers)
  array_length = numbers.length
  result = []

  numbers.each_with_index do |number, index|
    new_product = numbers.reduce do |product, n|
      if n == number || n == 0
        product * 1
      else
        product * n
      end
    end

    result << new_product
  end

  # test_array = [1, 7, 3, 4]
  # length: 4, index: 0 - 3
  # num of #'s to multiply: 3
  # 1 (index 0): 7*3*4 (index 1 * index 2 * index 3)
  # 7 (index 1): 1*3*4 (index 0 * index 2 * index 3)
  # 3 (index 2): 1*7*4 (index 0 * index 1 * index 3)
  # 4 (index 3): 1*7*3 (index 0 * index 1 * index 2)
  result
end

# ASSETS
# => use the index of the number you want to exclude
#
# REDUNDANCIES
# => multiplying the same two numbers several times
# => looping through the array several times, multiplying the same numbers

# run your function through some test cases here
# remember: debugging is half the battle!
test_array = [1, 7, 3, 4, 0]
puts "#{product_of_other_numbers(test_array)}"

# your function would return:
# [84, 12, 28, 21]
# by calculating:
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]
