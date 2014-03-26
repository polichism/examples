import urllib2

def get_data(url):
	f = None
	try:
		f = urllib2.urlopen(url)
	except urllib2.URLError as urlerror:
		print "URLError ({0}): {1}".format(urlerror.errno, urlerror.strerror)
	except urllib2.HTTPError as httperror:
		print "HTTPError ({0}): {1}".format(httperror.errno, httperror.strerror)
	except ValueError:
		pass
		data = None
	try:
		data = f.read()
	except AttributeError:
		pass
	return data
