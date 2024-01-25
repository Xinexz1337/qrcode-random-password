#Create qrcode (pip install qrcode)
import qrcode
#Add to text
qr = qrcode.make('your text or link')
#the qrcode varieble is saved with the .png designation
qr.save('qrcode.png')


import random
import string
# Создаем список символов, из которых будет состоять пароль
characters = string.ascii_letters + string.digits + string.punctuation
# Генерируем пароль из 16 случайных символов
password = ''.join(random.choice(characters) for i in range(16))
# Выводим пароль на экран
print("Ваш случайный пароль: ", password)
