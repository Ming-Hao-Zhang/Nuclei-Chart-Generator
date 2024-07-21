# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:23:11 2022

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:38:56 2021

@author: hp
"""
"""
please read this at first
this program is writen by Minghao Zhang
I'm more than glad if this program saves your time
if you have any problems or make some improvement in this program
please contact me
my e-mail address: mhzhang@mail.bnu.edu.cn
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from math import sin, cos, pi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

path = os.getcwd()
datapath = os.path.join(path, "data.txt")
imagepath = os.path.join(path, "code.jpg")

Z,N,MS,RD,LP,FI,FU,SP,PF,UN = [],[],[],[],[],[],[],[],[],[]
with open(datapath, 'r') as c1:#1
    lines = c1.readlines()#2
    for line in lines:#3
        value = [float(s) for s in line.split()]#4
        Z.append(value[0])#5
        N.append(value[1])
        MS.append(value[2])
        RD.append(value[3])
        LP.append(value[4])
        FI.append(value[5])
        FU.append(value[6])
        SP.append(value[7])
        PF.append(value[8])
        UN.append(value[9])
y=np.array(Z)
x=np.array(N)
ms=np.array(MS)
rd=np.array(RD)
lp=np.array(LP)
fi=np.array(FI)
fu=np.array(FU)
sp=np.array(SP)
pf=np.array(PF)
un=np.array(UN)




x1=(x+5)*40+1
#y1=(120-y)*40+1
y1=(129-y)*40+1
x2=(x+6)*40+1
#y2=(121-y)*40+1
y2=(130-y)*40+1



x1=x1.tolist()
y1=y1.tolist()
x2=x2.tolist()
y2=y2.tolist()
lenrd=rd.tolist()
lenms=ms.tolist()
lenlp=lp.tolist()
lenfi=fi.tolist()
lenfu=fu.tolist()
lensp=sp.tolist()
lenpf=pf.tolist()
lenun=un.tolist()


#***************************************************************************
class MyDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        ImageDraw.ImageDraw.__init__(self, im, mode=mode)
        
    def isotriangle(self, xy, r, a=270, b=90, outline=None, fill=None):
        x, y = xy
        # a: 顶点方向，默认朝上，按x轴逆时针算是270度
        # b: 顶点角度，默认60度即是等边三角
        a, b = a*pi/180, b*pi/180   # 角度转弧度
        x1, y1 = x+cos(a)*r,     y+sin(a)*r
        x2, y2 = x+cos(pi+a-b)*r,  y+sin(pi+a-b)*r
        x3, y3 = x+cos(pi+a+b)*r,  y+sin(pi+a+b)*r
        self.polygon((x1, y1, x2, y2, x3, y3), outline=outline, fill=fill)
        
    @staticmethod
    def Draw(im, mode=None):
        try:
            return im.getdraw(mode)
        except AttributeError:
            return MyDraw(im, mode)
#***********************************************************how to paint triangle


WIDTH = 207 * 40

HEIGHT = 135 * 40

image = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255)) #255颜色代号

colors = ['cyan', 'black', 'orange', 'yellow', 'red', 'blue', 'green', 'purple']

draw = ImageDraw.Draw(image)
draw1 = MyDraw.Draw(image)


