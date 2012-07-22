#!/usr/bin/env python

price = float(24.95)
wholesaleDiscount = float(0.60)
orderAmount = int(60)
shippingOne = int(3)
shippingAdditional = float(0.75)

print("Total price for %s books is: %s") % (orderAmount, (((price * wholesaleDiscount) + shippingOne) + ((price * wholesaleDiscount) + shippingAdditional) * (orderAmount - 1))) 


