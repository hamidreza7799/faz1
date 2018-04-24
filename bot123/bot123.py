from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import PIL
from PIL import Image

class captcha:
    def __init__(self, image):
        self.number_list = []
        self.image = Image.open(image)
        self.image.show()
        self.black_white_filter(self.image)
        self.list_image = self.split(self.image)
        self.address_number = {'0.jpg': 0, '1.jpg': 1, '2.jpg': 2, '3.jpg': 3, '4.jpg': 4, '5.jpg': 5, '6.jpg': 6,
                               '7.jpg': 7, '8.jpg': 8, '9.jpg': 9}
        for image in self.list_image:
            self.get_image(image)

    def pr(self):
        return self.number_list

    def black_white_filter(self, img):
        total = 0
        rgb_im = img.convert('RGB')
        (width, heght) = img.size
        for w in range(width):
            for h in range(heght):
                r, g, b = rgb_im.getpixel((w, h))
                total += r + g + b

        average = total / (width * heght)
        for w in range(width):
            for h in range(heght):
                r, g, b = rgb_im.getpixel((w, h))
                if r + g + b >= average:
                    img.putpixel((w, h), (255, 255, 255))
                else:
                    img.putpixel((w, h), (0, 0, 0))

    def split(self, img):
        (width, heght) = img.size
        image_list = []
        sensor = False
        mylist = []
        for w in range(width):
            a = 0
            for h in range(heght):
                r, g, b = img.getpixel((w, h))
                if r == 255:
                    mylist += [w]
                    a = 1
                    sensor = True
            if a == 1:
                width1 = w
            if a == 0 and sensor == True:
                mylist += [w]
                image = Image.new('RGB', (-mylist[0] + mylist[len(mylist) - 1], heght), '#122345')

                for w1 in range(mylist[0], mylist[len(mylist) - 1]):
                    for h1 in range(heght):
                        r, g, b = img.getpixel((w1, h1))
                        image.putpixel((w1 - mylist[0], h1), (r, g, b))
                image_list += [image]
                sensor = False
                mylist = []
        for image in image_list:
            image.show()
        return image_list

    def compare(self, img1, img2):
        (width, heght) = img1.size
        total = 0
        try:
            for w in range(width):
                for h in range(heght):
                    r, g, b = img1.getpixel((w, h))
                    r1, g1, b1 = img2.getpixel((w, h))
                    if r == r1 and g == g1 and b == b1:
                        total += 1
                    else:
                        a = 0
        except:
            return total
        return total

    def get_image(self, image):
        dif = {}
        for address in self.address_number:
            image2 = Image.open(address)
            self.black_white_filter(image2)
            a = self.compare(image, image2)
            dif[address] = a
        b = max(dif.values())
        for address in dif:
            if dif[address] == b:
                i = Image.open(address)
                i.show()
                self.number_list += [self.address_number[address]]
                break


def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    print(size)
    print(location)
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x'] + 3
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save('hamid.jpg', 'jpeg')  # saves new cropped image
    # image.show()


driver = webdriver.Chrome()
driver.get("http://stu.iust.ac.ir/loginpage.rose")
#driver.save_screenshot('captcha.png')
#elem = driver.find_element_by_id("captcha_img")
#get_captcha(driver, elem, 'captcha.png')


def number_captcha():
    # image=Image.open('hamid.jpg')
    cap = captcha('hamid.jpg')

    capt = cap.pr()
    s = ''
    print(capt)
    for number in capt:
        s += str(number)
    return s


#numberrcaptcha = number_captcha()
#print(numberrcaptcha)
fill_user = driver.find_element_by_id("j_username")
fill_user.send_keys('')
fill_pass = driver.find_element_by_id("j_password")
fill_pass.send_keys('')
import time
time.sleep(5)
#fill_cap = driver.find_element_by_id("captcha_input")

#fill_cap.send_keys(numberrcaptcha)


driver.find_element_by_id("login_btn_submit").click()

assert "No results found." not in driver.page_source

driver.find_element_by_xpath("//*[@id='1_div']/div[1]/a/img").click()
driver.find_element_by_xpath("//*[@id='nextWeekBtn']").click()
'''A="//*[@id='userWeekReserves.selected0']"
B="//*[@id='userWeekReserves.selected1']"
C="//*[@id='userWeekReserves.selected2']"
D="//*[@id='userWeekReserves.selected3']"
E="//*[@id='userWeekReserves.selected4']"
F="//*[@id='userWeekReserves.selected5']"
G="//*[@id='userWeekReserves.selected6']"
H="//*[@id='userWeekReserves.selected7']"
I="//*[@id='userWeekReserves.selected8']"
J="//*[@id='userWeekReserves.selected9']"
x1 = [A, B]
x2 = [C, D]
x3 = [E, F]
x4 = [G, H]
x5 = [I, J]
''
import random

i = random.randrange(1, 3)
print(i)
x11 = x1[i-1]
q = random.randrange(1, 3)
print(q)
x22 = x2[q-1]
e = random.randrange(1, 3)
print(e)
x33 = x3[e-1]
v = random.randrange(1, 3)
print(v)
x44 = x4[v-1]
t = random.randrange(1, 3)
x55 = x5[t-1]
print(t)

driver.find_element_by_xpath(x11).click()
driver.find_element_by_xpath(x22).click()
driver.find_element_by_xpath(x33).click()
driver.find_element_by_xpath(x44).click()
#driver.find_element_by_xpath("x55").click()

driver.find_element_by_xpath("//*[@id='doReservBtn']").click()'''
reservclick=driver.find_element_by_xpath("//div[contains(text(),'رزرو غذا')]").click()

