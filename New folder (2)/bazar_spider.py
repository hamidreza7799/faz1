#!/usr/bin/env python
# -*- coding: utf-8 -*-
# _*_ coding: utf-8 _*_
import scrapy
import sqlite3
from scrapy.http import HtmlResponse                        
def replace(string):
    m=''
    count=0
    while string[count]==' ' or string[count]=='\n':
        count+=1
    while string[count]!='\n':
        m+=string[count]
        count+=1
    return m                
             
class BAZAARSpider(scrapy.Spider):
    name = "bazaar"
    start_urls = ['https://cafebazaar.ir/cat/?l=en']
    def parse(self, response):
        a='cafebazaar.ir/cat/?l=en'
        a=a.split('/')
        a.remove(a[2])
        for li in response.xpath("/html/body/div/div[1]/ul/li"):
            title=li.xpath("a/text()").extract()
            link=li.xpath("a/@href").extract()
            link=link[0].split('/')
            link=a+[link[2]]+[link[3]]
            link='/'.join(link)
            link='https://'+link
            yield scrapy.Request(url=link,callback=self.parse2)
    def parse2(self,response):
        link=response.url.split('/')
        link.remove(link[-1])
        link='https://'+link[2]
        for div in response.xpath("/html/body/div[1]/div[4]/div[2]/div"):
            new_link=div.xpath("div/div[1]/span[2]/a/@href").extract()
            new_link=new_link[0].split('/')
            new_link=link+'/'+new_link[1]+'/'+new_link[2]+'/'+'?l=en'
            yield scrapy.Request(url=new_link,callback=self.parse3)
    def parse3(self,response):
        for div in response.xpath("/html/body/div[1]/div[4]/div[2]/div[4]/div"):
            link=div.xpath("div/a/@href").extract()
            link=link[0].split('/')
            new_link='https://cafebazaar.ir/'+link[1]+'/'+link[2]+'/'+'?l=en'
            yield scrapy.Request(url=new_link,callback=self.parse4)
    def parse4(self,response):
        conn=sqlite3.connect('test.db')
        name=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div/h1/text()").extract()
        name=replace(name[0])
        cate=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[1]/span[2]/a/span/text()").extract()
        install=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/span[2]/span/text()").extract()
        size=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/span[2]/text()").extract()
        size=replace(size[0])
        version=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[4]/span[2]/text()").extract()
        version=replace(version[0])
        try:
            shamad=response.xpath("/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[5]/span[2]/a/text()").extract()
            shamad=replace(shamad[0])
        except:
            a=1
        sql = "insert into BAZAAR values (NULL,?, ?, ?, ?,?,?)"
        a=(str(name),str(cate),str(install),str(size),str(version),str(shamad))
        conn.execute(sql,a)
        conn.commit()
        conn.close()
       
