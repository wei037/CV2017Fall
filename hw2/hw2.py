from PIL import Image

im = Image.open('lena.bmp')
pixels = im.load()

###threshold##
im_thre = Image.new('1', im.size, 'white')

for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		im_thre.putpixel((i,j), (pixels[i,j] >=128)*1 )

im_thre.save('lena_thre.bmp')

###histogram###
im_hist = Image.new('L', (256,256), 'white')
pixal_array = [0]*256
for i in range(int(im.size[0])) :
	for j in range(int(im.size[1])) :
		pixal_array[pixels[i,j]] += 1	##

M = max(pixal_array)
for i in range(256) :
    pixal_array[i] = pixal_array[i]*(250)//M

for i in range(256) :
    for j in range(256-pixal_array[i],256,1) :
        im_hist.putpixel((i,j), 0 )
        
im_hist.save('hist.bmp')

###4-conn###
m =im_thre.size[0] 
n = im_thre.size[1]

labels = [0]*m*n
label_num = 1

pixels = im_thre.load()
for i in range(m) :
    for j in range(n) :
        if pixels[i,j] == 1 and labels[i*m+j] == 0 :
            if i < m-1 and pixels[i+1,j] == 1 :                
                if i < m-1 and labels[(i+1)*m+j] != 0 :
                    labels[i*m+j] = labels[(i+1)*m+j]   
                else :    
                    labels[i*m+j] = label_num
                    labels[(i+1)*m+j] = label_num  
                    label_num += 1
            if j < im_thre.size[1]-1 and pixels[i,j+1] == 0 :
                labels[i*m+j+1] = labels[i*m+j]
        elif pixels[i,j] == 1 and labels[i*m+j] != 0 :
            if i < im_thre.size[0]-1 and pixels[i+1,j] == 1 :
                labels[(i+1)*m+j] = labels[i*m+j]
            if j < im_thre.size[1]-1 and pixels[i,j+1] == 1 :
                labels[i*m+j+1] = labels[i*m+j]

done = 0
while(done == 0) :
    print (done)
    done = 1
    for i in range(m) :
        for j in range(n) :
            if i < m-1 and labels[i*m+j] != labels[(i+1)*m+j] and min(labels[i*m+j] , labels[(i+1)*m+j]) != 0:
                labels = list(map(lambda x:x if x!= max(labels[i*m+j] , labels[(i+1)*m+j]) else min(labels[i*m+j] , labels[(i+1)*m+j]),labels))
                done = 0
    for i in range(m) :
        for j in range(n) :
            if j < n-1 and labels[i*m+j] != labels[i*m+j+1] and min(labels[i*m+j] , labels[i*m+j+1]) != 0:
                labels = list(map(lambda x:x if x!= max(labels[i*m+j] , labels[i*m+j+1]) else min(labels[i*m+j] , labels[i*m+j+1]),labels))
                done = 0

ctr_list = [0]*(max(labels)+1)

index_list = []
for i in range(len(labels)):
    ctr_list[labels[i]] += 1

for i in range(len(ctr_list)) :
    if ctr_list[i] > 500 and i != 0 :
        index_list.append(i)

bd = [[m,0,m,0]]*len(index_list) #boundary
for i in range(m) :
    for j in range(n) :
        for k in range(len(index_list)) :
            if labels[i*m+j] == index_list[k] :
                bd[k] = [min(bd[k][0] , i) , max(bd[k][1] , i) , min(bd[k][2] , j) , max(bd[k][3] , j)]
                
img_con = Image.new('RGB', im.size)

rainbow = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (100, 100, 255), (127, 0, 255), (255, 0, 255)]

for i in range(int(im.size[0])) :
    for j in range(int(im.size[1])) :
        if pixels[i,j] == 1 :
            img_con.putpixel((i,j), (255,255,255))
        elif pixels[i,j] == 0 :
            img_con.putpixel((i,j), (0,0,0))

for k in range(len(bd)) :   #draw boundary
    for i in range(bd[k][2],bd[k][3]+1) :
        img_con.putpixel((bd[k][0],i),rainbow[k])
        img_con.putpixel((bd[k][1],i),rainbow[k])  
    for j in range(bd[k][0],bd[k][1]+1) :
        img_con.putpixel((j,bd[k][2]),rainbow[k])
        img_con.putpixel((j,bd[k][3]),rainbow[k])
for k in range(len(bd)) :   #draw center
    for i in range((bd[k][2]+bd[k][3])//2-5,(bd[k][2]+bd[k][3])//2+6) :
        img_con.putpixel(((bd[k][0]+bd[k][1])//2,i),rainbow[k])
    for j in range((bd[k][0]+bd[k][1])//2-5,(bd[k][0]+bd[k][1])//2+6) :
        img_con.putpixel((j,(bd[k][2]+bd[k][3])//2),rainbow[k])

img_con.save('lena_4connect.png')