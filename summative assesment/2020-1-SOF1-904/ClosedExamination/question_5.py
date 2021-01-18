class Blotris:
    def __init__(self, rows, cols):
        if rows<5 or cols<5:
            raise ValueError
        self._board = [] #initialise an empty board
        self._board_width = cols
        self._board_height = rows
        for i in range(rows):
            blank_row = []
            for j in range(cols):
                blank_row.append(0) #0 represents a blank space, we are filling the board with blank spaces
            self._board.append(blank_row.copy()) #append a copy of the list or when one row is changed, the others will change to match it

    def add(self, shape, row, col):
        if row<0 or row>=self._board_height or col<0 or col>= self._board_width: #make sure that the starting position of the block is in range
            return False
        shape_width = len(shape[0])
        shape_height = len(shape)
        if (col + shape_width> self._board_width) or (row + shape_height> self._board_height):
            #check that the block would not go off the edge of the board when added
            return False
        #the shape is within the bounds of the board
        for i in range(shape_height):
            for j in range(shape_width):
                if shape[i][j]==1: #check the spaces which the shape would fill
                    if self._board[row+i][col+j]==1:
                        return False #if any of the spaces the block should fill are already filled, it cannot be added, return false
        for i in range(shape_height):
            for j in range(shape_width):
                if shape[i][j]==1:
                    self._board[row+i][col+j] = 1 #add the shape to the board space by space
        return True

    def update(self):
        delete_rows = []
        for i in range(len(self._board)):
            if not 0 in self._board[i]: #check if there are any 0s on the board, if there are not the row is complete
                delete_rows.append(i) #add the row to the list of rows to be deleted
        for i in reversed(delete_rows): #reverse the list of rows before iterating through so that they are deleted top to bottom,
            #meaning that the indexes of the rows still to be deleted are not affected by the ones that have already been deleted moving the others down an index
            self._board.pop(i)
        new_row = []
        for j in range(self._board_width):
            new_row.append(0)
        for i in range(len(delete_rows)): #replace the rows that have been deleted by adding blank rows at the top of the board
            self._board.insert(0, new_row.copy())
        