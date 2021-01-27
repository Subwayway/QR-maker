import qrcode
from PIL import Image,ImageDraw,ImageFont
import os
import time

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

print("One QR Code? Multi QR Code? (one/multi)")
print("1. One QR")
print("2. Multi QR")
print("3. Read from <.txt> file")
option = input('==>')
os.system('cls')

out_path='./qr_out/'+time.strftime('%y%m%d-%H%M', time.localtime(time.time()))

def createFolder():
    try:
        if not os.path.exists(out_path):
            os.makedirs(out_path + '/one_qr')
            os.makedirs(out_path + '/multi_qr')
    except OSError:
        pass

def one_option():
    data = input('write data -> ')
    img = qrcode.make(data)
    img.save(out_path+'/one_qr/'+data+'.png')
    print("# "+data+" make QR")

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
        img.save(out_path+'/one_qr/'+ i + '.png')
        print("# "+i+" make QR")
        count = count + 1

    merge_count=0
    for i in range(count//2):
        multi_add_horizontal(out_path+'/one_qr/'+data[i*2]+'.png',out_path+'/one_qr/'+data[(i*2)+1]+'.png', 'merge' + str(i))
        merge_count=i

    for i in range(merge_count):
        multi_add_vertical(out_path+'/multi_qr/'+'merge0.png',out_path+'/multi_qr/'+'merge'+str(i+1)+'.png', 'merge0')

    if(((merge_count+1)*2)<count):
        multi_add_empty_horizontal(out_path+'/one_qr/'+data[count-1]+'.png', 'merge_empty')
        multi_add_vertical(out_path+'/multi_qr/'+'merge0.png',out_path+'/multi_qr/'+'merge_empty.png', 'merge0')

def multi_add_horizontal(img1, img2, name):
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
    new_image.save(out_path+'/multi_qr/'+str(name) +".png","PNG")

    text1=img1.split('/')
    text2=img2.split('/')
    text1=text1[4].split('.')
    text2=text2[4].split('.')

    fontsFolder = 'C:\Windows\Fonts\gulim.ttc'
    selectedFont =ImageFont.truetype(fontsFolder,20)
    draw =ImageDraw.Draw(new_image)
    draw.text((0,315),text1[0],fill="black",font=selectedFont,align='center')
    draw.text((290,315),text2[0],fill="black",font=selectedFont,align='center')
    new_image.save(out_path+'/multi_qr/'+str(name) +".png","PNG")

def multi_add_empty_horizontal(img1, name):
    target1 = Image.open(img1)
    target2 = Image.new("RGB", (290,290), (255,255,255))

    white = Image.new("RGB", (290,100), (255,255,255))

    white_size = white.size
    target1_size = target1.size
    target2_size = target2.size

    new_image = Image.new('RGB',(2*white_size[0], target1_size[1]+white_size[1]), (255,255,255))
    new_image.paste(target1,(0,0))
    new_image.paste(target2,(white_size[0],0))
    new_image.paste(white,(0,target1_size[1]))
    new_image.paste(white,(white_size[0],target1_size[1]))
    new_image.save(out_path+'/multi_qr/'+str(name) +".png","PNG")

    text1=img1.split('/')
    text1=text1[4].split('.')
    text2=' '

    fontsFolder = 'C:\Windows\Fonts\gulim.ttc'
    selectedFont =ImageFont.truetype(fontsFolder,20)
    draw =ImageDraw.Draw(new_image)
    draw.text((0,315),text1[0],fill="black",font=selectedFont,align='center')
    draw.text((290,315),text2[0],fill="black",font=selectedFont,align='center')
    new_image.save(out_path+'/multi_qr/'+str(name) +".png","PNG")

def multi_add_vertical(img1, img2, name):
    target1 = Image.open(img1)
    target2 = Image.open(img2)

    target1_size = target1.size
    target2_size = target2.size

    new_image = Image.new("RGB", (target1_size[0],target1_size[1]+target2_size[1]), (255,255,255))
    new_image.paste(target1,(0,0))
    new_image.paste(target2,(0,target1_size[1]))
    new_image.save(out_path+'/multi_qr/'+str(name) +".png","PNG")

def read_option():
    os.system('cls')
    file_name = input('Write file name(without .txt) ==>')
    with open("./"+file_name+".txt", mode="r") as file:
        data = []

        for i in file:
            data.append(i.rstrip('\n'))

    count = 0
    for i in data:
        img = qrcode.make(i)
        img.save(out_path+'/one_qr/'+ i + '.png')
        print("# "+i+" make QR")
        count = count + 1

    merge_count=0
    for i in range(count//2):
        multi_add_horizontal(out_path+'/one_qr/'+data[i*2]+'.png',out_path+'/one_qr/'+data[(i*2)+1]+'.png', 'merge' + str(i))
        merge_count=i

    for i in range(merge_count):
        multi_add_vertical(out_path+'/multi_qr/'+'merge0.png',out_path+'/multi_qr/'+'merge'+str(i+1)+'.png', 'merge0')

    if(((merge_count+1)*2)<count):
        multi_add_empty_horizontal(out_path+'/one_qr/'+data[count-1]+'.png', 'merge_empty')
        multi_add_vertical(out_path+'/multi_qr/'+'merge0.png',out_path+'/multi_qr/'+'merge_empty.png', 'merge0')

createFolder()
if (option == '1'):
    one_option()
elif (option == '2'):
    multi_option()
elif (option == '3'):
    read_option()
