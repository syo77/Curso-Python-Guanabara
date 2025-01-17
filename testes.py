# x = int(input("Digite um número: "))
# y = int(input("Digite outro número: "))
# z = x + y

import calendar
print(calendar.month(2024, 11))
calendario = calendar.TextCalendar()
print(calendario.formatyear(2024))

import qrcode

link = input("Insira o link para gerar o código: ")
qr = qrcode.QRCode(version=1, box_size=10, border=1)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qr.png')
print("QR Code gerado com sucesso e salvo como 'qr.png'")

print()
