def count(lst):

    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[12,23,45,54,65,66,43,14,16,17]

even,odd=count(lst)