from PIL import Image

def binarize(im , threshold) :
	pixels = im.load()
	im_thre = im.copy()

	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_thre.putpixel((i,j), (pixels[i,j] > threshold)*255 )

	return im_thre

def down_sampling(im) :
	pixels = im.load()
	im_down = Image.new('L', (64,64) , 'black')

	for i in range(0 , im.size[0] , 8) :
		for j in range(0 , im.size[1] , 8) :
			im_down.putpixel((int(i/8) , int(j/8)) , pixels[i,j])
	return im_down

def yokoi(im) :
	pixels = im.load()

	yokoi_list = []
	for j in range(1,im.size[0]-1) :
		tmp = []
		for i in range(1,im.size[1]-1) :
			if pixels[i,j] == 255 :
				s = 0
				s += h(255 , pixels[i,j+1] , pixels[i-1,j+1] , pixels[i-1,j])
				s += h(255 , pixels[i-1,j] , pixels[i-1,j-1] , pixels[i,j-1])
				s += h(255 , pixels[i,j-1] , pixels[i+1,j-1] , pixels[i+1,j])
				s += h(255 , pixels[i+1,j] , pixels[i+1,j+1] , pixels[i,j+1])
				if s == 0.4 :
					tmp.append(5)
				else :
					tmp.append(int(s))
			else :			
				tmp.append(' ')
		yokoi_list.append(tmp)

	return yokoi_list


def h(b,c,d,e) :
	if b == c and b == d and b == e :
		return 0.1
	elif b != c :
		return 0
	else :
		return 1 

if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	im = binarize(im , 128)
	im_down = down_sampling(im)
	im_down.save(benchmark+'_down.bmp')
	yokoi = yokoi(im_down)
	#print (len(yokoi[0]))
	for i in range(len(yokoi)) :
		for j in range(len(yokoi[0])) :
			print (yokoi[i][j],end="")
		print ('')