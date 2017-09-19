import sys
from PIL import Image

if len(sys.argv) != 5 :
	print (len(sys.argv))
	print ("lena.bmp lena_r.bmp lena_g.bmp lena_b.bmp\n")
	sys.exit()

im = Image.open(sys.argv[1])
pixels = im.load()

im_r = Image.new('L', (im.size[0],im.size[1]), 'white')
im_g = Image.new('L', (im.size[0],im.size[1]), 'white')
im_b = Image.new('L', (im.size[0],im.size[1]), 'white')

for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		im_r.putpixel((i,j), 255 - pixels[i,j])
		im_g.putpixel((i,j), 128 )
		im_b.putpixel((i,j), pixels[i,j])


im_r.save(sys.argv[2])
im_g.save(sys.argv[3])
im_b.save(sys.argv[4])
