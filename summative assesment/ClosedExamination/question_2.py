def molecule_to_list(molecule):
    if not(molecule[0].isalpha() and molecule[0].isupper()): #check the fist char is a letter and uppercase
        raise ValueError
    if not molecule.isalnum(): #check the entire string is alphanumeric
        raise ValueError
    molecule_list = []
    pointer = 0
    next_atom_name = ""
    next_atom_num = 0
    while pointer<len(molecule):
        if molecule[pointer].islower(): #check that the atom starts with a capital
            raise ValueError
        if pointer+1<len(molecule): #check there wont be an out of range error in this
            if molecule[pointer+1].isalpha() and not molecule[pointer+1].isupper(): #the atom symbol is 2 letters long
                next_atom_name=molecule[pointer:pointer+2]
                numstart = pointer+2
            else: #the atom symbol is 1 letter long
                next_atom_name = molecule[pointer]
                numstart = pointer+1
        else: #we are looking at the last letter in the string so it must be 1 letter long
            next_atom_name = molecule[pointer]
            numstart = pointer+1
        if numstart<len(molecule):#check there wont be an out of range error in this
            if molecule[numstart].isnumeric(): #is there a number there at all, if not then this atom does not have a number and has amount 1
                if numstart+1<len(molecule):#check there wont be an out of range error in this
                    if molecule[numstart+1].isnumeric(): #double digit number examining
                        next_atom_num = int(molecule[numstart:numstart+2])
                        pointer = numstart+2
                    else:
                        next_atom_num = int(molecule[numstart])
                        pointer = numstart+1
                else:
                    next_atom_num = int(molecule[numstart])
                    pointer = numstart+1
            else:
                next_atom_num = 1
                pointer = numstart
        else:
            next_atom_num = 1
            pointer = numstart
        molecule_list.append((next_atom_name, next_atom_num))
    return molecule_list

