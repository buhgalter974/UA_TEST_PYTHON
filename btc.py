BTC_price = int(input("What is Bitcoin price today?\n"))
USD_have = int(input("How much $ do you have?\n"))
BTC_sum = USD_have / BTC_price
print("You can buy %.7f BTC" % BTC_sum)
input()
