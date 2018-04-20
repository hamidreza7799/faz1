import PIL
from PIL import Image

class captcha:
    def __init__(self,image):
        self.number_list=[]
        self.image=Image.open(image)
        self.black_white_filter(self.image)
        self.list_image=self.split(self.image)
        #print(self.list_image)
        self.address_number={'0.jpg':0,'1.jpg':1,'2.jpg':2,'3.jpg':3,'4.jpg':4,'5.jpg':5,
                             '6.jpg':6,'7.jpg':7,'8.jpg':8,'9.jpg':9}
        for image in self.list_image:
            self.get_image(image)
        
        
        print(self.number_list) 
    def black_white_filter(self,img):
        total=0
        rgb_im = img.convert('RGB')
        (width,heght)=img.size
        for w in range(width):
            for h in range(heght):
                r, g, b = rgb_im.getpixel((w,h))
                total+=r+g+b
        
        average=total/(width*heght)
        for w in range(width):
            for h in range(heght):
                r, g, b = rgb_im.getpixel((w,h))
                if r+g+b>=average:
                    img.putpixel((w,h),(255,255,255))
                else:
                    img.putpixel((w,h),(0,0,0))
    def split(self,img):
        (width,heght)=img.size
        image_list=[]
        sensor=False
        mylist=[]
        for w in range(width):
            a=0
            for h in range(heght):
                r, g, b = img.getpixel((w,h))
                if r==255:
                    mylist+=[w]
                    a=1
                    sensor=True
            if a==1:
                width1=w
            if a==0 and sensor==True:
                mylist+=[w]
                image=Image.new('RGB',(-mylist[0]+mylist[len(mylist)-1],heght),'#122345')
                
                for w1 in range(mylist[0],mylist[len(mylist)-1]):
                    for h1 in range(heght):
                        r, g, b = img.getpixel((w1,h1))
                        image.putpixel((w1-mylist[0],h1),(r,g,b))
                image_list+=[image]
                sensor=False
                mylist=[]
                
        return image_list
#a=split(img)
    def compare(self,img1,img2):
        (width,heght)=img1.size
        for w in range(width):
            for h in range(heght):
                r, g, b = img1.getpixel((w,h))
                r1, g1, b1 = img2.getpixel((w,h))
                if r==r1 and g==g1 and b==b1:
                    a=1
                else:
                    a=0
                    return 0
        return 1
    def get_image(self,image):
        for address in self.address_number:
            image2=Image.open(address)
            self.black_white_filter(image2)
            a=self.compare(image,image2)
            if a==1:
                self.number_list+=[self.address_number[address]]
                break
                
image=Image.open('captcha.jpg')
captcha=captcha('captcha.jpg')
