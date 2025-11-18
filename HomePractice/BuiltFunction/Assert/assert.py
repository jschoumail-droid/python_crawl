#注意 : assert應視為除錯工具，而不是拿來處理執行階段錯誤。
#assert述句會假定條件總是為真，如果條件為假，它會停止程式執行，發出AssertError訊息

'''x=2
assert x<1,'Invalid value'''

def avg(marks):
    #assert len(marks)!=0
    assert len(marks)!=0, 'empty list'
    return round(sum(marks)/len(marks),2)
seml_marks=[62,65,75]
print("Average marks for semester 1:",avg(seml_marks))

ranks=[]
print("Average marks for semester 1:",avg(ranks))