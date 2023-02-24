import random
start = input ('請決定隨機數字開始值:')
start = int (start)
end = input ('請決定隨機數字結束值:')
end = int (end)

r = random.randint(start,end)     #r是隨機數
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
