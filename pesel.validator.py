# -*- coding: utf-8 -*-
import sys,os
import datetime

class PeselValidate:
	__pesel=''
	def __init__(self,str1):
		self.__pesel=str1	

	def validate(self):
		psl=self.__pesel
		msc=psl[2:4]
		day=psl[4:6]
		try:
			if (int(msc) in range(81,93) and datetime.datetime(year=int(str(18)+psl[0:2]),month=int(msc)%80,day=int(day))) or (int(msc) in range(21,33) and datetime.datetime(year=int(str(20)+psl[0:2]),month=int(msc)%20,day=int(day))) or (int(msc) in range(41,53) and datetime.datetime(year=int(str(21)+psl[0:2]),month=int(msc)%40,day=int(day))) or (int(msc) in range(61,73) and datetime.datetime(year=int(str(22)+psl[0:2]),month=int(msc)%60,day=int(day))) or (int(msc) in range(1,13) and datetime.datetime(year=int(str(19)+psl[0:2]),month=int(msc),day=int(day))):
				out=(1*int(psl[0]) + 3*int(psl[1]) + 7*int(psl[2]) + 9*int(psl[3]) + 1*int(psl[4]) + 3*int(psl[5]) + 7*int(psl[6]) + 9*int(psl[7]) + 1*int(psl[8]) + 3*int(psl[9]) + 1*int(psl[10]))%10
				if out==0:
					return True
				else:
					return False
		except:
			return False

def main():
	if len(sys.argv)<2:
		print 'Usage: '+os.path.basename(sys.argv[0])+' <pesel>'
	else:
		psl=PeselValidate(sys.argv[1])
		if psl.validate()==True:
			print "Pesel jest prawidłowy"
		else:
			print "Pesel jest niepoprawny"
		# plik=open(sys.argv[1],'r')
		# for i in plik:
		# 	psl=PeselValidate(i)
		# 	if psl.validate()==False:
		# 		print "Pesel jest niepoprawny: ",
		# 		print i
		
if __name__=='__main__':
	main()