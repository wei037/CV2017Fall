from PIL import Image
from collections import Counter

im = Image.open('lena.bmp')
pixels = im.load()

im_div3 = Image.new('L', (im.size[0],im.size[1]), 'white')#1/3
im_con = Image.new('L', (im.size[0],im.size[1]), 'white')#contrast

pixel_array =  []

for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_div3.putpixel((i,j), pixels[i,j]//3)
        pixel_array.append(pixels[i,j]//3)

ctr = Counter(pixel_array)
pixel_num = [ctr[0]]

for i in range(1,86) :
    pixel_num.append(pixel_num[i-1] + ctr[i])

div_pixel = im_div3.load()
div_new_pixel = []

for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_con.putpixel((i,j), (255*pixel_num[div_pixel[i,j]]//pixel_num[85]))
        div_new_pixel.append(255*pixel_num[div_pixel[i,j]]//pixel_num[85])

im_con.save('lena_con.bmp')

im_hist = Image.new('L', (256,256), 'white')

div_pixel_array = [0]*256
for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		div_pixel_array[div_new_pixel[i*im.size[0]+j]] += 1	##

M = max(div_pixel_array)
for i in range(256) :
    div_pixel_array[i] = div_pixel_array[i]*(250)//M

for i in range(256) :
    for j in range(256-div_pixel_array[i],256,1) :
        im_hist.putpixel((i,j), 0 )
        
im_hist.save('hist.bmp')

