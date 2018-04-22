from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import PIL
from PIL import Image

class captcha:
    def __init__(self,image):
        self.number_list=[]
        self.image=Image.open(image)
        self.black_white_filter(self.image)
        self.list_image=self.split(self.image)
        self.address_number={'0.jpg':0,'1.jpg':1,'2.jpg':2,'3.jpg':3,'4.jpg':4,'5.jpg':5,'6.jpg':6,'7.jpg':7,'8.jpg':8,'9.jpg':9}
        for image in self.list_image:
            self.get_image(image)
        
        
        
    def pr(self):
        return self.number_list
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
    def compare(self,img1,img2):
        (width,heght)=img1.size
        total=0
        try:
            for w in range(width):
                for h in range(heght):
                    r, g, b = img1.getpixel((w,h))
                    r1, g1, b1 = img2.getpixel((w,h))
                    if r==r1 and g==g1 and b==b1:
                        total+=1
                    else:
                         a=0
        except:
            return total           
        return total
    def get_image(self,image):
        dif={}
        for address in self.address_number:
            image2=Image.open(address)
            self.black_white_filter(image2)
            a=self.compare(image,image2)
            dif[address]=a
        b=max(dif.values())
        for address in dif:
            if dif[address]==b:
                self.number_list+=[self.address_number[address]]
                break
def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    #print(size)
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']+155
    top = location['y']+50
    right = location['x'] + size['width']+155
    bottom = location['y']+ size['height']+50

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save('hamid.jpg', 'jpeg')  # saves new cropped image

driver = webdriver.Chrome()
driver.get("http://stu.iust.ac.ir/loginpage.rose")
driver.save_screenshot('captcha.png')
elem = driver.find_element_by_id("captcha_img")
get_captcha(driver,elem,'captcha.png')
def number_captcha():
    #image=Image.open('hamid.jpg')
    cap=captcha('hamid.jpg')
    capt=cap.pr()
    s=''
    for number in capt:
        s+=str(number)
    return s
numberrcaptcha=number_captcha()
fill_user=driver.find_element_by_id("j_username")
fill_user.send_keys('96521002')
fill_pass=driver.find_element_by_id("j_password")
fill_pass.send_keys('0021804125')
fill_cap=driver.find_element_by_id("captcha_input")
fill_cap.send_keys(numberrcaptcha)
Ok=driver.find_element_by_id("login_btn_submit").click()

assert "No results found." not in driver.page_source
#driver.close()


