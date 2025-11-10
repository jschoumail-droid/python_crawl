items=['apple','orange','banana']
quantity=[5,3,2]
orders=zip(items,quantity)
print(orders)

#print(list(orders))
#print(tuple(orders))
#print(dict(orders))

#print(list(dict(orders).keys()))

dicOrders=dict(orders)
for tuple in dicOrders.items():
    print(tuple)