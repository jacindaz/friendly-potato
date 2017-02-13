# Find the 5th largest element in an array of unsorted integers

test_array = [10, 2, 7, 99, 56, 55, -3, 57, 20, 100, 0, -100]

# try TDD

# PSUEDOCODE
# array is unsorted
# brute force solution
# max1, max2, max3, max4, max5
# would be O(n) because can keep track of max1, 2, 3, 4, 5

def find_fifth_largest_value(my_array)
  max1 = my_array.max

  my_array.delete(max1)
  max2 = my_array.max

  my_array.delete(max2)
  max3 = my_array.max

  my_array.delete(max3)
  max4 = my_array.max

  my_array.delete(max4)
  max5 = my_array.max

  puts "5th largest value is #{max5}"
  puts "max4: #{max4}, max3: #{max3}, max2: #{max2}, max1: #{max1}"

  max5
end

find_fifth_largest_value(test_array)

# describe "find the 5th largest element in an array of unsorted integers" do
#   it "should keep track of the largest integer" do
#   end

#   it "should correctly handle negative numbers" do
#   end
# end
