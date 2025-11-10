items=['apple','orange','banana']
quantities=[5,3,2]
orders=zip(items,quantities)
print("orders: ",orders)

#print(list(orders))
#print(tuple(orders))
#print(dict(orders))

#print(list(dict(orders).keys()))

dicOrders=dict(orders)
for fruit,quantity in dicOrders.items():
    print(fruit,quantity)