from termcolor import colored
import random
import time
from kbhit import KBHit
import os

#codes: 0-air 1-wall 2-brick 3-bomberman 4-enemy 5-bomb

matrix = list()
class Wall():
	def __init__(self,row,col):
		self.row = row
		self.col = col

class Brick():
	def __init__(self,row,col):
		self.row = row
		self.col = col



walls = list()
bricks = list()
def generate_walls():
	for i in range(17):
		templist = list()
		if i==0 or i==16:
			for j in range(17):
				templist.append(1)
				classobj = Wall(i,j)
				walls.append(classobj)

		elif i%2==1:
			for j in range(17):
				if j==0 or j==16:
					templist.append(1)
					classobj = Wall(i,j)
					walls.append(classobj)
				else:
					templist.append(0)
		else:
			for j in range(17):
				if j%2==0:
					templist.append(1)
					classobj = Wall(i,j)
					walls.append(classobj)

				else:
					templist.append(0)
		matrix.append(templist)



def generate_bricks():
	for i in range(1,16):
		for j in range(1,16):
			if matrix[i][j]==0:
				rnd = random.random()
				if rnd < 0.1:
					matrix[i][j]=2
					classobj = Brick(i,j)
					bricks.append(classobj)
					
	matrix[1][1]=3
	matrix[1][2]=0
	matrix[2][1]=0


def print_matrix():
	strings = list()
	for ls in matrix:
		templist1 = list()
		templist2 = list()
		for num in ls:
			if num==0:
				templist1.append("    ")
				templist2.append("    ")
			elif num==1:
				templist1.append("XXXX")
				templist2.append("XXXX")
			elif num==2:
				templist1.append(colored("////", "grey", attrs=["bold"]))
				templist2.append(colored("////", "grey", attrs=["bold"]))
			elif num==3:
				templist1.append(colored("BBBB", "blue"))
				templist2.append(colored("BBBB", "blue"))
			elif num==4:
				templist1.append(colored("EEEE", "red"))
				templist2.append(colored("EEEE", "red"))
			elif num==53:
				templist1.append(colored("3333", "green", attrs=["bold"]))
				templist2.append(colored("3333", "green", attrs=["bold"]))
			elif num==52:
				templist1.append(colored("2222", "green", attrs=["bold"]))
				templist2.append(colored("2222", "green", attrs=["bold"]))
			elif num==51:
				templist1.append(colored("1111", "green", attrs=["bold"]))
				templist2.append(colored("1111", "green", attrs=["bold"]))
			elif num==50:
				templist1.append(colored("0000", "yellow", attrs=["bold"]))
				templist2.append(colored("0000", "yellow", attrs=["bold"]))

		strings.append(templist1)
		strings.append(templist2)

	for string in strings:
		print("".join(string))

def instantiate(objectName,row,col):
	objectName.row = row
	objectName.col = col
	matrix[row][col] = objectName.code

class Person():

	def __init__(self,initrow,initcol):
		'''self.row = initrow
		self.col = initcol
		matrix[initrow][initcol] = self.code'''
		instantiate(self,initrow,initcol)

	def move(self,key):
		# 0-up 1-right 2-down 3-left
		if key==0:
			if self.code==3 and matrix[self.row-1][self.col]==4:
				self.death()
			elif self.code==4 and matrix[self.row-1][self.col]==3:
				self.kill()
			elif self.row>=2 and self.row<=15 and matrix[self.row-1][self.col]==0:
				matrix[self.row][self.col] = 0
				matrix[self.row-1][self.col] = self.code
				self.row -= 1
		elif key==1:
			if self.code==3 and matrix[self.row][self.col+1]==4:
				self.death()
			elif self.code==4 and matrix[self.row][self.col+1]==3:
				self.kill()
			elif self.col>=1 and self.col<=14 and matrix[self.row][self.col+1]==0:
				matrix[self.row][self.col] = 0
				matrix[self.row][self.col+1] = self.code
				self.col += 1
		elif key==2:
			if self.code==3 and matrix[self.row+1][self.col]==4:
				self.death()
			elif self.code==4 and matrix[self.row+1][self.col]==3:
				self.kill()
			elif self.row>=1 and self.row<=14 and matrix[self.row+1][self.col]==0:
				matrix[self.row][self.col] = 0
				matrix[self.row+1][self.col] = self.code
				self.row += 1
		elif key==3:
			if self.code==3 and matrix[self.row][self.col-1]==4:
				self.death()
			elif self.code==4 and matrix[self.row][self.col-1]==3:
				self.kill()
			elif self.col>=2 and self.col<=15 and matrix[self.row][self.col-1]==0:
				matrix[self.row][self.col] = 0
				matrix[self.row][self.col-1] = self.code
				self.col -= 1

class Bomberman(Person):
	code = 3

	def death(self):
		print("GAME OVER")
		exit()

class Enemy(Person):
	code = 4

	def kill(self):
		print("GAME OVER")
		exit()

	def isvalid_dir(self,num):
		if num==0:
			if matrix[self.row-1][self.col]==1 or matrix[self.row-1][self.col]==2:
				return False
			else:
				return True
		elif num==1:
			if matrix[self.row][self.col+1]==1 or matrix[self.row][self.col+1]==2:
				return False
			else:
				return True
		elif num==2:
			if matrix[self.row+1][self.col]==1 or matrix[self.row+1][self.col]==2:
				return False
			else:
				return True
		elif num==3:
			if matrix[self.row][self.col-1]==1 or matrix[self.row][self.col-1]==2:
				return False
			else:
				return True

	def choose_dir(self):
		x = random.randint(0,3)
		if self.isvalid_dir(x):
			return x
		val = x
		if not self.isvalid_dir(x):
			x = (x+1) % 4
		if not self.isvalid_dir(x):
			x = (x+1) % 4
		if not self.isvalid_dir(x):
			x = (x+1) % 4
		if not self.isvalid_dir(x):
			x = (x+1) % 4
		if val == x:
			return -1;
		else:
			return x

enemies = list()

def generate_enemies(x):
	for _ in range(x):
		row = random.randint(1,15)
		col = random.randint(1,15)

		while matrix[row][col]!=0 or (row==1 and col==1) or (row==1 and col==2) or (row==2 and col==1):
			row = random.randint(1,15)
			col = random.randint(1,15)

		e = Enemy(row,col)
		enemies.append(e)
