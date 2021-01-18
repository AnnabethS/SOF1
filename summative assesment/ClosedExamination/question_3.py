ATOMS = {
    'H':{'name':'Hydrogen', 'weight':1.00797},
    'He':{'name':'Helium', 'weight':4.00260},
    'C':{'name':'Carbon', 'weight':12.011},
    'N':{'name':'Nitrogen', 'weight':14.0067},
    'O':{'name':'Oxygen', 'weight':15.9994},
    'Ca':{'name':'Calium', 'weight':40.08}    
    }

def molar_mass(molecule):
    total = 0
    for i in molecule:
        if not (i[0] in ATOMS.keys()): #check that the atom is a valid key in the ATOMS dictionary
            raise ValueError
        single_mass = ATOMS[i[0]]["weight"] #get the molar mass of a single atom
        total += single_mass * i[1] #multiply by how many atoms there are of this type
    return total

