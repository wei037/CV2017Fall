from PIL import Image

###threshold##

def binarize(im , threshold) :
	pixels = im.load()
	print (pixels[0,0])
	im_thre = im.copy()

	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_thre.putpixel((i,j), (pixels[i,j] > threshold)*255 )

	return im_thre

def dilation(im , kernel):
	pixels = im.load()
	im_dil = Image.new('L', im.size, 'black')

	for i in range(1,int(im.size[0])-1) :
		for j in range(1,int(im.size[1])-1) :
			for k in range(len(kernel)):
				if(pixels[i,j] == 255):
					im_dil.putpixel((i+kernel[k][0],j+kernel[k][1]), 255 )
	return im_dil

def erosion(im , kernel) :
	pixels = im.load()
	im_ero = Image.new('L', im.size, 'white')
	for i in range(int(im.size[0])) :
		im_ero.putpixel((i,0), 0)
		im_ero.putpixel((i,511), 0)
		im_ero.putpixel((0,i), 0)
		im_ero.putpixel((511,i), 0)


	for i in range(1,int(im.size[0])-1) :
		for j in range(1,int(im.size[1])-1) :
			for k in range(len(kernel)):
				if(pixels[i,j] == 0):
					im_ero.putpixel((i+kernel[k][0],j+kernel[k][1]), 0 )
	return im_ero

def opening(im , kernel):
	return dilation(erosion(im , kernel) , kernel)

def closing(im , kernel):
	return erosion(dilation(im , kernel) , kernel)

def hit_miss(im , J , K):
	pixels = im.load()
	im_c = im.copy()

	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_c.putpixel((i,j), (pixels[i,j] == 0)*255 )

	im1 = erosion(im , J)
	im2 = erosion(im_c , K)
	pixels1 = im1.load()
	pixels2 = im2.load()

	im_result = im.copy()
	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_result.putpixel((i,j), ((pixels1[i,j] == 255)&(pixels2[i,j] == 255))*255 )

	return im_result



if __name__ == '__main__':

	kernel = [[0,0] , [0,1] , [1,0] , [0,-1] , [-1,0]]
	J = [[0,0] , [0,-1] , [1,0]]
	K = [[0,1] , [-1,0] , [-1,1]]
	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	im_thre = binarize(im,128)
	im_dil = dilation(im_thre , kernel)
	im_ero = erosion(im_thre , kernel)
	im_open = opening(im_thre , kernel)
	im_close = closing(im_thre , kernel)
	im_hit_miss = hit_miss(im_thre , J , K)

	im_thre.save(benchmark+'_threshold.bmp')
	im_dil.save(benchmark+'_dilation.bmp')
	im_ero.save(benchmark+'_erosion.bmp')
	im_open.save(benchmark+'_opening.bmp')
	im_close.save(benchmark+'_closing.bmp')
	im_hit_miss.save(benchmark+'_hit_miss.bmp')