import qrcode

img = qrcode.make('https://keiichimorimoto.github.io/AR_test/')
img.save('img/simple_qrcode.png')
