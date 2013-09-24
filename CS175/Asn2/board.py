import subprocess as sub

max_row = 440
max_col = 630

row = 0
col = 0

colwidth = 78
rowheight = 55

board = sub.Popen('./Sketchpad.jar', 1, stdin=sub.PIPE).stdin

for x in range(7):
	row1 = ' 0'
	row2 = ' 450'
	col += colwidth
	y = ' ' + str(col)
	board.write(bytes("drawSegment" + y + row1 + y + row2 + '\n', 'UTF-8'))
	board.flush()

for x in range(7):
	col1 = ' 0'
	col2 = ' 640'
	row += rowheight
	x = ' ' + str(row)
	board.write(bytes("drawSegment" + col1 + x + col2 + x + '\n', 'UTF-8'))
	board.flush()

junk = input('just chillin')
board.write(bytes('end\n', 'UTF-8'))