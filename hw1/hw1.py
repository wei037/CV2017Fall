from PIL import Image

im = Image.open('lena.bmp')
pixels = im.load()

im_u_d = Image.new('L', (im.size[0],im.size[1]), 'white')#upside-down
im_r_l = Image.new('L', (im.size[0],im.size[1]), 'white')#sight-side-left
im_d_m = Image.new('L', (im.size[0],im.size[1]), 'white')#diagonally mirrored

for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		im_u_d.putpixel((i,j), pixels[i , im.size[1]-j-1] )
		im_r_l.putpixel((i,j), pixels[im.size[0]-i-1 , j] )
		im_d_m.putpixel((i,j), pixels[j,i])

im_u_d.save('lena_u_d.bmp')
im_r_l.save('lena_r_l.bmp')
im_d_m.save('lena_d_m.bmp')