food = ['غذای نوع 3 | چلو شنیتسل مرغ',' غذای نوع 1 | ماكاروني','غذای نوع 2/1 | كوفته','غذای نوع 1 | استانبولی پلو' ,
        'غذای نوع 2/1 | خوراك كتلت','غذای نوع 1 | کوکوسبزی','غذای نوع 2 | چلو کباب کوبیده','غذای نوع 1 | شویدپلو با گوشت'
    ,'غذای نوع 2 | چلو خورش قیمه سیب زمینی','غذای نوع 3 | جوجه کباب ',
        ' غذای نوع 3 | زرشك پلو با مرغ',' غذای نوع 3 | سبزي پلو با ماهي',' غذای نوع 1 | كوكو سيب زميني',' غذای نوع 2 | چلو خورش قیمه بادمجان','غذای نوع 3 | چلوکنسرو ماهی تن*']

a=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    a.append(b)
print(a)
w = food.index(a[0])
e = food.index(a[1])


if w < e :
    x = "//*[@id='userWeekReserves.selected" + str(0) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(1) + "']"
    sel = driver.find_element_by_xpath(y).click()

c=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    c.append(b)
print(c)
w = food.index(c[0])
e = food.index(c[1])


if w < e :
    x = "//*[@id='userWeekReserves.selected" + str(2) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(3) + "']"
    sel = driver.find_element_by_xpath(y).click()

d=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    d.append(b)
print(d)
w = food.index(d[0])
e = food.index(d[1])


if w < e :
    x = "//*[@id='userWeekReserves.selected" + str(4) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(5) + "']"
    sel = driver.find_element_by_xpath(y).click()

e=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    e.append(b)
print(e)
w = food.index(e[0])
r = food.index(e[1])


if w < r :
    x = "//*[@id='userWeekReserves.selected" + str(6) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(7) + "']"
    sel = driver.find_element_by_xpath(y).click()

driver.find_element_by_xpath("//*[@id='doReservBtn']").click()
driver.find_element_by_xpath("//*[@id='nextWeekBtn']").click()

food = ['غذای نوع 3 | چلو شنیتسل مرغ',' غذای نوع 1 | ماكاروني','غذای نوع 2/1 | كوفته','غذای نوع 1 | استانبولی پلو' ,
        'غذای نوع 2/1 | خوراك كتلت','غذای نوع 1 | کوکوسبزی','غذای نوع 2 | چلو کباب کوبیده','غذای نوع 1 | شویدپلو با گوشت'
    ,'غذای نوع 2 | چلو خورش قیمه سیب زمینی','غذای نوع 3 | جوجه کباب ',
        ' غذای نوع 3 | زرشك پلو با مرغ',' غذای نوع 1 | لوبیا پلو',' غذای نوع 3 | سبزي پلو با ماهي',' غذای نوع 1 | كوكو سيب زميني',' غذای نوع 2 | چلو خورش قیمه بادمجان','غذای نوع 3 | چلوکنسرو ماهی تن*']

a1=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    a1.append(b)
print(a1)
w1 = food.index(a[0])
e1 = food.index(a[1])


if w1 < e1 :
    x = "//*[@id='userWeekReserves.selected" + str(0) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(1) + "']"
    sel = driver.find_element_by_xpath(y).click()

c1=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    c1.append(b)
print(c1)
w1 = food.index(c[0])
e1 = food.index(c[1])


if w1 < e1 :
    x = "//*[@id='userWeekReserves.selected" + str(2) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(3) + "']"
    sel = driver.find_element_by_xpath(y).click()

d1=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    d1.append(b)
print(d1)
w1 = food.index(d[0])
e1 = food.index(d[1])


if w1 < e1 :
    x = "//*[@id='userWeekReserves.selected" + str(4) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(5) + "']"
    sel = driver.find_element_by_xpath(y).click()

e1=[]

for i in range(0,2):
    xpath = "//*[@id='foodNameSpan" + str(i) + "']"
    elem = driver.find_element_by_xpath(xpath)
    b = elem.text
    print(b)
    e1.append(b)
print(e)
w1 = food.index(e[0])
r1 = food.index(e[1])

if w1 < r1 :
    x = "//*[@id='userWeekReserves.selected" + str(6) + "']"
    sel = driver.find_element_by_xpath(x).click()
else:
    y = "//*[@id='userWeekReserves.selected" + str(7) + "']"
    sel = driver.find_element_by_xpath(y).click()

driver.find_element_by_xpath("//*[@id='doReservBtn']").click()

''''a2=driver.find_element_by_xpath("//*[@id='foodNameSpan1']")
a3=driver.find_element_by_xpath("//*[@id='foodNameSpan1']")
a4=driver.find_element_by_xpath("//*[@id='foodNameSpan1']")

print(a1.text)
print(a2.text)
print(a3.text)
print(a4.text)'''




# driver.close()
