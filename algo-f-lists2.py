product_cut_prices = [0.50,  10.00,  1.50,  5.50,  2.50, ]

#algorithm: filter + mapping
discount = 0.9
for i in range(len(product_cut_prices)):
    if product_cut_prices[i]> 5.00:
        product_cut_prices[i] = product_cut_prices[i] * discount

# algorithm: print + inter + index
for i in range(len(product_cut_prices)):
    print(i, ")", product_cut_prices[i])



 