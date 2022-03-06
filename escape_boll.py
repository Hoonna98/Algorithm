from collections import deque

n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]
dx,dy = [-1,0,1,0],[0,1,0,-1]
mic = 11
r,b,h = 0,0,0
for i in range(n):
	for j in range(m):
		if board[i][j] == 'B':
			b = (j,i)
		elif board[i][j] == 'R':
			r = (j,i)
		elif board[i][j] == 'O':
			h = (j,i)
if r == 0 or b == 0 or h == 0:
	print(-1)
	exit(0)
	
def lean(direc, r,b):
	rx,ry = r
	bx,by = b
	fr,fb = r, b

	while True:
		rx = rx+dx[direc]
		ry = ry+dy[direc]
		if board[ry][rx] == '.':
			continue
		elif board[ry][rx] == '#':
			r = (rx-dx[direc],ry-dy[direc])
			break
		elif board[ry][rx] == 'O':
			r = (rx,ry)
			break
	while True:
		bx = bx+dx[direc]
		by = by+dy[direc]
		if board[by][bx] == '.':
			continue
		elif board[by][bx] == '#':
			b = (bx-dx[direc],by-dy[direc])
			break
		elif board[by][bx] == 'O':
			b = (bx,by)
			break

	if r == b and board[r[1]][r[0]] != 'O':
		if direc == 0:
			if fr[0]-fb[0]>0:
				r = (r[0]-dx[direc],r[1]-dy[direc])
			else:
				b = (b[0]-dx[direc],b[1]-dy[direc])
		elif direc == 2:
			if fr[0]-fb[0]<0:
				r = (r[0]-dx[direc],r[1]-dy[direc])
			else:
				b = (b[0]-dx[direc],b[1]-dy[direc])
		elif direc == 3:
			if fr[1]-fb[1]>0:
				r = (r[0]-dx[direc],r[1]-dy[direc])
			else:
				b = (b[0]-dx[direc],b[1]-dy[direc])
		else:
			if fr[1]-fb[1]<0:
				r = (r[0]-dx[direc],r[1]-dy[direc])
			else:
				b = (b[0]-dx[direc],b[1]-dy[direc])
	return r,b

def bfs():
	while que:
		r,b,c = que.popleft()
		if c > 10:
			return -1
		for i in range(4):
			nr,nb = lean(i,r,b)
			if nr == nb:
				return -1
			if nr == h:
				return c + 1
			if nr == r:
				continue
			que.append([nr,nb,c+1])

que = deque()
que.append([r,b,0])
print(bfs())