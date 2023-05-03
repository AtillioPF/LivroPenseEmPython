#Exercises
def justifyRight(string):
    length = 70 - len(string)
    space = ''
    for a in range(length):
        space+=' '
        
    print(space+string)
    
def drawGrid(lines, columns):
    for l in range(lines):
        line = ''
        if lines%2==0:
            if l==0 or l==lines-1 or l==lines/2 or l==(lines/2)-1:
                line = drawColumn(columns, '+', '-')
            else:
                line = drawColumn(columns, '|', ' ')
        else:
            if l==0 or l==lines-1 or l==round((lines-1)/2):
                line = drawColumn(columns, '+', '-')
            else:
                line = drawColumn(columns, '|', ' ')
        print(line)
                
def drawColumn(columns, char_one, char_two):
    line = ''
    for c in range(columns):
        if columns%2==0:
            if c==0 or c==columns-1 or c==columns/2 or c==(columns/2)-1:
                line+=char_one
            else:
                line+=char_two
        else:
            if c==0 or c==columns-1 or c==round((columns-1)/2):
                line+=char_one
            else:
                line+=char_two
    return line
        
    
justifyRight("Atillio")
justifyRight("Is very awesome")
drawGrid(6,6)
drawGrid(24,28)