d=np.c_[x1,y1,x2,y2,lenrd,lenms,lenlp, lenfi,lenfu,lensp,lenpf,lenun]
font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 48, encoding="unic")
#print(d)
#print("d="+str(d))
draw.rectangle(( 30+6000, 30+3600, 180+6000, 180+3600), colors[1],'black')
#draw.text((120+6000, 40), str('α decay'), 'black', font)
draw.rectangle(( 30+6000, 220+3600, 180+6000, 370+3600), colors[0],'black')
#draw.text((120, 120), "β\u207a decay", 'black', font)
draw.rectangle(( 30+6000, 410+3600, 180+6000, 560+3600), colors[2],'black')
#draw.text((120, 200), "β\u207b decay", 'black', font)
draw.rectangle(( 30+6000, 600+3600, 180+6000, 750+3600), colors[3],'black')
#draw.text((120, 280), "Spontaneous fission", 'black', font)
draw.rectangle(( 30+6000, 790+3600, 180+6000, 940+3600), colors[4],'black')
draw.rectangle(( 30+6000, 980+3600, 180+6000, 1130+3600), colors[5],'black')
draw.rectangle(( 30+6000, 1170+3600, 180+6000, 1320+3600), colors[6],'black')
draw.rectangle(( 30+6000, 1360+3600, 180+6000, 1510+3600), colors[7],'black')
for num in d:
 t=np.array(num)
 
 #*********
 xl=float(t[0])
 yl=float(t[1])
 xr=float(t[2])
 yr=float(t[3])
 #******* the position of the rectangle
 
 ms=float(t[4])
 rd=float(t[5])
 lp=float(t[6])
 fi=float(t[7])
 fu=float(t[8])
 sp=float(t[9])
 pf=float(t[10])
 un=float(t[11])
 

 
 num=num.tolist()
 #count=num.count(0)
 #print(count)
 #if count == 3:
      #print(num)
 a = max(num[4:]) #最大值
 b = num.index(max(num[4:])) #最大值的位置
 draw.rectangle(( xl, yl, xr, yr), colors[b-4],'black')


          
      
      

 

     
 


 
 
 #t1=xl+al*40
 #t2=yl+al*40
 #draw.rectangle(( xl, yl, xr, yr), 'yellow','black')
 #draw1.isotriangle((t1, t2), al*40*1.3, 225, fill='green')
 
 

#image.show()
image.save('code.jpg', 'jpeg')
fig=plt.figure(dpi=150,figsize=(10,6))#分辨率，画布大小
im1=Image.open(imagepath)
im1=np.array(im1)#获得numpy对象,RGB
#print(type(im1))
#print(im1.shape)
xticks = [220, 620, 1020, 1420, 1820, 2220, 2620, 3020, 3420, 3820, 4220, 4620, 5020, 5420, 5820, 6220, 6620, 7020, 7420, 7820, 8220]
xticklabes = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200']
#yticks = [20, 100, 180, 260, 340, 420, 500, 580, 660, 740, 820, 900, 980, 1060, 1140]
#yticklabes = ['120', '118', '116', '114', '112', '110', '108', '106' , '104', '102', '100', '98', '96', '94', '92']
yticks = [380, 780, 1180, 1580, 1980, 2380, 2780,3180, 3580, 3980, 4380, 4780, 5180]
yticklabes = ['120','110', '100', '90', '80','70', '60', '50', '40', '30', '20', '10', '0']



'''
#稳定岛线
N1 = [122,125,126,126,130,130,134,134,136,136,140,140,144,144,148,148,152,152,156,156,160,160,164,164,168,168,172,172,176,176,180,180,184,184,186,186,190,190,198,198,202,202]
Z1 = [82, 82, 82, 84, 84, 86, 86, 88, 88, 90, 90, 92, 92, 94, 94, 96, 96, 98, 98, 100,100,102,102,104,104,106,106,108,108,110,110,112,112,114,114,116,116,118,118,120,120,122]
ZZ2 = np.array(Z1)
NN2 = np.array(N1)


xN2=(NN2+5)*40+1
xZ2=(129-ZZ2)*40+1
plt.plot(xN2, xZ2, 'black',linewidth=2)

#location of the island of stability
Z3 = [113,113]
N3 = [180,188]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3+5)*40+1
xZ3= (129-ZZ3)*40+1
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [114,114]
N3 = [180,188]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3+5)*40+1
xZ3= (129-ZZ3)*40+1 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [110,118]
N3 = [183.5,183.5]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3+5)*40+1
xZ3= (129-ZZ3)*40+1 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [110,118]
N3 = [184.5,184.5]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3+5)*40+1
xZ3= (129-ZZ3)*40+1 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

'''




