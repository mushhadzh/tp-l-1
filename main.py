print('Привет! Как вас зовут?')
name = input('>>> ')
print(str(name) + ' выберите товар из списка')
products = ['1. Шуруповерт', '2. Наушники', '3. Армянский чапалах']
price = ['3000','23000', '1000000']
for x in products:
	print(x)

summ = 0

flag = True
while flag:
	choice = input('Введите цифру нужного вам товара >>> ')
	if choice == 'exit':
		print('Сумма к оплате: '+ str(summ)+'рублей')
		flag = False
		
	elif int(choice) <= len(products):
		summ = summ + int(price[int(choice)-1])
		print('Ваш товар: '+ products[int(choice)-1])
		print('Сумма к оплате: '+ str(summ)+'рублей')
		choice = 0
		
	else:
		print('Товар не найден')
		flag = False

