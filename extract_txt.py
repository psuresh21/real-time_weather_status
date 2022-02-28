import re

def ext_txt(on_time_weather,mains):
	for m in mains:
		if "span" in m:
			xs = re.sub(r'span class|=|\[A-Z][A-Z][A-Z]\d\w>','',m)
			x = xs.strip().split('>')[1]
			on_time_weather.append(x)
		else:
			m = ''
