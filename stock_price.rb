def max_profit(stock_prices)
  min_price = stock_prices[0]
  max_profit = stock_prices[1] - min_price
  num_prices = stock_prices.length

  stock_prices.each_with_index do |price, index|
    price_one = stock_prices[index]
    price_two = nil

    if index == (num_prices - 1)
      puts "\n==============="
      puts "price: #{price}, index: #{index}, num_prices: #{num_prices}"
      puts "price_one: #{price_one}, price_two: #{price_two}"
      puts "min_price: #{min_price}"
      puts "===============\n"
      return max_profit
    end

    price_two = stock_prices[index + 1] unless index == (num_prices - 1)
    min_price = [price_one, min_price].min

    max_profit = [max_profit, price - min_price].max
  end

  highest_profit
end

def generate_random_list_of_numbers(min, max, length)
  length.times.map{ min + Random.rand(max - min) }
end


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
lots_oh_prices = generate_random_list_of_numbers(1, 65, 100)
going_down = [100, 90, 84, 83, 82]

puts "lots_oh_prices: #{lots_oh_prices}"
puts "\nmax profit: #{max_profit(lots_oh_prices)}"

