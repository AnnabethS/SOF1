def mergeLists(list1, list2):
    output = []
    for i in range(len(list1)+len(list2)):
        if len(list1)>0 and len(list2)>0:
            if(list1[0]<list2[0]):
                output.append(list1[0])
                list1.pop(0)
            else:
                output.append(list2[0])
                list2.pop(0)
        elif len(list1)==0:
            for i in range(len(list2)):
                output.append(list2[i])
            break
        elif len(list2)==0:
            for i in range(len(list1)):
                output.append(list1[i])
            break
    print(output)

mergeLists([0, 2, 3, 5, 7], [1, 4, 4, 6, 8])