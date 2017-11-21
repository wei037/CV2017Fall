from PIL import Image

def binarize(im , threshold) :
	pixels = im.load()
	im_thre = im.copy()

	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_thre.putpixel((i,j), (pixels[i,j] >= threshold)*255 )

	return im_thre

def down_sampling(im) :
	pixels = im.load()
	im_down = Image.new('L', (66,66) , 'black')

	for i in range(64) :
		for j in range(64) :
			im_down.putpixel((i+1 , j+1) , pixels[i*8,j*8])
	return im_down

def down_sampling_fake(im) :
	pixels = im.load()
	im_down = Image.new('L', (514,514) , 'black')

	for i in range(512) :
		for j in range(512) :
			im_down.putpixel((i+1 , j+1) , pixels[i,j])
	return im_down

def _int_bor(im) :
	pixels = im.load()
	int_bor_list = []
	# b border
	# i interior 
	for j in range(1,im.size[0]-1) :
		tmp = []
		for i in range(1,im.size[1]-1) :
			if pixels[i,j] == 255 :
				this = 'i'
				for m in range(-1,2) :
					for n in range(-1,2) :
						if pixels[i+m,j+n] != 255 :
							this = 'b'
							break
				tmp.append(this)
			else :			
				tmp.append(' ')
		int_bor_list.append(tmp)
	return int_bor_list

def _marked(int_bor) :
	marked_list = []
	for i in range(len(int_bor)) :
		tmp = []
		for j in range(len(int_bor[0])) :
			if int_bor[i][j] == 'b' :
				this = 'b'
				for m in range(-1,2) :
					for n in range(-1,2) :
						if i+m < len(int_bor) and i+m >= 0 and j+n < len(int_bor[0]) and j+n >= 0 and int_bor[i+m][j+n] == 'i' :
							this = 'm'
							break
				tmp.append(this)
			else :			
				tmp.append(int_bor[i][j])
		marked_list.append(tmp)
	return marked_list

######

def _shrink(im , marked) :
	pixels = im.load()
	im_shrink = im.copy()
	# b border
	# i interior 
	for j in range(1,im.size[0]-1) :
		for i in range(1,im.size[1]-1) :
			if marked[j-1][i-1] == 'm' :
				if yokoi_pixel(im,i,j) == 1 :
					#print ('remove')
					im_shrink.putpixel((i , j) , 0)

	return im_shrink

def yokoi_pixel(im , i , j) :
	pixels = im.load()
	s  = h(255 , pixels[i,j+1] , pixels[i-1,j+1] , pixels[i-1,j])
	s += h(255 , pixels[i-1,j] , pixels[i-1,j-1] , pixels[i,j-1])
	s += h(255 , pixels[i,j-1] , pixels[i+1,j-1] , pixels[i+1,j])
	s += h(255 , pixels[i+1,j] , pixels[i+1,j+1] , pixels[i,j+1])

	return 1 if int(s) == 1 else 0

def h(b,c,d,e) :
	if b == c and b == d and b == e :
		return 0.1
	elif b != c :
		return 0.0
	else :
		return 1 



if __name__ == '__main__' :

	benchmark = 'lena'
	im = Image.open(benchmark+'.bmp').convert('L')

	im = binarize(im , 128)
	im_down = down_sampling(im)
	im_down.save(benchmark+'_down.bmp')
	while 1 :
		print ('hello')
		int_bor = _int_bor(im_down)
		'''for i in range(len(int_bor)) :
			for j in range(len(int_bor[0])) :
				print (int_bor[i][j],end="")
			print ('')'''
		marked = _marked(int_bor)
		'''for i in range(len(marked)) :
			for j in range(len(marked[0])) :
				print (marked[i][j],end="")
			print ('')'''
		im_shrink = _shrink(im_down,marked)
		pixel_before = im_down.load()
		pixel_after = im_shrink.load()
		diff = False
		for i in range(66) :
			for j in range(66) :
				if pixel_before[i,j] != pixel_after[i,j] :
					diff = True
					break
		if diff == False :
			break
		else :
			im_down = im_shrink
	im_shrink.save(benchmark+'_shrink.bmp')
