import sys

class PeselValidate:
	__pesel=''
	def __init__(self,str1):
		__pesel=str1

	def validate():
		pass


def main():
	if len(sys.argv)<2:
		print 'Usage: '+sys.argv[0]+' <pesel>'
	else:
		print sys.argv[1]

if __name__=='__main__':
	main()
