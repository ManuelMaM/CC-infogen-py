import datetime
from random import Random


class Cgen(object):

	generator = None

	def __init__(self):
		self.generator = Random()
		self.generator.seed()


	def gen(self, quant : int,length = 16, cc_number = 0) -> list:

		def completnum(ccnumber, length):
		
			mby2 = []
			remaining_num = []
			new_num = ''
			y = 0

			while len(ccnumber) < (length - 1):#generate random digits
					digit = int(self.generator.choice(range(0, 10)))
					ccnumber.append(digit)

			# get numbers to multiply by 2
			for i in ccnumber[0:length:2]:

				i *= 2
				if len(str(i)) == 2:# check if the multiplied number is a two digit number
				
					for x in str(i):        
						y += int(str(x))
					i = y
				
				mby2.append(i)
				y = 0

			for i in ccnumber[1:length-1:2]:# extract remaining numbers
				remaining_num.append(i)

			# get the last digit / luhns algorithm
			last_digit = ((sum(mby2) + sum(remaining_num)) * 9) % 10

			for i in ccnumber:
				new_num += str(i)

			return new_num + str(last_digit)

		def compledate():

			today = datetime.date.today()
			yeartd = int(today.year)
			month = int(today.month)

			ext =''
			
			while True:
				temp_year = self.generator.choice(range(yeartd, 2040))
				temp_mon = self.generator.choice(range(1,12))

				if yeartd == temp_year and month > temp_mon:
					continue
				ext += f'{str(temp_mon).zfill(2)}/{temp_year}'
				return ext

		def gen_nums(cc_number, length, quant):
			#generate carn numbers
			numbers = []

			while len(numbers) < quant:

				a = cc_number.copy()
				cc = completnum(a, length)
				numbers.append(cc)


			return numbers

		def gen_scs(quant):
			#generate security code
			scs = []

			while len(scs) < quant:
				sc = str(self.generator.choice(range(100, 999)))
				scs.append(sc)

			return scs

		def gen_exts(quant):

			exts = []

			while len(exts) < quant:

				ext = compledate()

				exts.append(ext)		

			return exts

		if length < 6:
			return 0

		if not cc_number:
			cc_number = self.generator.choice(range(100000,999999))

		cc_number_list = []

		for i in str(cc_number):
			cc_number_list.append(int(i))

		numbers = gen_nums(cc_number_list, length, quant)
		scs = gen_scs(quant)
		exts = gen_exts(quant)

		return [numbers,scs,exts]
