from PIL import Image

im = Image.open('lena.bmp')
pixels = im.load()

im_div3 = Image.new('L', (im.size[0],im.size[1]), 'white')#1/3
im_con = Image.new('L', (im.size[0],im.size[1]), 'white')#contrast

pixel_array =  []

####divide by 3####
for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_div3.putpixel((i,j), pixels[i,j]//3)
        pixel_array.append(pixels[i,j]//3)

####calculate pixel numbers###
ctr = [0]*256
for i in range(len(pixel_array)) :
    ctr[pixel_array[i]] += 1
pixel_num = [ctr[0]]

for i in range(1,256) :
    pixel_num.append(pixel_num[i-1] + ctr[i])

div_pixel = im_div3.load()
div_new_pixel = []

####histogram equalization####
for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_con.putpixel((i,j), (255*pixel_num[div_pixel[i,j]]//pixel_num[255]))
        div_new_pixel.append(255*pixel_num[div_pixel[i,j]]//pixel_num[255])

im_con.save('lena_con.bmp')

####create histogram####
im_hist = Image.new('L', (256,256), 'white')

div_pixel_array = [0]*256
for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		div_pixel_array[div_new_pixel[i*im.size[0]+j]] += 1	

M = max(div_pixel_array)
for i in range(256) :
    div_pixel_array[i] = div_pixel_array[i]*(250)//M

for i in range(256) :
    for j in range(256-div_pixel_array[i],256,1) :
        im_hist.putpixel((i,j), 0 )

im_hist.save('hist.bmp')