from PIL import Image
import numpy as np

def getpixel(im , x , y):
	pixels = im.load()
	try :
		return pixels[x,y]
	except :
		return 0

def getneighbor(im , center , size) :	
	pixels = im.load()

	neighbor = []
	for m in range(-(size//2),size//2+1) :
		tmp = []
		for n in range(-(size//2),size//2+1) :
			tmp.append(getpixel(im,center[0]+m,center[1]+n))
		neighbor.append(tmp)

	return neighbor

def Robert(im, threshold):
	pixels = im.load()
	im_robert = Image.new('L', im.size, 'black')
	masks = [[[-1,0],[0,1]] , [[0,-1],[1,0]]]

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(2) :
					for n in range(2) :
						r += getpixel(im,i+m,j+n)*masks[num_mask][m][n]
				r_sqt.append(r**2)
			result = 0 if np.sqrt(sum(r_sqt)) > threshold else 255
			im_robert.putpixel((i,j) , result)

	return im_robert

def Prewitt(im, threshold):
	pixels = im.load()
	im_prewitt = Image.new('L', im.size, 'black')
	masks = [[[-1,-1,-1],[0,0,0],[1,1,1]] , [[-1,0,1],[-1,0,1],[-1,0,1]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(3) :
					for n in range(3) :
						r += getpixel(im,i+n,j+m)*masks[num_mask][m][n]
				r_sqt.append(r**2)
			result = 0 if np.sqrt(sum(r_sqt)) > threshold else 255
			im_prewitt.putpixel((i,j) , result)

	return im_prewitt

def Sobel(im, threshold):
	pixels = im.load()
	im_sobel = Image.new('L', im.size, 'black')
	masks = [[[-1,-2,-1],[0,0,0],[1,2,1]] , [[-1,0,1],[-2,0,2],[-1,0,1]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(-(size//2),size//2+1) :
					for n in range(-(size//2),size//2+1) :
						r += getpixel(im,i+n,j+m)*masks[num_mask][m][n]
				r_sqt.append(r**2)
			result = 0 if np.sqrt(sum(r_sqt)) > threshold else 255
			im_sobel.putpixel((i,j) , result)

	return im_sobel

def Frei_and_Chen(im, threshold):
	pixels = im.load()
	im_fac = Image.new('L', im.size, 'black')
	masks = [[[-1,-np.sqrt(2),-1],[0,0,0],[1,np.sqrt(2),1]] , [[-1,0,1],[-np.sqrt(2),0,np.sqrt(2)],[-1,0,1]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0.
				for m in range(-(size//2),size//2+1) :
					for n in range(-(size//2),size//2+1) :
						r += float(getpixel(im,i+n,j+m))*masks[num_mask][m][n]
				r_sqt.append(r**2)
			result = 0 if np.sqrt(sum(r_sqt)) > threshold else 255
			im_fac.putpixel((i,j) , result)

	return im_fac


def Kirsch(im, threshold):
	pixels = im.load()
	im_kirsch = Image.new('L', im.size, 'black')
	masks = [[[-3,-3,5],[-3,0,5],[-3,-3,5]] , [[-3,5,5],[-3,0,5],[-3,-3,-3]] ,
			 [[5,5,5],[-3,0,-3],[-3,-3,-3]] , [[5,5,-3],[5,0,-3],[-3,-3,-3]] ,
			 [[5,-3,-3],[5,0,-3],[5,-3,-3]] , [[-3,-3,-3],[5,0,-3],[5,5,-3]] ,
			 [[-3,-3,-3],[-3,0,-3],[5,5,5]] , [[-3,-3,-3],[-3,0,5],[-3,5,5]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(-(size//2),size//2+1) :
					for n in range(-(size//2),size//2+1) :
						r += getpixel(im,i+n,j+m)*masks[num_mask][m][n]
				r_sqt.append(r)
			result = 0 if max(r_sqt) > threshold else 255
			im_kirsch.putpixel((i,j) , result)

	return im_kirsch

def Robinson(im, threshold):
	pixels = im.load()
	im_robinson = Image.new('L', im.size, 'black')
	masks = [[[-1,0,1],[-2,0,2],[-1,0,1]] , [[0,1,2],[-1,0,1],[-2,-1,0]] ,
			 [[1,2,1],[0,0,0],[-1,-2,-1]] , [[2,1,0],[1,0,-1],[0,-1,-2]] ,
			 [[1,0,-1],[2,0,-2],[1,0,-1]] , [[0,-1,-2],[1,0,-1],[2,1,0]] ,
			 [[-1,-2,-1],[0,0,0],[1,2,1]] , [[-2,-1,0],[-1,0,1],[0,1,2]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(-(size//2),size//2+1) :
					for n in range(-(size//2),size//2+1) :
						r += getpixel(im,i+n,j+m)*masks[num_mask][m][n]
				r_sqt.append(r)
			result = 0 if max(r_sqt) > threshold else 255
			im_robinson.putpixel((i,j) , result)

	return im_robinson

def Nevatia_and_Babu(im, threshold):
	pixels = im.load()
	im_nab = Image.new('L', im.size, 'black')
	masks = [[[ 100, 100, 100, 100, 100] , [ 100, 100, 100, 100, 100] , [   0,   0,   0,   0,   0] , [-100,-100,-100,-100,-100] , [-100,-100,-100,-100,-100]] ,
			 [[ 100, 100, 100, 100, 100] , [ 100, 100, 100,  78, -32] , [ 100,  92,   0, -92,-100] , [  32, -78,-100,-100,-100] , [-100,-100,-100,-100,-100]] ,
			 [[ 100, 100, 100,  32,-100] , [ 100, 100,  92, -78,-100] , [ 100, 100,   0,-100,-100] , [ 100,  78, -92,-100,-100] , [ 100, -32,-100,-100,-100]] ,
			 [[-100,-100,   0, 100, 100] , [-100,-100,   0, 100, 100] , [-100,-100,   0, 100, 100] , [-100,-100,   0, 100, 100] , [-100,-100,   0, 100, 100]] ,
			 [[-100,  32, 100, 100, 100] , [-100, -78,  92, 100, 100] , [-100,-100,   0, 100, 100] , [-100,-100, -92,  78, 100] , [-100,-100,-100, -32, 100]] ,
			 [[ 100, 100, 100, 100, 100] , [ -32,  78, 100, 100, 100] , [-100, -92,   0,  92, 100] , [-100,-100,-100, -78,  32] , [-100,-100,-100,-100,-100]]]

	size = len(masks[0])

	for i in range(im.size[0]) :
		for j in range(im.size[0]) :
			r_sqt = []
			for num_mask in range(len(masks)) :
				r = 0
				for m in range(-(size//2),size//2+1) :
					for n in range(-(size//2),size//2+1) :
						r += getpixel(im,i+n,j+m)*masks[num_mask][m][n]
				r_sqt.append(r)
			result = 0 if max(r_sqt) > threshold else 255
			im_nab.putpixel((i,j) , result)

	return im_nab






if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')	

	im_robert = Robert(im,12)
	im_robert.save(benchmark+'_robert.bmp')
	im_prewitt = Prewitt(im,24)
	im_prewitt.save(benchmark+'_prewitt.bmp')
	im_sobel = Sobel(im,38)
	im_sobel.save(benchmark+'_sobel.bmp')
	im_fac = Frei_and_Chen(im,30)
	im_fac.save(benchmark+'_frei_and_chen.bmp')
	im_kirsch = Kirsch(im,135)
	im_kirsch.save(benchmark+'_kirsch.bmp')
	im_robinson = Robert(im,43)
	im_robinson.save(benchmark+'_robinson.bmp')
	im_nab = Nevatia_and_Babu(im,12500)
	im_nab.save(benchmark+'_nevatia_and_babu.bmp')


