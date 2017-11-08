from test import *
class Bomb():

	status = -1
	enem_up = -1
	enem_right = -1
	enem_down = -1
	enem_left = -1

	def place(self,row,col):
		if self.status==-1:
			self.status = 3
			self.row = row
			self.col = col
			matrix[row][col] = 53

	def which_enem(self,r,c):
		for i in range(len(enemies)):
			if enemies[i].row == r and enemies[i].col == c:
				return i
		return -1

	def determine(self,r,c):
		return matrix[r][c]

	def explode(self,bmrow,bmcol):
		self.up = self.determine(self.row-1,self.col)
		self.right = self.determine(self.row,self.col+1)
		self.down = self.determine(self.row+1,self.col)
		self.left = self.determine(self.row,self.col-1)
		if bmrow==self.row and bmcol==self.col:
			self.center = 3
		else:
			self.center = 0

		if self.up != 1:
			matrix[self.row-1][self.col] = 50
			if self.up == 4:
				self.enem_up = self.which_enem(self.row-1,self.col)

		if self.right != 1:
			matrix[self.row][self.col+1] = 50
			if self.up == 4:
				self.enem_right = self.which_enem(self.row,self.col+1)
		if self.down != 1:
			matrix[self.row+1][self.col] = 50
			if self.up == 4:
				self.enem_down = self.which_enem(self.row+1,self.col)
		if self.left != 1:
			matrix[self.row][self.col-1] = 50
			if self.up == 4:
				self.enem_left = self.which_enem(self.row,self.col-1)

		matrix[self.row][self.col] = 50

	def restore(self,bmobj):
		if self.up==3 or self.right==3 or self.down==3 or self.left==3 or self.center==3:
			bmobj.death()

		matrix[self.row][self.col] = 0

		if self.up==2 or self.up==0:
			matrix[self.row-1][self.col] = 0
		elif self.up==4:
			enemies.remove(enemies[self.enem_up])
			matrix[self.row-1][self.col] = 0

		if self.right==2 or self.right==0:
			matrix[self.row][self.col+1] = 0
		elif self.right==4:
			enemies.remove(enemies[self.enem_right])
			matrix[self.row][self.col+1] = 0

		if self.down==2 or self.down==0:
			matrix[self.row+1][self.col] = 0
		elif self.down==4:
			enemies.remove(enemies[self.enem_down])
			matrix[self.row+1][self.col] = 0

		if self.left==2 or self.left==0:
			matrix[self.row][self.col-1] = 0
		elif self.left==4:
			enemies.remove(enemies[self.enem_left])
			matrix[self.row][self.col-1] = 0



	def detonate(self,bmobj):
		if self.status==2 or self.status==3:
			self.status-=1
			matrix[self.row][self.col] = 50 + self.status
		elif self.status==1:
			self.explode(bmobj.row,bmobj.col)
			self.status = 0
		elif self.status == 0:
			self.restore(bmobj)
			self.status = -1