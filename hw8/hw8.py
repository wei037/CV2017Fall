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
			val = np.random.uniform(0.0,1.0,None)
			if val < threshold :
				im_Sp.putpixel((i,j), 0)
			elif val > 1-threshold:
				im_Sp.putpixel((i,j), 255)
			else :
				im_Sp.putpixel((i,j), pixels[i,j])

	return im_Sp

def box_filter(im, bsize) :
	pixels = im.load()
	im_fil = im.copy()

	print (im.size)

	for i in range(bsize//2,im.size[0]-bsize//2) :
		for j in range(bsize//2,im.size[1]-bsize//2) :
			avg = 0
			for m in range(-(bsize//2),bsize//2+1) :
				for n in range(-(bsize//2),bsize//2+1) :
					avg += pixels[i+m,j+n]
			im_fil.putpixel((i,j),avg//(bsize*bsize))
	return im_fil

def median_filter(im, bsize) :
	pixels = im.load()
	im_fil = im.copy()

	print (im.size)

	for i in range(bsize//2,im.size[0]-bsize//2) :
		for j in range(bsize//2,im.size[1]-bsize//2) :
			l = []
			for m in range(-(bsize//2),bsize//2+1) :
				for n in range(-(bsize//2),bsize//2+1) :
					l.append(pixels[i+m,j+n])
			l.sort()
			im_fil.putpixel((i,j),l[len(l)//2+1])
	return im_fil

if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	#im_Gaussian_10 = Gaussian(im,10)
	#im_Gaussian_30 = Gaussian(im,30)
	#im_Salt_and_Paper_05 = Salt_and_Pepper(im,0.05)
	#im_Salt_and_Paper_10 = Salt_and_Pepper(im,0.10)
	#im_Gaussian_10.save(benchmark+'_Gaussian_10.bmp')
	#im_Gaussian_30.save(benchmark+'_Gaussian_30.bmp')
	#im_Salt_and_Paper_05.save(benchmark+'_Salt_and_Paper_05.bmp')
	#im_Salt_and_Paper_10.save(benchmark+'_Salt_and_Paper_10.bmp')
	im_Gaussian_10 = Image.open('lena_Gaussian_10.bmp')
	im_Gaussian_30 = Image.open('lena_Gaussian_30.bmp')
	im_Salt_and_Paper_05 = Image.open('lena_Salt_and_Paper_05.bmp')
	im_Salt_and_Paper_10 = Image.open('lena_Salt_and_Paper_10.bmp')

	#im_box_filter_3_G10 = box_filter(im_Gaussian_10 , 3)
	#im_box_filter_3_G30 = box_filter(im_Gaussian_30 , 3)	
	#im_box_filter_5_G10 = box_filter(im_Gaussian_10 , 5)
	#im_box_filter_5_G30 = box_filter(im_Gaussian_30 , 5)
	#im_box_filter_3_G10.save(benchmark+'_box_filter_3_G10.bmp')
	#im_box_filter_3_G30.save(benchmark+'_box_filter_3_G30.bmp')	
	#im_box_filter_5_G10.save(benchmark+'_box_filter_5_G10.bmp')	
	#im_box_filter_5_G30.save(benchmark+'_box_filter_5_G30.bmp')
    ###################
	#im_box_filter_3_SP05 = box_filter(im_Salt_and_Paper_05 , 3)
	#im_box_filter_3_SP10 = box_filter(im_Salt_and_Paper_10 , 3)	
	#im_box_filter_5_SP05 = box_filter(im_Salt_and_Paper_05 , 5)
	#im_box_filter_5_SP10 = box_filter(im_Salt_and_Paper_10 , 5)
	#im_box_filter_3_SP05.save(benchmark+'_box_filter_3_SP05.bmp')
	#im_box_filter_3_SP10.save(benchmark+'_box_filter_3_SP10.bmp')	
	#im_box_filter_5_SP05.save(benchmark+'_box_filter_5_SP05.bmp')	
	#im_box_filter_5_SP10.save(benchmark+'_box_filter_5_SP10.bmp')

	#im_median_filter_3_G10 = median_filter(im_Gaussian_10 , 3)
	#im_median_filter_3_G30 = median_filter(im_Gaussian_30 , 3)	
	#im_median_filter_5_G10 = median_filter(im_Gaussian_10 , 5)
	#im_median_filter_5_G30 = median_filter(im_Gaussian_30 , 5)
	#im_median_filter_3_G10.save(benchmark+'_median_filter_3_G10.bmp')
	#im_median_filter_3_G30.save(benchmark+'_median_filter_3_G30.bmp')	
	#im_median_filter_5_G10.save(benchmark+'_median_filter_5_G10.bmp')	
	#im_median_filter_5_G30.save(benchmark+'_median_filter_5_G30.bmp')
    ###################
	#im_median_filter_3_SP05 = median_filter(im_Salt_and_Paper_05 , 3)
	#im_median_filter_3_SP10 = median_filter(im_Salt_and_Paper_10 , 3)	
	#im_median_filter_5_SP05 = median_filter(im_Salt_and_Paper_05 , 5)
	#im_median_filter_5_SP10 = median_filter(im_Salt_and_Paper_10 , 5)
	#im_median_filter_3_SP05.save(benchmark+'_median_filter_3_SP05.bmp')
	#im_median_filter_3_SP10.save(benchmark+'_median_filter_3_SP10.bmp')	
	#im_median_filter_5_SP05.save(benchmark+'_median_filter_5_SP05.bmp')	
	#im_median_filter_5_SP10.save(benchmark+'_median_filter_5_SP10.bmp')

	##-8 (4*OpenClo + 4* CloOpen)


