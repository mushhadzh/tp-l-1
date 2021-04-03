print('Привет! Как вас зовут?')
name = input('>>> ')
print(str(name) + ' выберите товар из списка')
products = ['1. Шуруповерт', '2. Наушники', '3. Армянский чапалах']
price = ['3000','23000', '1000000']
for x in products:
	print(x)
choice = input('Введите цифру нужного вам товара >>> ')

flag = True
while flag:
	if int(choice) <= len(products):
		print('Ваш товар: '+ products[int(choice)-1])
		print('Сумма к оплате: '+ price[int(choice)-1]+'рублей')
		flag = False
	else:
		print('Товар не найден')
		flag = False