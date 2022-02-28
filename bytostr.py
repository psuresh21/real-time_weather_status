def bytes_to_str(mybt):
	# convert bytes to encode
	by_code = bytes(mybt,encoding='cp1252')
	z = by_code.decode('unicode-escape')
	z = z.split('Â'); z = ''.join(z);
	return z
	
