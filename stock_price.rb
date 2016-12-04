profit_six = [10, 7, 5, 8, 11, 9]
negative_profit = [100, 50, 0, -50]
profit_seventy = [99, 119, 50, 120, 20]

def max_profit(yesterday_stock_prices, max_profit = nil)
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

  max_profit(yesterday_stock_prices[1..-1], max_profit)
end

puts "result: #{max_profit(profit_seventy)}, array: #{profit_seventy}"
puts "result: #{max_profit(negative_profit)}, array: #{negative_profit}"
puts "result: #{max_profit(profit_six)}, array: #{profit_six}"
