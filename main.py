from pygame import mixer
from pynput import keyboard

mixer.pre_init(buffer=256)
mixer.init()
mixer.set_num_channels(32)
PLUSTEN = mixer.Sound("mp3/PLUSTEN.mp3") # 0
TWENTYONE = mixer.Sound("mp3/TWENTYONE.mp3") # 1
NOOTNOOT = mixer.Sound("mp3/NOOTNOOT.mp3") # 2
SWAWS = mixer.Sound("mp3/SWAWS.mp3") # 3
SAMSUNG = mixer.Sound("mp3/SAMSUNG.mp3") # 4
BEANS = mixer.Sound("mp3/BEANS.mp3") # 5
THWOMP = mixer.Sound("mp3/THWONP.mp3") # 6
CAVE = mixer.Sound("mp3/CAVE.mp3") # 7
ALARM = mixer.Sound("mp3/ALARM.mp3") # 8
WHATSNINE = mixer.Sound("mp3/WHATSNINE.mp3") # 9
VINEBOOM = mixer.Sound("mp3/VINEBOOM.mp3") # return
NYAGA = mixer.Sound("mp3/NYAGA.mp3") # a
SLEEP = mixer.Sound("mp3/SLEEP.mp3") # z
SPEEN = mixer.Sound("mp3/SPEEN.mp3") # e
OOF = mixer.Sound("mp3/OOF.mp3") # r
TACOBELL = mixer.Sound("mp3/TACOBELL.mp3") # t
YODA = mixer.Sound("mp3/YODA.mp3") # y
AMOGUS = mixer.Sound("mp3/AMOGUS.mp3") # u
SCOOB = mixer.Sound("mp3/SCOOB.mp3") # i
OHMYGOD = mixer.Sound("mp3/OHMYGOD.mp3") # o
PIZZATIME = mixer.Sound("mp3/PIZZATIME.mp3") # p
THICC = mixer.Sound("mp3/THICC.mp3") # q
SUS = mixer.Sound("mp3/SUS.mp3") # s
DOOT = mixer.Sound("mp3/DOOT.mp3") # d
VINEFART = mixer.Sound("mp3/VINEFART.mp3") # f
GNOMED = mixer.Sound("mp3/GNOMED.mp3") # g
HEHEHEHA = mixer.Sound("mp3/HEHEHEHA.mp3") # h
GRANDDAD = mixer.Sound("mp3/GRANDDAD.mp3") # j
GURANYAA = mixer.Sound("mp3/GURANYAA.mp3") # k
CLASHROYALE = mixer.Sound("mp3/CLASHROYALE.mp3") # l
MEGALOVANIA = mixer.Sound("mp3/MEGALOVANIA.mp3") # m
WEDNESDAY = mixer.Sound("mp3/WEDNESDAY.mp3") # w
XQCHEETO = mixer.Sound("mp3/XQCHEETO.mp3") # x
CERTIFIED = mixer.Sound("mp3/CERTIFIED.mp3") # c
BASSDROP = mixer.Sound("mp3/BASSDROP.mp3") # v
BABABOOEY = mixer.Sound("mp3/BABABOOEY.mp3") # b
BRUH = mixer.Sound("mp3/BRUH.mp3") # n
NOKIAARABIC = mixer.Sound("mp3/NOKIAARABIC.mp3") # space
YOUSTUPID = mixer.Sound("mp3/YOUSTUPID.mp3") # enter
DISCORDPING = mixer.Sound("mp3/DISCORDPING.mp3") # backspace
YEET = mixer.Sound("mp3/YEET.mp3") # tab
WHATSAPPDRIP = mixer.Sound("mp3/WHATSAPPDRIP.mp3") # ctrl_r
DISCORDCALL = mixer.Sound("mp3/DISCORDCALL.mp3") # ctrl
AIRPODSHOTTY = mixer.Sound("mp3/AIRPODSHOTTY.mp3") # alt
FUTURESEASHANTY = mixer.Sound("mp3/FUTURESEASHANTY.mp3") # shift_r
SEASHANTY = mixer.Sound("mp3/SEASHANTY.mp3") # shift
spacenotheld = True

def on_press(key):
    global spacenotheld
    try:
        k = key.char
    except:
        k = key.name

    if k == '0':
        PLUSTEN.play()
    if k == '1':
        TWENTYONE.play()
    if k == '2':
        NOOTNOOT.play()
    if k == '3':
        SWAWS.play()
    if k == '4':
        SAMSUNG.play()
    if k == '5':
        BEANS.play()
    if k == '6':
        THWOMP.play()
    if k == '7':
        CAVE.play()
    if k == '8':
        ALARM.play()
    if k == '9':
        WHATSNINE.play()

    if k == 'a' or k == 'A':
        NYAGA.play()
    if k == 'z' or k == 'Z':
        SLEEP.play()
    if k == 'e' or k == 'E':
        SPEEN.play()
    if k == 'r' or k == 'R':
        OOF.play()
    if k == 't' or k == 'T':
        TACOBELL.play()
    if k == 'y' or k == 'Y':
        YODA.play()
    if k == 'u' or k == 'U':
        AMOGUS.play()
    if k == 'i' or k == 'I':
        SCOOB.play()
    if k == 'o' or k == 'O':
        OHMYGOD.play()
    if k == 'p' or k == 'P':
        PIZZATIME.play()
    if k == 'q' or k == 'Q':
        THICC.play()
    if k == 's' or k == 'S':
        SUS.play()
    if k == 'd' or k == 'D':
        DOOT.play()
    if k == 'f' or k == 'F':
        VINEFART.play()
    if k == 'g' or k == 'G':
        GNOMED.play()
    if k == 'h' or k == 'H':
        HEHEHEHA.play()
    if k == 'j' or k == 'J':
        GRANDDAD.play()
    if k == 'k' or k == 'K':
        GURANYAA.play()
    if k == 'l' or k == 'L':
        CLASHROYALE.play()
    if k == 'm' or k == 'M':
        MEGALOVANIA.play()
    if k == 'w' or k == 'W':
        WEDNESDAY.play()
    if k == 'x' or k == 'X':
        XQCHEETO.play()
    if k == 'c' or k == 'C':
        CERTIFIED.play()
    if k == 'v' or k == 'V':
        VINEBOOM.play()
    if k == 'b' or k == 'B':
        BABABOOEY.play()
    if k == 'n' or k == 'N':
        BRUH.play()
    if k == 'space' and spacenotheld:
        NOKIAARABIC.play()
        spacenotheld = False
    if k == 'shift':
        SEASHANTY.play()
    if k == 'shift_r':
        FUTURESEASHANTY.play()

def on_release(key):
    global spacenotheld
    try:
        k = key.char
    except:
        k = key.name
    
    if k == 'space':
        NOKIAARABIC.stop()
        spacenotheld = True
    if k == 'shift':
        SEASHANTY.stop()
    if k == 'shift_r':
        FUTURESEASHANTY.stop()

if __name__=='__main__':
    listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
    listener.start()
    while True:
        pass