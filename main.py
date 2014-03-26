import sys
sys.path.append('/home/polichism/test/')

from data import data as _data
if __name__ == "__main__":
	print _data.get_data('http://www.google.com')
