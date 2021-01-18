def encrypt(message, shifts, alphabet):
    """encrypts a message using a caesar cipher, which changes the shift per letter

    Args:
        message (string): the message to be encrypted, must be the same length as shifts
        shifts (list of integers): a list of integers the same length as the message, the amount to shift each character of message
        alphabet (string): the alphabet to use in a string with no spaces

    Raises:
        ValueError: raised if message and shifts are not the same length
        ValueError: raised if a shift is larger than the alphabet length or less than 0
        ValueError: raised if a character in message is not in the alphabet

    Returns:
        outputstring: an encrypted version of message, shifted by the amounts defined in shifts
    """
    if len(message)!=len(shifts): #check if the sizes of message and shifts are the same if not raise an error
        raise ValueError
    outputstring = ""
    for i in range(len(message)):
        if shifts[i]>=len(alphabet) or shifts[i]<0: #if the shift is negative or greater than or equal to alphabet size raise an error
            raise ValueError
        position = alphabet.find(message[i]) #find the position of the character under inspection in the alphabet
        if position==-1: #find returns -1 if it cannot find the character, if this is the case then raise a valuerror
            raise ValueError
        position = (position + shifts[i]) % len(alphabet) #add the shift to the letter, use mod to wrap the position to the alphabet length
        #the use of mod means that for example position 27 becomes position 2
        outputstring += (alphabet[position]) #add the shifted character to the output string
    return outputstring