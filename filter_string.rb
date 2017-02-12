def remove_dupes(filter, original_string)
  filter = filter.split("").uniq.join("")

  orig_string_hashed = {}
  original_string.split("").each do |orig_str_char|
    if orig_string_hashed[orig_str_char]
      orig_string_hashed[orig_str_char] += 1
    else
      orig_string_hashed[orig_str_char] = 1
    end
  end

  filter.split("").each do |char|
    orig_string_hashed.delete_if{ |orig_str_char_key, value| char == orig_str_char_key }
  end

  rebuild_string = ""
  orig_string_hashed.each do |key, value|
    value.times{ |i| rebuild_string << key }
  end

  puts rebuild_string
  rebuild_string
end

remove_dupes("chat", "character")

# test cases
# WORST CASE: original_string and filter both contain every single character in the English language, and contain many duplicates of the same character
# original_string => character
# filter => chat
# de-dupe the characters in the filter

# change original_string to hash with counts of each character
# change filter to hash with counts of each character




# can use rspec
# require 'rspec/autorun'
# class Dog
#   def talk!
#     'BARK'
#   end
# end

# RSpec.describe Dog do
#   it 'barks when spoken to' do
#     expect(Dog.new.talk!).to eq('BARK')
#   end
# end
