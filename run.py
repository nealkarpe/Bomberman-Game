from test import *
from bomb import *

def Main():
	generate_walls()
	generate_enemies(3)
	generate_bricks()

	bm = Bomberman(1,1)
	kb = KBHit()
	bomb = Bomb()
	lastTime = time.time()

	while True:
		os.system("clear")
		print_matrix()
		lastTime=time.time()
		if kb.kbhit():
			c = kb.getch()
			if c=='w':
				bm.move(0)
			elif c=='d':
				bm.move(1)
			elif c=='s':
				bm.move(2)
			elif c=='a':
				bm.move(3)
			elif c=='b':
				bomb.place(bm.row,bm.col)

#			if time.time() - lastTime >= 0.1:
#				for e in enemies:
#					dir = e.choose_dir()
#					if dir>=0 and dir<=3:
#						e.move(dir)
			#print_matrix()

		else:
			time.sleep(0.5)
			if time.time() - lastTime >= 0.5:
				bomb.detonate(bm)
				for e in enemies:
					dir = e.choose_dir()
					if dir>=0 and dir<=3:
						e.move(dir)



			#print_matrix()



Main()