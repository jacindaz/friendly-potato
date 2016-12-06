length_four = [1, 7, 3, 4]
length_five = [1, 7, 3, 4, 2]
length_six = [1, 7, 3, 4, 2, 8]

def product_of_other_numbers(numbers)
  multiply_all_nums = 1

  numbers.each do |num|
    unless num == 0
      multiply_all_nums *= num
    end
  end

  puts "multiply_all_nums: #{multiply_all_nums}"

  numbers.each_with_index do |num, index|
    unless num == 0
      numbers[index] = (multiply_all_nums / num)
    end
  end

  puts "numbers: #{numbers}"
end

product_of_other_numbers(length_four)
product_of_other_numbers(length_five)
product_of_other_numbers(length_six)
