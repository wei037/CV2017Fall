import sys
from PIL import Image

if len(sys.argv) != 5 :
	print (len(sys.argv))
	print ("pseudo lena.bmp lena_r.bmp lena_g.bmp lena_b.bmp\n")
	sys.exit()

#pic = open(sys.argv[1],"rb").read()
im = Image.open(sys.argv[1])
pixels = im.load()

for i in range(im.size[0]) :
	for j in range(im.size[1]) :
		pixels[i,j] =  (tuple(255-t for t in pixels[i,j]))
im.save(sys.argv[2])
