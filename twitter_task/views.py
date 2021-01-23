from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import requests,time,os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from UploadApp.models import UploadImage

def front(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        images = request.FILES.getlist('images')
        print(len(images),len(UploadImage.objects.all()))
        UploadImage.objects.all().delete()
        print(len(images), len(UploadImage.objects.all()))
        for i in range(len(images)):
            print("here",i)
            UploadImage.objects.create(pic=images[i],name="i"+str(i+1))

        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #driver = webdriver.Chrome(r"C:\Users\user\Desktop\twitter_task\twitter_task\Browsers\chromedriver.exe",chrome_options=options)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
        #driver.maximize_window()

        driver.get("https://mobile.twitter.com/login")
        time.sleep(5)

        username = '9896502571'
        password = 'Hardik@26'
        desc = '#102ndBirthday   of Shah Satnam Ji maharaj'
        print("here")

        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(
            username)
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(
            password)
        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(10)

        total_posts = len(UploadImage.objects.all())
        print("Total posts to be made",total_posts)
        print(driver.page_source)
        for i in range(total_posts):
            time.sleep(2)
            btn = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            time.sleep(3)
            btn.click()
            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(
                desc)
            time.sleep(3)

            try:
                btn = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div')
                btn.click()
            except NoSuchElementException:
                pass


            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[1]/input').send_keys(
                'C://Users/user/Desktop/twitter_task/'+str(UploadImage.objects.filter(name='i'+str(i+1))[0].pic))
            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]').click()
            time.sleep(8)

        driver.close()
        UploadImage.objects.all().delete()


    return render(request,'front.html')

#.\newenv\Scripts\activate