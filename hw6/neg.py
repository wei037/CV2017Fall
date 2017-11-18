from PIL import Image

def negative(im) :
	pixels = im.load()
	im_neg = im.copy()

	for i in range(int(im.size[0])) :
		for j in range(int(im.size[1])) :
			im_neg.putpixel((i,j), 255 - pixels[i,j])

	return im_neg


if __name__ == '__main__' :

	im = Image.open('Yokoi.png').convert('L')

	im = negative(im)
	im.save('Yokoi_neg.bmp')