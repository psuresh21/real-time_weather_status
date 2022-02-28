import urllib.request


def read_the_url(url_str):
	try:
		url = url_str
		usr = 'Mozilla/5.0 (Windows; U; \
			Windows NT 5.1; en-US; rv:1.9.0.7) \
			Gecko/2009021910 Firefox/3.0.7'
		my_headers = {'User-Agent':usr} 
		req = urllib.request.Request(url,None,my_headers)
		res = urllib.request.urlopen(req)
		s_data = res.read() 
		return s_data
	except:
		print("turn on your internet,then proceed again")
