import qrcode
from PIL import Image,ImageDraw,ImageFont
import os

os.system('cls')
print("  /$$$$$$  /$$$$$$$        /$$      /$$           /$$                          ")
print(" /$$__  $$| $$__  $$      | $$$    /$$$          | $$                          ")
print("| $$  \ $$| $$  \ $$      | $$$$  /$$$$  /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$ ")
print("| $$  | $$| $$$$$$$/      | $$ $$/$$ $$ |____  $$| $$  /$$/ /$$__  $$ /$$__  $$")
print("| $$  | $$| $$__  $$      | $$  $$$| $$  /$$$$$$$| $$$$$$/ | $$$$$$$$| $$  \__/")
print("| $$/$$ $$| $$  \ $$      | $$\  $ | $$ /$$__  $$| $$_  $$ | $$_____/| $$      ")
print("|  $$$$$$/| $$  | $$      | $$ \/  | $$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      ")
print(" \____ $$$|__/  |__/      |__/     |__/ \_______/|__/  \__/ \_______/|__/      ")
print("      \__/                                                                     ")
print("                                                                  Subwayway\n\n")

print("one QR Code? Multi QR Code? (one/multi)")
print("1. one QR")
print("2. multi QR")
option = input('==>')
os.system('cls')

def one_option():
    data = input('write data -> ')
    img = qrcode.make(data)
    img.save('./qr_out/'+'qrcode.png')

def multi_option():
    data = []
    buf = ''
    while(buf != 'END'):
        buf = input('write data(end=END) -> ')
        data.append(buf)
    data.remove('END')

    count = 0
    for i in data:
        img = qrcode.make(i)
        img.save('./qr_out/'+ i + '.png')
        count = count + 1

    for i in range(count//2):
        multi_empty_add_horizontal('./qr_out/'+data[i*2]+'.png','./qr_out/'+data[(i*2)+1]+'.png', 'merge' + str(i))

    for i in range(count//2):
        multi_empty_add_vertical('./qr_out/'+'merge0.png','./qr_out/'+'merge'+str(i+1)+'.png', 'merge0')

def multi_empty_add_horizontal(img1, img2, name):
    target1 = Image.open(img1)
    target2 = Image.open(img2)

    white = Image.new("RGB", (290,100), (255,255,255))

    white_size = white.size
    target1_size = target1.size
    target2_size = target2.size

    new_image = Image.new('RGB',(2*white_size[0], target1_size[1]+white_size[1]), (255,255,255))
    new_image.paste(target1,(0,0))
    new_image.paste(target2,(white_size[0],0))
    new_image.paste(white,(0,target1_size[1]))
    new_image.paste(white,(white_size[0],target1_size[1]))
    new_image.save('./qr_out/'+str(name) +".png","PNG")

    text1=img1.split('/')
    text2=img2.split('/')
    text1=text1[2].split('.')
    text2=text2[2].split('.')

    fontsFolder = 'C:\Windows\Fonts\gulim.ttc'
    selectedFont =ImageFont.truetype(fontsFolder,12)
    draw =ImageDraw.Draw(new_image)
    draw.text((0,315),text1[0],fill="black",font=selectedFont,align='center')
    draw.text((290,315),text2[0],fill="black",font=selectedFont,align='center')
    new_image.save('./qr_out/'+str(name) +".png","PNG")

def multi_empty_add_vertical(img1, img2, name):
    target1 = Image.open(img1)
    target2 = Image.open(img2)

    target1_size = target1.size
    target2_size = target2.size

    new_image = Image.new("RGB", (target1_size[0],target1_size[1]+target2_size[1]), (255,255,255))
    new_image.paste(target1,(0,0))
    new_image.paste(target2,(0,target1_size[1]))
    new_image.save('./qr_out/'+str(name) +".png","PNG")

if (option == '1'):
    one_option()
elif (option == '2'):
    multi_option()
