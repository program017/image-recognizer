from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import copy
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

def creating_examples():
    examplefile=open('database.txt','w')
    for number in range(0,10):
        for versions in range(1,10):
            path=r'C:\Users\user\Documents\py\3.6\image recognition\images\numbers/'+str(number)+'.'+str(versions)+'.png'
            img=Image.open(path)
            imgar=np.array(img)
            listed=str(imgar.tolist())
            linetowrite=str(number)+'::'+listed+'\n'
            examplefile.write(linetowrite)
    return
            
def matching(path):
    matchedarr=[]
    database1=open('database.txt','r').read()
    database=database1.split('\n')
    givenimg=Image.open(path)
    iar=np.array(givenimg)
    iarv2=copy.deepcopy(iar)
    threshold(iar)
    iarl=iar.tolist()
    iarlist=str(iarl)
    for eachpart in database:
        if len(eachpart) > 3:
            eachpartsplit=eachpart.split('::')
            number=eachpartsplit[0]
            cmplist=eachpartsplit[1]
            cmppart=cmplist.split('],')
            tocmp=iarlist.split('],')
            x=0
            while x < len(cmppart):
                if cmppart[x]==tocmp[x]:
                    matchedarr.append(int(number))
                x +=1
    #print matchedarr
    x=Counter(matchedarr)
    listn=[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]]
    number=max(listn)
    check=listn.index(number)
    graphx=[]
    graphy=[]
    for each in x:
        graphx.append(each)
        graphy.append(x[each])
    #print graphx
    #print graphy
    fig=plt.figure()
    ax1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2=plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)
    ax1.imshow(iarv2)
    ax2.bar(graphx,graphy,color='g',align='center')
    plt.ylim(400)
    xloc=plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()
    database=open('database.txt','a')
    database.write(str(check)+'::'+str(iarv2.tolist())+'\n')
    database.close()
    return

def main():
    i=0
    while True:
        temp=raw_input('Want to run image recognition. Enter Y/N: ')
        if temp =='N' or temp =='n':
            return
        else:
            path=raw_input('Enter the path of fig to be matched: ')
            if i==0:
                creating_examples()
            i +=1
            matching(path)
    
    return


if __name__=='__main__':
    main()
