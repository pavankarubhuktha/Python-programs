#4.​ Create a generator function that flattens nested lists of arbitrary depth.
def flat(nestedlist):
    for item in nestedlist:
        if isinstance(item,list):
            yield from flat(item)
        else:
            yield item
nestedlist = [1,[3,5],2,[7,2,6],3]
for i in flat(nestedlist):
    print(i , end=" ")