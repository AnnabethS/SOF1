#EX 1
a_word = "bruh"
f = open("Week 5/exo1.txt", "w")
f.write(a_word)
f.close()

#EX 2
def save_list2file(sentences, filename):
    f = open(filename, "w")
    for i in sentences:
        f.write(i + "\n")
    f.close()

save_list2file(["test", "test2", "test3"], "Week 5/exo2.txt")
    
#EX 3

def save_to_log(entry, filename):
    f = open(filename, "a")
    f.write(entry + "\n")
    f.close()

save_to_log("THIS IS A TEST ENTRY", "Week 5/exo3.txt")

#EX 4
def fileUpper(filename):
    f = open(filename, "r")
    lines = f.readlines()
    for i in lines:
        print(i.upper())
    f.close()

fileUpper("Week 5/sampleFile.txt")

#EX 5
def to_upper_case(inp_filename, out_filename):
    f = open(inp_filename, "r")
    lines = f.readlines()
    f.close()
    f = open(out_filename, "w")
    for i in lines:
        f.write(i.upper() + "\n")

to_upper_case("Week 5/sampleFile.txt", "Week 5/exo5.txt")

#EX 6
def sum_list(numlist):
    total = 0
    for i in numlist:
        total = total + i
    return total

def sum_from_file(filename):
    """Reads integers from a file and sums them  together. The integers
    must be seperated by single spaces and the file can go onto
    multiple lines

    Args:
        filename (String): The relative path to the file from the 
        project directory root

    Returns:
        int: the total of all of the numbers from the file summed 
        together
    """    
    lines = []
    nums = []
    f = open(filename, "r")
    lines = f.readlines()
    for i in lines:
        temp = i.split(" ")
        for i in temp:
            nums.append(i)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return sum_list(nums)
    

print(sum_from_file("Week 5/exo6.txt"))
