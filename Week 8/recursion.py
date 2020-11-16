import math

def is_power(a,b):
    if a==1 & b!=0:
        return True #anything ^0 is 1

    if a==b:
        return True

    if b==1:
        return False

    if b==0 & a>0:
        return True
    elif b==0:
        return False

    if a%b!=0:
        return False
    else:
        return is_power(a//b, b)

def rec_sum(user_list):
    if len(user_list)==0:
        return 0
    elif len(user_list)==1:
        return user_list[0]
    else:
        return user_list[0] + rec_sum(user_list[1:])


def sum_digits(n):
    n = int(math.fabs(n)) 
    d = n//10
    m = n%10
    if d==0:
        return m
    else:
        return m + sum_digits(d)

def flatten(user_list):
    output_list = []
    for i in user_list:
        if type(i)==list:
            flat_list = flatten(i)
            for j in flat_list:
                output_list.append(j)
        else:
            output_list.append(i)
    return output_list

def merge(list1, list2):
    output_list = []
    if len(list1)==0 and len(list2)==0:
        return []
    elif len(list1)==0:
        return list2
    elif len(list2)==0:
        return list1
    if list1[0]>=list2[0]:
        x = (merge(list1, list2[1:]))
        x.insert(0, list2[0])
        return x
    elif list1[0]<list2[0]:
        x = (merge(list1[1:], list2))
        x.insert(0, list1[0]) 
        return x

def iselvish(word):
    def searcher(word, pattern): #pattern should be a 2d list like [["e", False], ["f", False]]
        for i in pattern:
            if len(word)==0:
                check = True
                for j in pattern:
                    if not j[1]:
                        check = False
                return check
            if word[0]==i[0]:
                i[1] = True
        return searcher(word[1:], pattern)
    return searcher(word, [["e", False], ["l", False]])


def something_ish(word, pattern):
    def searcher(word, pattern): #pattern should be a 2d list like [["e", False], ["f", False]]
        for i in pattern:
            if len(word)==0:
                check = True
                for j in pattern:
                    if not j[1]:
                        check = False
                return check
            if word[0]==i[0]:
                i[1] = True
        return searcher(word[1:], pattern)

    formatted_pattern = []
    for i in pattern:
        formatted_pattern.append([i, False])
        
    return searcher(word, formatted_pattern)

print(something_ish("testword", "xyz"))

