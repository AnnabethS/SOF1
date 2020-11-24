def print_all(num_list):
    if type(num_list)!=list:
        raise TypeError
    if len(num_list)==0:
        return ""
    else:
        if type(num_list[0])!=int:
            raise TypeError
        return str(num_list[0])+ "\n" + print_all(num_list[1:])

def print_all_reverse(num_list):
    if type(num_list)!=list:
        raise TypeError
    if len(num_list)==0:
        return ""
    else:
        if type(num_list[len(num_list)-1])!=int:
            raise TypeError
        return str(num_list[len(num_list)-1])+ "\n" + print_all_reverse(num_list[:-1])

def to_binary(num):
    if num>255 or num<0:
        raise ValueError
    if num==0:
        return "0"
    elif num==1:
        return "1"
    else:
        d, m = divmod(num, 2)
        return str(m) + to_binary(d)

def to_base10(binary):
    def finder(binary, num):
        if binary=="":
            return 0
        else:
            return (2^num) *int(binary[len(binary)-1]) + finder(binary[:-1], num+1)
    return finder(binary, 1)

print(to_base10(to_binary(83)))