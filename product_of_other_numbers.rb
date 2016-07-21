def product_of_other_numbers(numbers)
  array_length = numbers.length
  result = []

  # brute force approach
  numbers.each_with_index do |number, index|
    # index goes from 0 - 3

    # (5..10).inject { |sum, n| sum + n }            #=> 45
    # (5..10).reduce(1, :*)                          #=> 151200
    # (5..10).inject(1) { |product, n| product * n } #=> 151200

    # new_product = numbers.reduce(1) do |multiply, n|
    #   next if n == (index + 1)
    #   multiply * numbers[index + n]
    # end

    # test_array.reduce { |product, n| puts "\nproduct: #{product}, n: #{n}"; n== 7 ? product * 1 : product * n }

    new_product = numbers.reduce do |product, n|
      # puts "\nproduct: #{product}, n: #{n}"
      n == number ? product * 1 : product * n
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
test_array = [1, 7, 3, 4]
puts "#{product_of_other_numbers(test_array)}"

# your function would return:
# [84, 12, 28, 21]
# by calculating:
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]
