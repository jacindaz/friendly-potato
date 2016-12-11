length_three = [7, 3, 4]
length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]
la = [3, 1, 2, 5, 6, 4]

# brute force approach
def product_of_other_numbers(numbers)
  products = []
  array_length = numbers.length
  reusable_number_one = numbers[2..(array_length - 1)].reduce(:*)
  reusable_number_two = numbers[0..(array_length - 3)].reduce(:*)

  # puts "\n================="
  # puts "reusable_number_one: #{reusable_number_one}"
  # puts "reusable_number_two: #{reusable_number_two}"
  # puts "=================\n"

  products = []

  numbers.each do |current_number|
    product = 1
    numbers.each do |multiplying_number|
      unless multiplying_number == 0 || current_number == multiplying_number
        product *= multiplying_number
      end
    end

    products << product
  end

  puts "\n=============="
  puts "original array: #{numbers}"
  puts "products: #{products}"
  puts "==============\n"

  products
end

product_of_other_numbers(length_three)
product_of_other_numbers(length_four)
product_of_other_numbers(length_five)
product_of_other_numbers(length_six)
product_of_other_numbers(la)
