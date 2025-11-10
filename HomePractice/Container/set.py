s1=set([1,2,3,4,5,6])
print(s1)

s2=set([1,2,2,3,4,5,5,6])
print(s2)

s3={"apple","orange","banana"}
print(s3)
s3.add('pinapple')
print(s3)

s5={1,2,3,4}
s6={3,4,5,6}
print("s5={},s6={}".format(s5,s6))
print(s5|s6)
print(s5.union(s6))

print(s5&s6)
print(s5.intersection(s6))

print(s5-s6)
print(s5.difference(s6))

print(s5<=s6)
print(s5.issubset(s6))
s7={1,2,3}
print('s7={},s5={}'.format(s7,s5))
print('s7 is subset of s5: ',s7<=s5)
print(s7.issubset(s5))
print('s7 is real subset of s5: ',s7<s5)

print('s5 is superset of s7: ',s5>=s7)
print(s5.issuperset(s7))