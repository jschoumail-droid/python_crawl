def formatCustomer(first,last,location=None):
    fullName='%s %s' % (first,last)
    if location:
        return '%s (%s)' % (fullName,location)
    else:
        return fullName

print(formatCustomer('John','Smith',location='California'))
print(formatCustomer('Mareike','schmidt'))