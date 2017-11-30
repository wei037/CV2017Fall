from PIL import Image
import numpy as np

def Gaussian(im , amp) :
	pixels = im.load()
	im_Gaussian = im.copy()

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			im_Gaussian.putpixel((i,j), int(np.clip([(pixels[i,j]+amp*np.random.normal(0.0,1.0,None))] , 0 , 255)[0]))

	return im_Gaussian

def Salt_and_Pepper (im , threshold) :
	pixels = im.load()
	im_Sp = im.copy()

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			if np.random.uniform(0.0,1.0,None) < threshold :
				im_Sp.putpixel((i,j), 0)
			elif np.random.uniform(0.0,1.0,None) > 1-threshold:
				im_Sp.putpixel((i,j), 255)
			else :
				im_Sp.putpixel((i,j), pixels[i,j])

	return im_Sp

def box_filter(im, bsize) :
	pixels = im.load()
	im_fil = im.copy()

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			avg = 0
			cnt = 0
			for m in range(-(bsize//2),bsize//2+1) :
				for n in range(-(bsize//2),bsize//2+1) :
					if i+m > 511 or j+n > 511 or i+m < 0 or j+n < 0 :
						cnt += 0
					else :
						cnt += 1
						avg += pixels[i+m,j+n]
			im_fil.putpixel((i,j),avg//cnt)
	return im_fil

def median_filter(im, bsize) :
	pixels = im.load()
	im_fil = im.copy()

	for i in range(im.size[0]) :
		for j in range(im.size[1]) :
			l = []
			cnt = 0
			for m in range(-(bsize//2),bsize//2+1) :
				for n in range(-(bsize//2),bsize//2+1) :
					if i+m > 511 or j+n > 511 or i+m < 0 or j+n < 0 :
						cnt += 0
					else :
						cnt += 1
						l.append(pixels[i+m,j+n])
			l.sort()
			im_fil.putpixel((i,j),l[len(l)//2+1])
	return im_fil

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

def SNR(im , im_n):
	im_pixel = im.load()
	im_n_pixel = im_n.load()
	N = (im.size[0]-4)*(im.size[1]-4)

	im_mean = 0
	for i in range(2,im.size[0]-2) :
		for j in range(2,im.size[1]-2) :
			im_mean += im_pixel[i,j]
	im_mean /= N

	im_n_mean = 0
	for i in range(2,im.size[0]-2) :
		for j in range(2,im.size[1]-2) :
			im_n_mean += im_n_pixel[i,j] - im_pixel[i,j]
	im_n_mean /= N

	im_vs = 0
	for i in range(2,im.size[0]-2) :
		for j in range(2,im.size[1]-2) :
			im_vs += (im_pixel[i,j] - im_mean)**2
	im_vs /= N

	im_n_vs = 0
	for i in range(2,im.size[0]-2) :
		for j in range(2,im.size[1]-2) :
			im_n_vs += (im_n_pixel[i,j] - im_pixel[i,j] - im_n_mean)**2
	im_n_vs /= N

	return 20*np.log10((im_vs**(1/2))/(im_n_vs**(1/2)))

if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	kernel =          [[-2,-1] , [-2, 0] , [-2, 1] ,
			 [-1,-2] , [-1,-1] , [-1, 0] , [-1, 1] , [-1, 2] ,
			 [ 0,-2] , [ 0,-1] , [ 0, 0] , [ 0, 1] , [ 0, 2] ,
			 [ 1,-2] , [ 1,-1] , [ 1, 0] , [ 1, 1] , [ 1, 2] ,
			 		   [ 2,-1] , [ 2, 0] , [ 2, 1]]


	#### Gaussian 10 ####
	print ('start drawing Gaussian 10...')
	im_G10      = Gaussian(im,10)
	im_G10_bf_3 = box_filter(im_G10 , 3)
	im_G10_bf_5 = box_filter(im_G10 , 5)
	im_G10_mf_3 = median_filter(im_G10 , 3)
	im_G10_mf_5 = median_filter(im_G10 , 5)
	im_G10_OpCl = closing(opening(im_G10,kernel) , kernel)
	im_G10_ClOp = opening(closing(im_G10,kernel) , kernel)
	print (SNR(im,im_G10))
	print (SNR(im,im_G10_bf_3))
	print (SNR(im,im_G10_bf_5))
	print (SNR(im,im_G10_mf_3))
	print (SNR(im,im_G10_mf_5))
	print (SNR(im,im_G10_OpCl))
	print (SNR(im,im_G10_ClOp))

	im_G10.save(benchmark+'_G10.bmp')
	im_G10_bf_3.save(benchmark+'_G10_bf_3.bmp')
	im_G10_bf_5.save(benchmark+'_G10_bf_5.bmp')
	im_G10_mf_3.save(benchmark+'_G10_mf_3.bmp')
	im_G10_mf_5.save(benchmark+'_G10_mf_5.bmp')
	im_G10_OpCl.save(benchmark+'_G10_OpCl.bmp')
	im_G10_ClOp.save(benchmark+'_G10_ClOp.bmp')
	

	#### Gaussian 30 ####
	print ('start drawing Gaussian 30...')
	im_G30      = Gaussian(im,30)
	im_G30_bf_3 = box_filter(im_G30 , 3)
	im_G30_bf_5 = box_filter(im_G30 , 5)
	im_G30_mf_3 = median_filter(im_G30 , 3)
	im_G30_mf_5 = median_filter(im_G30 , 5)
	im_G30_OpCl = closing(opening(im_G30,kernel) , kernel)
	im_G30_ClOp = opening(closing(im_G30,kernel) , kernel)
	print (SNR(im,im_G30))
	print (SNR(im,im_G30_bf_3))
	print (SNR(im,im_G30_bf_5))
	print (SNR(im,im_G30_mf_3))
	print (SNR(im,im_G30_mf_5))
	print (SNR(im,im_G30_OpCl))
	print (SNR(im,im_G30_ClOp))

	im_G30.save(benchmark+'_G30.bmp')
	im_G30_bf_3.save(benchmark+'_G30_bf_3.bmp')
	im_G30_bf_5.save(benchmark+'_G30_bf_5.bmp')
	im_G30_mf_3.save(benchmark+'_G30_mf_3.bmp')
	im_G30_mf_5.save(benchmark+'_G30_mf_5.bmp')
	im_G30_OpCl.save(benchmark+'_G30_OpCl.bmp')
	im_G30_ClOp.save(benchmark+'_G30_ClOp.bmp')

	
	#### Salt_and_Pepper 0.05 ####
	print ('start drawing Salt_and_Pepper 0.05...')
	im_SP05      = Salt_and_Pepper(im,0.05)
	im_SP05_bf_3 = box_filter(im_SP05 , 3)
	im_SP05_bf_5 = box_filter(im_SP05 , 5)
	im_SP05_mf_3 = median_filter(im_SP05 , 3)
	im_SP05_mf_5 = median_filter(im_SP05 , 5)
	im_SP05_OpCl = closing(opening(im_SP05,kernel) , kernel)
	im_SP05_ClOp = opening(closing(im_SP05,kernel) , kernel)
	print (SNR(im,im_SP05))
	print (SNR(im,im_SP05_bf_3))
	print (SNR(im,im_SP05_bf_5))
	print (SNR(im,im_SP05_mf_3))
	print (SNR(im,im_SP05_mf_5))
	print (SNR(im,im_SP05_OpCl))
	print (SNR(im,im_SP05_ClOp))

	im_SP05.save(benchmark+'_SP05.bmp')
	im_SP05_bf_3.save(benchmark+'_SP05_bf_3.bmp')
	im_SP05_bf_5.save(benchmark+'_SP05_bf_5.bmp')
	im_SP05_mf_3.save(benchmark+'_SP05_mf_3.bmp')
	im_SP05_mf_5.save(benchmark+'_SP05_mf_5.bmp')
	im_SP05_OpCl.save(benchmark+'_SP05_OpCl.bmp')
	im_SP05_ClOp.save(benchmark+'_SP05_ClOp.bmp')


	#### Salt_and_Pepper 0.10 ####
	print ('start drawing Salt_and_Pepper 0.10...')
	im_SP10      = Salt_and_Pepper(im,0.1)
	im_SP10_bf_3 = box_filter(im_SP10 , 3)
	im_SP10_bf_5 = box_filter(im_SP10 , 5)
	im_SP10_mf_3 = median_filter(im_SP10 , 3)
	im_SP10_mf_5 = median_filter(im_SP10 , 5)
	im_SP10_OpCl = closing(opening(im_SP10,kernel) , kernel)
	im_SP10_ClOp = opening(closing(im_SP10,kernel) , kernel)
	print (SNR(im,im_SP10))
	print (SNR(im,im_SP10_bf_3))
	print (SNR(im,im_SP10_bf_5))
	print (SNR(im,im_SP10_mf_3))
	print (SNR(im,im_SP10_mf_5))
	print (SNR(im,im_SP10_OpCl))
	print (SNR(im,im_SP10_ClOp))

	im_SP10.save(benchmark+'_SP10.bmp')
	im_SP10_bf_3.save(benchmark+'_SP10_bf_3.bmp')
	im_SP10_bf_5.save(benchmark+'_SP10_bf_5.bmp')
	im_SP10_mf_3.save(benchmark+'_SP10_mf_3.bmp')
	im_SP10_mf_5.save(benchmark+'_SP10_mf_5.bmp')
	im_SP10_OpCl.save(benchmark+'_SP10_OpCl.bmp')
	im_SP10_ClOp.save(benchmark+'_SP10_ClOp.bmp')

