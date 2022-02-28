import urllib.request, re
import datetime
import pprint

def copyright_intro():
	nows = datetime.datetime.now()
	c_year = nows.strftime('%Y')
	cpys_ = copyright._Printer__data.split('\n')[0]
	cpys__ = copyright._Printer__data.split('\n')[1]
	cpys__ = cpys_.split(' ')
	cpys__ = ' '.join(cpys__[0:2]) + ' '+ c_year + ' real time weather status\n| suresh pandiyan'
	cp = copyright._Printer__data.split('\n')[1]
	return ('%s\n%s' % (cpys__,cp))
	
	
def print_weather(celusis,country,country_time,status):
	country_times = country_time.split(' ')
	country_check = country_times[1]
	if country_check[0] in ['1','2','3','4','5','6','7','8','9','0']:
		print('+'+'-' * 32)
		print(' ')
		make_lc = [celusis,country,country_time,status]
		wea_t = [print('{}'.format(make).center(30)) for make in make_lc]
		print(' ')
		print(print_weather.__code__.co_consts[5])
	else:
		print("please enter valid country name")
		
