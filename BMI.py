height = input('請輸入身高(公尺):')
weight = input('請輸入體重(公斤):')
height = float(height)
weight = float(weight)
bmi = weight / height / height
bmi = float(bmi)
print('BMI= ' ,bmi)
#注意if 跟 elif 要在同一框架
if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi  < 24:
	print('正常範圍')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi <35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')

