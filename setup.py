from intro_ques import *
from read_the_urls import read_the_url
from extract_txt import ext_txt
from weather_report import print_weather
from bytostr import bytes_to_str
import urllib.request, re

urls = f"https://www.google.com/search?channel=fs&client=ubuntu&q={mycountry}+weather" # read the urls


read_the_url(urls) # read_the_url

data = read_the_url(urls) # store as dataa
datas = str(data) # convert to str
make_as_list = datas.split('<')

o_t_w = [] # o_t_w is on time weather
ext_txt(o_t_w,make_as_list)

remove_empty_str = [o_t_w[m] for m in range(0, len(o_t_w)) if len(o_t_w[m]) != 0 and len(o_t_w[m]) != 2] # remove empty string from the weather



w__ = remove_empty_str[1:8] #weathers list w__
w_country = w__[0]; w_celusis = bytes_to_str(w__[3]); f_celusis = w_celusis; w_time = w__[4]; w_clouds = w__[5] #w__ 
w_ = [f_celusis,w_country,w_time,w_clouds] # make the all weather status as w_


print_weather(w_[0],w_[1],w_[2],w_[3]) # print out that weather status