"""
#beta稳定线
#x = np.arange(3060, 7900, 40)
#A = (x-60)/40+125
#Z = A/(1.98+0.0155*A**(2/3))
#N = A-Z
#ZZ,NN=[],[]
#print(A,Z,N)
#for zz in Z[:]:
#    ZZ.append(int(zz))
#print(ZZ)
#for nn in N[:]:
#    NN.append(int(nn))
#print(NN)
#NNN=np.array(NN)
#ZZZ=np.array(ZZ)
#xN= (NNN-125)*40+60
#xZ= -40*ZZZ+4820 
#plt.plot(xN, xZ,'black',linewidth=0.5)
N1 = [122,125,126,126,130,130,134,134,136,136,140,140,144,144,148,148,152,152,156,156,160,160,164,164,168,168,172,172,176,176,180,180,184,184,186,186,190,190,198,198,202,202]
Z1 = [82, 82, 82, 84, 84, 86, 86, 88, 88, 90, 90, 92, 92, 94, 94, 96, 96, 98, 98, 100,100,102,102,104,104,106,106,108,108,110,110,112,112,114,114,116,116,118,118,120,120,122]
ZZ2 = np.array(Z1)
NN2 = np.array(N1)
xN2= (NN2-125)*40+60
xZ2= -40*ZZ2+4820+240 
plt.plot(xN2, xZ2, 'black',linewidth=2)



#PROTON
Z2 = [92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
N2 = [116,125,120,128,123,132,127,136,131,140,135,144,139,148,143,153,147,157,151,161,155,165,160,169,164,174,168,175,172,181,176,185,181,191,187,195]
ZZ2 = np.array(Z2)

NN2 = np.array(N2)
xN2= (NN2-125)*40+60
xZ2= -40*ZZ2+4820+240 
plt.plot(xN2, xZ2, 'black',linewidth=2)

#NEUTRON
Z3 = [92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]
N3 = [228,232,234,236,240,242,244,248,250,252,256,258,260,264,266,268,272,274,276,280,282,286,288,290,294,296,298]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3-125)*40+60
xZ3= -40*ZZ3+4820+240 
plt.plot(xN3, xZ3, 'black',linewidth=0.5)

Z3 = [113.5,113.5]
N3 = [120,210]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3-125)*40+60
xZ3= -40*ZZ3+4820+240 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [114.5,114.5]
N3 = [120,210]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3-125)*40+60
xZ3= -40*ZZ3+4820+240 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [50,135]
N3 = [183.5,183.5]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3-125)*40+60
xZ3= -40*ZZ3+4820+240 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')

Z3 = [50,135]
N3 = [184.5,184.5]
ZZ3 = np.array(Z3)
NN3 = np.array(N3)
xN3= (NN3-125)*40+60
xZ3= -40*ZZ3+4820+240 
plt.plot(xN3, xZ3, 'b',linewidth=0.5,linestyle='dashed')
"""
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.text(220+6000,190+3600,"Mass Spectroscopy",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,2*190+3600,"Radioactive Decay",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,3*190+3600,"Light Particles",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,4*190+3600,"Fission",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,5*190+3600,"Fusion",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,6*190+3600,"Spallation",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,7*190+3600,"Projectile Fragmentation",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
plt.text(220+6000,8*190+3600,"Transfer/Deep Inelastic",font='Times New Roman',fontsize=9,verticalalignment="bottom",horizontalalignment="left")
#plt.text(220+6000,1710+3600,"Transfer/Deep Inelastic",fontsize=7,verticalalignment="bottom",horizontalalignment="left")



plt.xlabel('Neutron number',font='Times New Roman',fontsize=15)
plt.ylabel('Proton number',font='Times New Roman',fontsize=15)
#plt.ylabel('${E^{+}}$',fontsize=20)


ax = plt.gca() 
ax.tick_params(top=False,right=False,tick2On=False)

plt.xticks(xticks, xticklabes,font='Times New Roman', size=10, color='black')
plt.yticks(yticks, yticklabes,font='Times New Roman', size=10, color='black')
plt.imshow(im1)
plt.show()
fig.savefig('1.png')



#(x1,y1,x2,y2,Z)



    




                         



















