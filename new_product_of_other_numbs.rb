length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

# brute force approach
def product_of_other_numbers(numbers)
  products = []
  array_length = numbers.length
  reusable_number_one = numbers[2..(array_length - 1)].reduce(:*)
  reusable_number_two = numbers[0..(array_length - 3)].reduce(:*)

  puts "\n================="
  puts "reusable_number_one: #{reusable_number_one}"
  puts "reusable_number_two: #{reusable_number_two}"
  puts "=================\n"

  numbers.each_with_index do |num, index|

  end
end

product_of_other_numbers(length_four)
product_of_other_numbers(length_five)
product_of_other_numbers(length_six)
