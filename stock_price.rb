profit_six = [10, 7, 5, 8, 11, 9]
negative_profit = [100, 50, 0, -50]
profit_seventy = [99, 119, 50, 120, 20]

def max_profit_greedy(yesterday_stock_prices)
  max_profit = yesterday_stock_prices[1] - yesterday_stock_prices[0] if max_profit.nil?
  min_buy_price = yesterday_stock_prices[0]

  yesterday_stock_prices[1..-1].each do |current_price|
    profit = current_price - min_buy_price
    max_profit = profit if profit > max_profit
    min_buy_price = current_price if current_price < min_buy_price
  end

  max_profit
end

def max_profit_recursive(yesterday_stock_prices, max_profit = nil)
  max_profit = yesterday_stock_prices[1] - yesterday_stock_prices[0] if max_profit.nil?
  return max_profit if yesterday_stock_prices.length == 1

  buy_price = yesterday_stock_prices[0]
  unless buy_price == yesterday_stock_prices[-1]
    yesterday_stock_prices[1..-1].each do |sell_price|
      profit = sell_price - buy_price

      # puts "\n=============="
      # puts "buy_price: #{buy_price}, sell_price: #{sell_price}"
      # puts "yesterday_stock_prices: #{yesterday_stock_prices}"
      # puts "profit: #{profit}, max_profit: #{max_profit}"
      # puts "\nprofit > max_profit: #{profit > max_profit}"

      max_profit = profit if profit > max_profit

      # puts "new max_profit: #{max_profit}"
      # puts "==============\n"
    end
  end

  max_profit_recursive(yesterday_stock_prices[1..-1], max_profit)
end

# puts "result: #{max_profit_recursive(profit_seventy)}, array: #{profit_seventy}"
# puts "result: #{max_profit_recursive(negative_profit)}, array: #{negative_profit}"
# puts "result: #{max_profit_recursive(profit_six)}, array: #{profit_six}"

puts "result: #{max_profit_greedy(profit_seventy)}, array: #{profit_seventy}"
puts "result: #{max_profit_greedy(negative_profit)}, array: #{negative_profit}"
puts "result: #{max_profit_greedy(profit_six)}, array: #{profit_six}"
