#A=rock, B=paper, C=scissors
#A=1,B=2,C=3
def lose(fmove):
	print('lost')
	if fmove=='A':
		return 3
	elif fmove=='B':
		return 1
	else:
		return 2
def draw(fmove):
	print('draw')
	mval={'A':1,'B':2,'C':3}
	return mval[fmove]+3
def win(fmove):
	print('win')
	mval={'A':2,'B':3,'C':1}
	return mval[fmove]+6
moves={'X':lose,'Y':draw,'Z':win}
with open("/storage/emulated/0/Download/input (1).txt") as f:
	f.seek(0)
	guide=f.readlines()
scoref=0
for line in guide:
	scoref+=moves[line[2]](line[0])
print('final: ',scoref)