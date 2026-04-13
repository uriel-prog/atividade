
cliente=input('qual seu nome?  ')
compra=float(input('qual foi o valor da compra?  '))
pi= 0.10
debi= 0.05
cre=0
desconto=0.05
pagamento= int(input("qual forma de pagamento? '1' pix; '2' débito; '3' crédito  "))
pix=compra -(compra * pi )
débito=compra -(compra * debi)
crédito=compra - (compra *cre )
pix2=compra -(compra * pi * desconto )
débito2=compra -(compra * debi * desconto)
crédito2=compra - (compra *cre *desconto )



if pagamento==1:
    print('custará',pix, 'R$, se for no pix')

elif pagamento==2:
    print(débito)
elif pagamento==3:
    print(crédito)

