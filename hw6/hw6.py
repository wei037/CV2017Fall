from PIL import Image

def down_sampling(im) :
	pixels = im.load()
	im_down = Image.new('L', (64,64) , 'black')

	for i in range(0 , im.size[0] , 8) :
		for j in range(0 , im.size[1] , 8) :
			im_down.putpixel((int(i/8) , int(j/8)) , pixels[i,j])
	return im_down

if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	im_down = down_sampling(im)
	im_down.save(benchmark+'_down.bmp')