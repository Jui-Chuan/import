import random
r = random.randint(1,100)     #r是隨機數
while True :
	number = input ('請猜一個數字:')
	number = int (number)
	if r == number :
		print ('終於答對了')
		break
	elif r < number :
		 print ('比答案大')
					
	elif r > number :
		 print ('比答案小')
			
