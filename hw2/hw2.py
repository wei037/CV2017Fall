
# coding: utf-8

# In[76]:

from PIL import Image

#get_ipython().magic('matplotlib inline')
#import matplotlib.pyplot as plt
from collections import Counter


# In[77]:

im = Image.open('lena.bmp')
pixels = im.load()

im_div3 = Image.new('L', (im.size[0],im.size[1]), 'white')#upside-down
im_con = Image.new('L', (im.size[0],im.size[1]), 'white')#upside-down

pixel_array =  []

for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_div3.putpixel((i,j), pixels[i,j]//3)
        pixel_array.append(pixels[i,j]//3)
        
#plt.hist(pixel_array , range = (0,255))
#plt.show()


# In[79]:

ctr = Counter(pixel_array)
pixel_num = [ctr[0]]

for i in range(1,86) :
    pixel_num.append(pixel_num[i-1] + ctr[i])


# In[80]:

div_pixel = im_div3.load()
div_pixel_array = []

for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        im_con.putpixel((i,j), (255*pixel_num[div_pixel[i,j]]//pixel_num[85]))
        div_pixel_array.append(255*pixel_num[div_pixel[i,j]]//pixel_num[85])
    
im_con.save('lena_con.bmp')

#plt.hist(div_pixel_array , range = (0,255))
#plt.show()

