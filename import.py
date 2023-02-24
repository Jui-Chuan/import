import random
r = random.randint(1,100)     #r是隨機數
count = 0
while True :
	count = count + 1
	number = input ('請猜一個數字:')
	number = int (number)
	if r == number :
		print ('終於答對了')
		break
	elif r < number :
		 print ('比答案大')			
	elif r > number :
		 print ('比答案小')
	print ('你已經猜了', count , '次')
