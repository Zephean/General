# getting key information
# row/col for top corner
masterRow = input('Top corner row # (R value/8): ')
masterCol = input('Top corner column # (G value/8): ')

# X/Y for top corner
masterX = input('Top corner X position: ')
masterY = input('Top corner Y position: ')

# How big the polygon is
rows = input('Number of rows (left of top corner): ')
columns = input('Number of columns (right of top corner): ')

# colorGrid scale
squareWidth = input('Color grid square width: ')
squareHeight = input('Color grid square height: ')


'''masterRow = 3
masterCol = 0
masterX = 469
masterY = 240
rows = 7
columns = 4
squareWidth = 42
squareHeight = 26'''

gridCoords = []
pixelCoords = []

for c in range(0, columns):
    for r in range(0, rows):
        x = masterX + ((c * (squareWidth/2)) - (r * (squareWidth/2)))
        y = masterY + (c + r) * (squareHeight/2)
        gridCoords.append(str(r+masterRow) + ',' + str(c+masterCol))
        pixelCoords.append(str(x) + ',' + str(y))

print('\n//gridCoords')
for item in gridCoords:
    print item + ';'

print('\n//pixelCoords')
for item in pixelCoords:
    print item + ';'
