from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def threshold(imgarr):
    newarr=imgarr
    balancearr=[]
    for each_row in imgarr:
        for each_pix in each_row:
            avgnum=reduce(lambda x,y:x+y,each_pix[:3])/len(each_pix[:3])
            balancearr.append(avgnum)
    balance=reduce(lambda x,y:x+y,balancearr)/len(balancearr)
    for each_row in newarr:
        for each_pix in each_row:
            if reduce(lambda x,y:x+y,each_pix[:3])/len(each_pix[:3]) >= balance:
                each_pix[0]=255
                each_pix[1]=255
                each_pix[2]=255
                each_pix[3]=255
            else:
                each_pix[0]=0
                each_pix[1]=0
                each_pix[2]=0
                each_pix[3]=255
    return newarr
    
i=Image.open(r'C:\Users\user\Documents\py\3.6\image recognition\images/numbers/0.1.png')
iar=np.array(i)
i2=Image.open(r'C:\Users\user\Documents\py\3.6\image recognition\images/numbers/y0.3.png')
iar2=np.array(i2)
i3=Image.open(r'C:\Users\user\Documents\py\3.6\image recognition\images/numbers/y0.4.png')
iar3=np.array(i3)
i4=Image.open(r'C:\Users\user\Documents\py\3.6\image recognition\images/sentdex.png')
iar4=np.array(i4)
#threshold(iar)
threshold(iar2)
threshold(iar3)
threshold(iar4)
fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)
ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
plt.show()