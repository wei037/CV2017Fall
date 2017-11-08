from PIL import Image

def dilation(im , kernel) :
	pixels = im.load()
	im_dil = Image.new('L', im.size, 'black')

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			if (pixels[i,j]) != 0 :
				Max = 0
				for k in range(len(kernel)):
					if (i+kernel[k][0] >= 0 and j+kernel[k][1] >= 0 and i+kernel[k][0] < im.size[0] and j+kernel[k][1] < im.size[1]) :
						Max = pixels[i+kernel[k][0] , j+kernel[k][1]] if pixels[i+kernel[k][0] , j+kernel[k][1]] > Max else Max
				for k in range(len(kernel)):
					if (i+kernel[k][0] >= 0 and j+kernel[k][1] >= 0 and i+kernel[k][0] < im.size[0] and j+kernel[k][1] < im.size[1]) :
						im_dil.putpixel((i+kernel[k][0] , j+kernel[k][1]) , Max)
						
	return im_dil
def erosion(im , kernel) : 
	pixels = im.load()
	im_ero = Image.new('L', im.size, 'black')

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			Min = 255
			erosion = 1
			for k in range(len(kernel)):
				if (i+kernel[k][0] < 0 or j+kernel[k][1] < 0 or i+kernel[k][0] >= im.size[0] or j+kernel[k][1] >= im.size[1] or pixels[i+kernel[k][0] , j+kernel[k][1]] == 0) :
					erosion = 0

			if erosion == 1 :
				for k in range(len(kernel)):
					Min = pixels[i+kernel[k][0] , j+kernel[k][1]] if pixels[i+kernel[k][0] , j+kernel[k][1]] < Min else Min
										
				im_ero.putpixel((i, j) , Min)
						
	return im_ero

def opening(im , kernel) :
	return dilation(erosion(im , kernel) , kernel)
	
def closing(im , kernel) :
	return erosion(dilation(im , kernel) , kernel)



if __name__ == '__main__' :

	kernel =          [[-2,-1] , [-2, 0] , [-2, 1] ,
			 [-1,-2] , [-1,-1] , [-1, 0] , [-1, 1] , [-1, 2] ,
			 [ 0,-2] , [ 0,-1] , [ 0, 0] , [ 0, 1] , [ 0, 2] ,
			 [ 1,-2] , [ 1,-1] , [ 1, 0] , [ 1, 1] , [ 1, 2] ,
			 		   [ 2,-1] , [ 2, 0] , [ 2, 1]]

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	im_dilation = dilation(im, kernel)
	im_erosion = erosion(im, kernel)
	im_open = opening(im_thre , kernel)
	im_close = closing(im_thre , kernel)

	im_dilation.save(benchmark+'_dilation.bmp')
	im_erosion.save(benchmark+'_erosion.bmp')
	im_open.save(benchmark+'_opening.bmp')
	im_close.save(benchmark+'_closing.bmp')