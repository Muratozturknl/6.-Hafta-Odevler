##ODEV 1: Sayi Tahmin
##		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
##		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
##		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi
##		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin
##		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
##		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
##		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
##
##		Ornek:
##
##			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece
##			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz.
##			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
##
##			 Pc'nin tahmini = 89
##			 Kullanicinin inputu = -
##			 Pc'nin tahmini = 45
##			 Kullanicinin inputu = +
##			 Pc'nin tahmini = 56
##			 Kullanicinin inputu = "Enter"

########################################################################################################################

print('!!-Let the pc find your number-!!\n'
      'Please keep a number between 0-100 in your mind\n'
      'if pc guess a number higher than yours please type \'-\'\n'
      'if pc guess a number lower than yours please type  \'+\'\n'
      'if pc guess your please type  \'r\' or \'R\' ', sep="")

uplimit = 101
downlimit = 0
guess = 50
guesscount = 0
user = ""

while (user != "r" or "R"):
    user = input("~Can your number be " + "«"+str(guess)+"» ?\n ")
    guesscount += 1
    if (user == "-"):  # Is high try smaller
        uplimit = guess
        guess = int((uplimit + downlimit) / 2)
    elif (user == "+"):  # Is low try higher
        downlimit = guess
        guess = int((uplimit + downlimit) / 2)
    elif (user == "r" or "R"):
        break
    else:
        print("Please use only given symbols...")
print("Yeap, your number guessed in", guesscount, "times. See you soon!")
