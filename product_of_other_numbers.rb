# test_array = [1, 7, 3, 4]
# length: 4, index: 0 - 3
# num of #'s to multiply: 3
# 1 (index 0): 7*3*4 (index 1 * index 2 * index 3)
# 7 (index 1): 1*3*4 (index 0 * index 2 * index 3)
# 3 (index 2): 1*7*4 (index 0 * index 1 * index 3)
# 4 (index 3): 1*7*3 (index 0 * index 1 * index 2)

# first pass
# 1: 7*3*4
# 7: 3*4
# 3: 4
# 4: 1
#
# second pass
# 1: same
# 7: 1*     (result of first pass)
# 3: 1*7*   (result of first pass)
# 4: 1*7*3* (result of first pass)

def better_product_of_other_numbers(numbers_array)
  array_length = numbers_array.length
  result = []

  numbers_array.each_with_index do |number, index|
    result << multiply_factorial(array_length, numbers_array, index)

    puts "\n==========="
    puts "index: #{index}" 
    puts "array_length: #{array_length}"
    puts "number: #{number}"
    puts "numbers_array: #{numbers_array}\n"

    puts "resulting array: #{result}"
    puts "===========\n"
  end

  result.each_with_index do |number, index|
    new_number = multiply_reverse_factorial(array_length, numbers_array, index)
    result[index] *= new_number

    puts "\n==========="
    puts "INSIDE RESULT LOOP"
    puts "index: #{index}" 
    puts "array_length: #{array_length}"
    puts "new_number: #{new_number}"
    puts "numbers_array: #{numbers_array}\n"

    puts "resulting array: #{result}"
    puts "===========\n"
  end

  numbers_array
end

def multiply_reverse_factorial(array_length, numbers_array, index)
  incrementer = index - 1
  new_number = 1

  while incrementer > array_length do
    new_number *= numbers_array[incrementer]
    incrementer -= 1
  end

  new_number
end

def multiply_factorial(array_length, numbers_array, index)
  incrementer = index + 1
  new_number = 1

  while incrementer < array_length do
    new_number *= numbers_array[incrementer]
    incrementer += 1
  end

  new_number
end

def print_debugging_message
  
end

# ASSETS
# => use the index of the number you want to exclude
#
# REDUNDANCIES
# => multiplying the same two numbers several times
# => looping through the array several times, multiplying the same numbers

# run your function through some test cases here
# remember: debugging is half the battle!
test_array = [1, 7, 3, 4]
better_product_of_other_numbers(test_array)
# puts "#{better_product_of_other_numbers(test_array)}"

# your function would return:
# [84, 12, 28, 21]
# by calculating:
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]
