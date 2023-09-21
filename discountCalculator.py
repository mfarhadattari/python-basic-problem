def discountPrice(price, discountRate):
    totalDiscount = price * discountRate / 100
    return totalDiscount

print(discountPrice(1005, 15))