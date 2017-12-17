from PIL import Image

def Laplace1(im, threshold):
	pixels = im.load()
	im_Laplace1 = Image.new('L', (im.size[0]-2 , im.size[1]-2), 'black')
	masks = [[0,1,0] , [1,-4,1] , [0,1,0]]

	for i in range(im_Laplace1.size[0]) :
		for j in range(im_Laplace1.size[0]) :
			result = 0
			for m in range(3) :
				for n in range(3) :
					result += pixels[i+m,j+n] * masks[2-m][2-n]
			result = 0 if result > threshold else 255
			im_Laplace1.putpixel((i,j) , result)

	return im_Laplace1

def Laplace2(im, threshold):
	pixels = im.load()
	im_Laplace2 = Image.new('L', (im.size[0]-2 , im.size[1]-2), 'black')
	masks = [[1,1,1] , [1,-8,1] , [1,1,1]]

	for i in range(im_Laplace2.size[0]) :
		for j in range(im_Laplace2.size[0]) :
			result = 0
			for m in range(3) :
				for n in range(3) :
					result += pixels[i+m,j+n] * masks[2-m][2-n]
			result =  result//3
			result = 0 if result > threshold else 255
			im_Laplace2.putpixel((i,j) , result)

	return im_Laplace2

def Minimum_variance_Laplacian(im, threshold):
	pixels = im.load()
	im_MvL = Image.new('L', (im.size[0]-2 , im.size[1]-2), 'black')
	masks = [[2,-1,2] , [-1,-4,-1] , [2,-1,2]]

	for i in range(im_MvL.size[0]) :
		for j in range(im_MvL.size[0]) :
			result = 0
			for m in range(3) :
				for n in range(3) :
					result += pixels[i+m,j+n] * masks[2-m][2-n]
			result =  result//3
			result = 0 if result > threshold else 255
			im_MvL.putpixel((i,j) , result)

	return im_MvL

def Laplace_of_Gaussian(im, threshold):
	pixels = im.load()
	im_LoG = Image.new('L', (im.size[0]-10 , im.size[1]-10), 'black')
	masks = [[  0,  0,  0, -1, -1, -2, -1, -1,  0,  0,  0],
			 [  0,  0, -2, -4, -8, -9, -8, -4, -2,  0,  0],
			 [  0, -2, -7,-15,-22,-23,-22,-15, -7, -2,  0],
			 [ -1, -4,-15,-24,-14, -1,-14,-24,-15, -4, -1],
			 [ -1, -8,-22,-14, 52,103, 52,-14,-22, -8, -1],
			 [ -2, -9,-23, -1,103,178,103, -1,-23, -9, -2],
			 [ -1, -8,-22,-14, 52,103, 52,-14,-22, -8, -1],
			 [ -1, -4,-15,-24,-14, -1,-14,-24,-15, -4, -1],
			 [  0, -2, -7,-15,-22,-23,-22,-15, -7, -2,  0],
			 [  0,  0, -2, -4, -8, -9, -8, -4, -2,  0,  0],
			 [  0,  0,  0, -1, -1, -2, -1, -1,  0,  0,  0]]

	for i in range(im_LoG.size[0]) :
		for j in range(im_LoG.size[0]) :
			result = 0
			for m in range(11) :
				for n in range(11) :
					result += pixels[i+m,j+n] * masks[10-m][10-n]
			result = 0 if result > threshold else 255
			im_LoG.putpixel((i,j) , result)

	return im_LoG


def Difference_of_Gaussian(im, threshold):
	pixels = im.load()
	im_DoG = Image.new('L', (im.size[0]-10 , im.size[1]-10), 'black')
	masks = [[ -1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
             [ -3, -5, -8,-11,-13,-13,-13,-11, -8, -5, -3],
             [ -4, -8,-12,-16,-17,-17,-17,-16,-12, -8, -4],
             [ -6,-11,-16,-16,  0, 15,  0,-16,-16,-11, -6],
             [ -7,-13,-17,  0, 85,160, 85,  0,-17,-13, -7],
             [ -8,-13,-17, 15,160,283,160, 15,-17,-13, -8],
             [ -7,-13,-17,  0, 85,160, 85,  0,-17,-13, -7],
             [ -6,-11,-16,-16,  0, 15,  0,-16,-16,-11, -6],
             [ -4, -8,-12,-16,-17,-17,-17,-16,-12, -8, -4],
             [ -3, -5, -8,-11,-13,-13,-13,-11, -8, -5, -3],
             [ -1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]]

	for i in range(im_DoG.size[0]) :
		for j in range(im_DoG.size[0]) :
			result = 0
			for m in range(11) :
				for n in range(11) :
					result += pixels[i+m,j+n] * masks[10-m][10-n]
			result = 0 if result < threshold else 255
			im_DoG.putpixel((i,j) , result)

	return im_DoG


if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')	

	im_Laplace1 = Laplace1(im , 15)
	im_Laplace1.save(benchmark+'_Laplace1.bmp')
	im_Laplace2 = Laplace2(im , 15)
	im_Laplace2.save(benchmark+'_Laplace2.bmp')	
	im_MvL = Minimum_variance_Laplacian(im , 20)
	im_MvL.save(benchmark+'_MvL.bmp')
	im_LoG = Laplace_of_Gaussian(im , 3000)
	im_LoG.save(benchmark+'_LoG.bmp')
	im_DoG = Difference_of_Gaussian(im , 1)
	im_DoG.save(benchmark+'_DoG.bmp')