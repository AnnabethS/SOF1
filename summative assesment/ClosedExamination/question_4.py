def check_level(level):
    if len(level)==1: #if the list is 1 long, we are on the final spring, the level is complete
        return True
    if level[len(level)-1]==0: #if the last element of the list is a 0, the level is impossible, return false
        return False
    if level[0]==0: #if the first element of the list is a 0, the level is impossible, return false
        return False
    else:
        for i in range(1, level[0]+1): #iterate from 1 to the current spring's number inclusive
            if level[i]==0: #if the position we are about to jump to is a 0, then dont jump there, check the next position
                continue
            result = check_level(level[i:]) #recur through the rest of the level from the position we are about to jump to
            if result: #if the result returned true, then that path must have been able to finish the level, return true
                return True
        return False #if none of the options from this spring worked then the level cannot be completed from this spring, return false
