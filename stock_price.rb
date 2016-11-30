p = [10, 7, 5, 8, 11, 9]
poop = [100, 50, 0, -50]
blah = [99, 119, 50, 120, 20]

def max_profit(yesterday_stock_prices, max_profit = 0)
  return max_profit if yesterday_stock_prices.length == 1

  buy_price = yesterday_stock_prices[0]
  unless buy_price == yesterday_stock_prices[-1]
    yesterday_stock_prices[1..-1].each do |sell_price|
      profit = sell_price - buy_price
      max_profit = profit if profit > max_profit

      # puts "\n=============="
      # puts "buy_price: #{buy_price}, sell_price: #{sell_price}"
      # puts "yesterday_stock_prices: #{yesterday_stock_prices}"
      # puts "profit: #{profit}, max_profit: #{max_profit}"
      # puts "==============\n"
    end
  end

  max_profit(yesterday_stock_prices[1..-1], max_profit)
end

puts "result: #{max_profit(blah)}, array: #{blah}"
puts "result: #{max_profit(poop)}, array: #{poop}"
puts "result: #{max_profit(p)}, array: #{p}"
