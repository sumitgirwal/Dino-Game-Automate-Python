import pyautogui as p
from PIL import Image, ImageGrab
import time

def hit(key):
	p.keyDown(key)
	return 
	  
def isCollide(data):
	# when brid			
	for i in range(200, 230):
		# for Y axis
		for j in range(350, 410):
			#255 is white the 100 pixel is shellow dark
			if data[i, j] < 100:
				hit("down")
				return

	#when cactus arive
	# for X axis and width
	for i in range(240, 270):
		# for Y axis and height
		for j in range(410, 480):
			#255 is white the 100 pixel is shellow dark
			if data[i, j] < 100:
				hit("up")
				return

	return
				
	#image.show()
def showBlock(data):
	#when bird X
	for i in range(200, 230):
		# for Y axis
		for j in range(350, 410):
			#255 is white the 100 pixel is shellow dark
			data[i, j] = 100
				

	#when cactus arive
	# for X axis and width
	for i in range(230, 260):
		# for Y axis and height
		for j in range(410, 480):
			#255 is white the 100 pixel is shellow dark
			data[i, j] = 0
				
	

if __name__ == "__main__":
	print('Let Begin....')
	time.sleep(0)
	#hit('up')
	while True:
		image = ImageGrab.grab().convert('L')
		#load image for show
		data = image.load()
		isCollide(data)
		#showBlock(data)
		#image.show()
		#break
