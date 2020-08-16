#Thu 23th July 2015
from tkinter import *
import random
import time  #Importing neccesaries
import tkinter.font
import tkinter.messagebox
import collections
import string

#Sample Cipher
#NYVLG GSYGL CHXFE UYTQC ESQXP ZIUFI GGRBJ HPAYN CRUYF PSXUF IUPSK YRECT MMCNC RUYRE GXIGR LGLBT IBLME CEBZS VRLPU XPBIB JAJRL JREOB AJRLU FIGJE HBEZY WTMGJ YXFQX ICTSG RDGTB JAFYO OCWTM JBLCT WWUCQ MGOFR LFMRF RLFWL BTIJL WUYPM CHJQX ICRFC HUMTS MZJBI MYVHC UVYRU GXJCW PDTPU ISRLF DHBAE NCYQU MUFEO GRHCR JMYTQ SMSXJ MRCSX JRMTT ISWZV JRFPE CJITN IDGEM DSSAI TASVJ HUYOF GXPSX GMVVQ FVRXI YXXMY MBXFJ PUFIG BEUFE UUIIY ZFAVB AOFBX ICMSA MQFIS QWPGR TRIBB MTSKH CWUUI MCXUF INBIT RVPWX SMNBL JPPYT UIXGP MLIFB GPMTF PEUGS ODVPK XICSN YRJES WCVOK IOREO YVNCH GGKIR ISHIU YRERL FDPJE LUASO RVPJW ZQXFK WGPSN YHSMR FKIBL AIGPF UIOCI ERSFL WVPIU USUFM OEWPL IUFEU UIEMR PRWFL HDPMU GGBJM ODSSK EUGSO YGSMW TRLFZ ECYPN YREYF TRVBG XBLHU USUFE UUIVQ IBLSO AVJRM DYPLC CHCRF PEUGS ONVPR SDMPP LXIYX DFEOL IMEMW CRUFI MCZFJ SGASN KMUKI ORXIC JEYLB TITFS XLMOB IWCPP NMOEX IGWQJ EOGEN QYSCX IYXUF IZUMM JVFGR TREUC XICTP UISQY QNPZU MUFMO YJFUQ PLXIQ FVRAJ RLMSG LRLFW AJJPO MXHSI TQXIY XXCOO MABZS VRMUY REUIX GPMNY UGXPS XPDFV QMOCW TDSSJ SOEIO MYHFX PASNC YQUMU FEQJE OMJPS VPURU MIYNP PGXJR MORLF KIBLX JKIXC RPUOO MAUFE URLFG VIGKI CWUQI DSVJR CDMQN SRJAE UGSOQ ESCIO AVZNX FBYTG RHYGB BIOSW DGTIC VTMAF AEOQX BPXIS RUGRH RLSMY HFXIC HBREC YWFDS SMXIC VJLXF PGFNX TUIDY RDPED IXIGW NYCCC XICFS CELRL SMYHF AFFEW CFFCR MMSLG RHDSS GRUFI GGKIR EHYMO QXUFI GBEMC XTLSU QGSCA JRYQY PMRLF ZITRL BPVZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
defd = """
QEVO, 

XLEROW JSV FVMRKMRK QI MR SR XLMW SRI, WIIQW PMOI E JEWGMREXMRK GEWI. 

M LEZI XLVII UYIWXMSRW: 
ALC ASYPH XLI JPEK HEC EWWSGMEXIW AERX E WLMT? 
ALC ASYPH XLIC AERX XLMW WLMT? 
ALC ASYPH XLIC AERX XLMW WLMT RSA? 

LEZMRK VIEH XLI EXXEGLIH HSGYQIRX M WYWTIGX XLEX XLI ERWAIVW EVI EPP VIPEXIH XS XLI UYIWXMSR SJ ALEX IBEGXPC WLI ERH LIV JPEK HEC EWWSGMEXI GVIA AIVI XVCMRK XS WYVZIC. 

M EQ KYIWWMRK XLEX CSY EPVIEHC GLIGOIH SYX XLI SRFSEVH KTW WCWXIQ JSV MRJSVQEXMSR EFSYX LIV QSZIQIRXW, FYX MJ CSY HMH JMRH ERCXLMRK M ASYPH FI JEWGMREXIH XS LIEV EFSYX MX. MR XLI QIERXMQI M EQ TVIXXC WYVI XLEX CSY ORSA QSVI EFSYX XLI JPEK HEC EWWSGMEXIW XLER CSY LEZI XSPH QI, WS E FVMIJMRK ASYPH FI QYGL ETTVIGMEXIH. 

EPP XLI FIWX, 

LEVVC
"""
global tk
tk = Tk()#Defining tk
tk.title("TkCracker - Version 0.1.6")#Title at top of window
tk.resizable(0, 0) #Stops window being manually resizable
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=1000, bg='black',)#If canvas size changed,

width = 1000
height = 1000
def Exit():
    quit1 = tkinter.messagebox.askyesno('Quit','Are you sure you want to quit?') #must have askyesno + DO NOT tkinter = Tk() at all
    if quit1 == True:
        quit()

def OpeningText():
    canvas.delete(ALL)

    def Continue():
        canvas.delete(ALL)
        PageTwo()
        
    canvas.create_text(width/2, height/7, fill='red', font=("Bauhaus 93",60), text='Python Decoder')  #Title and info stuff
    canvas.create_text(width/2, 1/4*(height), fill='white', font=("Times New Roman",15), text='This is a program to allow encryption and decryption in a')  
    canvas.create_text(width/2, 1/4*(height)+20, fill='white', font=("Times New Roman",15), text='variety of different types of ciphers.')  
    canvas.pack() #Puts canvas on the screen

    btnquit = Button(canvas, text = "Exit", command = Exit, anchor = W)
    btnquit.configure(width = 10, activebackground = "#33B5E5")
    btnquit_window =  canvas.create_window(890, 10, anchor=NW, window=btnquit)

    btncont = Button(canvas, text = "Continue", command = Continue)
    btncont.configure(width = 10, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 800, anchor=NW, window=btncont)    

def PageTwo(): #THE PAGE FOR GETTING TO PLACES
    canvas.delete(ALL)
    btnmenu = Button(canvas, text = "Back", command = OpeningText, anchor = W)
    btnmenu.configure(width = 10, activebackground = "#33B5E5")
    btnmenu_window =  canvas.create_window(10, 10, anchor=NW, window=btnmenu)

    btnquit = Button(canvas, text = "Exit", command = Exit, anchor = W)
    btnquit.configure(width = 10, activebackground = "#33B5E5")
    btnquit_window =  canvas.create_window(890, 10, anchor=NW, window=btnquit)

    btncont = Button(canvas, text = "Encrypt / Decrypt", command = EncryptDecrypt)
    btncont.configure(width = 20, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 400, anchor=NW, window=btncont) #Buttons and allllll

    btncont = Button(canvas, text = "Crack", command = Crack)
    btncont.configure(width = 20, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 300, anchor=NW, window=btncont)

    btncont = Button(canvas, text = "Analyse", command = Analyse)
    btncont.configure(width = 20, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 500, anchor=NW, window=btncont)
    
    btncont = Button(canvas, text = "Tutorial + Info", command = TutorialAndInfo)
    btncont.configure(width = 20, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 10, anchor=NW, window=btncont)

def EncryptDecrypt():
    canvas.delete(ALL)
    btncont = Button(canvas, text = "Caesar", command = CaesarSetup)
    btncont.configure(width = 20, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(450, 300, anchor=NW, window=btncont)
    
def Crack():
    print('test')

    
def Analyse():
    canvas.delete(ALL)

    global entertext1
    entertext1=Entry(foreground='red2', width=10)
    #width control
    entertext1.focus_set()   
    entertext1_window =  canvas.create_window(100, 50, window=entertext1) #Creating an entertext box and then setting it onto the canvas at (x,y)

    global entertext2
    entertext2=Entry(foreground='red2', width=10)
    entertext2.focus_set()   
    entertext2_window =  canvas.create_window(100, 80, window=entertext2) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext3
    entertext3=Entry(foreground='red2', width=10)
    entertext3.focus_set()   
    entertext3_window =  canvas.create_window(100, 110, window=entertext3) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext4
    entertext4=Entry(foreground='red2', width=10)
    entertext4.focus_set()   
    entertext4_window =  canvas.create_window(100, 140, window=entertext4) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext5
    entertext5=Entry(foreground='red2', width=10)
    entertext5.focus_set()   
    entertext5_window =  canvas.create_window(100, 170, window=entertext5) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext6
    entertext6=Entry(foreground='red2', width=10)
    entertext6.focus_set()   
    entertext6_window =  canvas.create_window(100, 200, window=entertext6) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext7    
    entertext7=Entry(foreground='red2', width=10)
    entertext7.focus_set()   
    entertext7_window =  canvas.create_window(100, 230, window=entertext7) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext8
    entertext8=Entry(foreground='red2', width=10)
    entertext8.focus_set()   
    entertext8_window =  canvas.create_window(100, 260, window=entertext8) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext9
    entertext9=Entry(foreground='red2', width=10)
    entertext9.focus_set()   
    entertext9_window =  canvas.create_window(100, 290, window=entertext9) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext10
    entertext10=Entry(foreground='red2', width=10)
    entertext10.focus_set()   
    entertext10_window =  canvas.create_window(100, 320, window=entertext10) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext11
    entertext11=Entry(foreground='red2', width=10)
    entertext11.focus_set()   
    entertext11_window =  canvas.create_window(100, 350, window=entertext11) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext12 #these arent even needed are they??
    entertext12=Entry(foreground='red2', width=10)
    entertext12.focus_set()   
    entertext12_window =  canvas.create_window(100, 380, window=entertext12) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext13
    entertext13=Entry(foreground='red2', width=10)
    entertext13.focus_set()   
    entertext13_window =  canvas.create_window(100, 410, window=entertext13) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext14
    entertext14=Entry(foreground='red2', width=10)
    entertext14.focus_set()   
    entertext14_window =  canvas.create_window(100, 440, window=entertext14) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext15
    entertext15=Entry(foreground='red2', width=10)
    entertext15.focus_set()   
    entertext15_window =  canvas.create_window(100, 470, window=entertext15) #Creating an entertext box and then setting it onto the canvas at (x,y)    
    global entertext16
    entertext16=Entry(foreground='red2', width=10)
    entertext16.focus_set()   
    entertext16_window =  canvas.create_window(100, 500, window=entertext16) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext17
    entertext17=Entry(foreground='red2', width=10)
    entertext17.focus_set()   
    entertext17_window =  canvas.create_window(100, 530, window=entertext17) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext18
    entertext18=Entry(foreground='red2', width=10)
    entertext18.focus_set()   
    entertext18_window =  canvas.create_window(100, 560, window=entertext18) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext19
    entertext19=Entry(foreground='red2', width=10)
    entertext19.focus_set()   
    entertext19_window =  canvas.create_window(100, 590, window=entertext19) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext20
    entertext20=Entry(foreground='red2', width=10)
    entertext20.focus_set()   
    entertext20_window =  canvas.create_window(100, 620, window=entertext20) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext21
    entertext21=Entry(foreground='red2', width=10)
    entertext21.focus_set()   
    entertext21_window =  canvas.create_window(100, 650, window=entertext21) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext22
    entertext22=Entry(foreground='red2', width=10)
    entertext22.focus_set()   
    entertext22_window =  canvas.create_window(100, 680, window=entertext22) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext23
    entertext23=Entry(foreground='red2', width=10)
    entertext23.focus_set()   
    entertext23_window =  canvas.create_window(100, 710, window=entertext23) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext24
    entertext24=Entry(foreground='red2', width=10)
    entertext24.focus_set()   
    entertext24_window =  canvas.create_window(100, 740, window=entertext24) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext25
    entertext25=Entry(foreground='red2', width=10)
    entertext25.focus_set()   
    entertext25_window =  canvas.create_window(100, 770, window=entertext25) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext26
    entertext26=Entry(foreground='red2', width=10)
    entertext26.focus_set()   
    entertext26_window =  canvas.create_window(100, 800, window=entertext26) #Creating an entertext box and then setting it onto the canvas at (x,y)

    global entertext01
    entertext01=Entry(foreground='red2', width=10)
    #width control
    entertext01.focus_set()   
    entertext01_window =  canvas.create_window(220, 50, window=entertext01) #Creating an entertext box and then setting it onto the canvas at (x,y)

    global entertext02
    entertext02=Entry(foreground='red2', width=10)
    entertext02.focus_set()   
    entertext02_window =  canvas.create_window(220, 80, window=entertext02) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext03
    entertext03=Entry(foreground='red2', width=10)
    entertext03.focus_set()   
    entertext03_window =  canvas.create_window(220, 110, window=entertext03) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext04
    entertext04=Entry(foreground='red2', width=10)
    entertext04.focus_set()   
    entertext04_window =  canvas.create_window(220, 140, window=entertext04) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext05
    entertext05=Entry(foreground='red2', width=10)
    entertext05.focus_set()   
    entertext05_window =  canvas.create_window(220, 170, window=entertext05) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext06
    entertext06=Entry(foreground='red2', width=10)
    entertext06.focus_set()   
    entertext06_window =  canvas.create_window(220, 200, window=entertext06) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext07    
    entertext07=Entry(foreground='red2', width=10)
    entertext07.focus_set()   
    entertext07_window =  canvas.create_window(220, 230, window=entertext07) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext08
    entertext08=Entry(foreground='red2', width=10)
    entertext08.focus_set()   
    entertext08_window =  canvas.create_window(220, 260, window=entertext08) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext09
    entertext09=Entry(foreground='red2', width=10)
    entertext09.focus_set()   
    entertext09_window =  canvas.create_window(220, 290, window=entertext09) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext010
    entertext010=Entry(foreground='red2', width=10)
    entertext010.focus_set()   
    entertext010_window =  canvas.create_window(220, 320, window=entertext010) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext011
    entertext011=Entry(foreground='red2', width=10)
    entertext011.focus_set()
    entertext011_window =  canvas.create_window(220, 350, window=entertext011) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext012 #these arent even needed are they??
    entertext012=Entry(foreground='red2', width=10)
    entertext012.focus_set()   
    entertext012_window =  canvas.create_window(220, 380, window=entertext012) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext013
    entertext013=Entry(foreground='red2', width=10)
    entertext013.focus_set()   
    entertext013_window =  canvas.create_window(220, 410, window=entertext013) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext014
    entertext014=Entry(foreground='red2', width=10)
    entertext014.focus_set()   
    entertext014_window =  canvas.create_window(220, 440, window=entertext014) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext015
    entertext015=Entry(foreground='red2', width=10)
    entertext015.focus_set()   
    entertext015_window =  canvas.create_window(220, 470, window=entertext015) #Creating an entertext box and then setting it onto the canvas at (x,y)    
    global entertext016
    entertext016=Entry(foreground='red2', width=10)
    entertext016.focus_set()   
    entertext016_window =  canvas.create_window(220, 500, window=entertext016) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext017
    entertext017=Entry(foreground='red2', width=10)
    entertext017.focus_set()   
    entertext017_window =  canvas.create_window(220, 530, window=entertext017) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext018
    entertext018=Entry(foreground='red2', width=10)
    entertext018.focus_set()   
    entertext018_window =  canvas.create_window(220, 560, window=entertext018) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext019
    entertext019=Entry(foreground='red2', width=10)
    entertext019.focus_set()   
    entertext019_window =  canvas.create_window(220, 590, window=entertext019) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext020
    entertext020=Entry(foreground='red2', width=10)
    entertext020.focus_set()   
    entertext020_window =  canvas.create_window(220, 620, window=entertext020) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext021
    entertext021=Entry(foreground='red2', width=10)
    entertext021.focus_set()   
    entertext021_window =  canvas.create_window(220, 650, window=entertext021) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext022
    entertext022=Entry(foreground='red2', width=10)
    entertext022.focus_set()   
    entertext022_window =  canvas.create_window(220, 680, window=entertext022) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext023
    entertext023=Entry(foreground='red2', width=10)
    entertext023.focus_set()   
    entertext023_window =  canvas.create_window(220, 710, window=entertext023) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext024
    entertext024=Entry(foreground='red2', width=10)
    entertext024.focus_set()   
    entertext024_window =  canvas.create_window(220, 740, window=entertext024) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext025
    entertext025=Entry(foreground='red2', width=10)
    entertext025.focus_set()   
    entertext025_window =  canvas.create_window(220, 770, window=entertext025) #Creating an entertext box and then setting it onto the canvas at (x,y)
    global entertext026
    entertext026=Entry(foreground='red2', width=10)
    entertext026.focus_set()   
    entertext026_window =  canvas.create_window(220, 800, window=entertext026) #Creating an entertext box and then setting it onto the canvas at (x,y)

    
    canvas.create_text(100, 20, fill='white', font=("Times New Roman", 9), text='Letter Freq. (%) in Cipher')  
    canvas.create_text(220, 20, fill='white', font=("Times New Roman", 9), text='Letter Freq. (%) in Eng. Lang. (Avg.)')  
    canvas.create_text(600, 20, fill='white', font=("Times New Roman", 20), text='Cipher Text')  
    canvas.create_text(600, 825, fill='white', font=("Times New Roman", 20), text='Translated Text')  

    text = Text(tk)
    text_window = canvas.create_window(600,220, window=text) #Big text box with multiple lines for writing
    #Idefk how to control the size though its a decent size but i didnt set that?!?!?!
    global textTwo
    textTwo = Text(tk)
    textTwo_window = canvas.create_window(600,630, window=textTwo)

    btnmenu = Button(canvas, text = "Back", command = PageTwo, anchor = W)
    btnmenu.configure(width = 10, activebackground = "#33B5E5")
    btnmenu_window =  canvas.create_window(890, 10, anchor=NW, window=btnmenu) 

    btnmenu = Button(canvas, text = "Clear", command = Clear, anchor = W)
    btnmenu.configure(width = 10, activebackground = "#33B5E5")
    btnmenu_window =  canvas.create_window(890, 100, anchor=NW, window=btnmenu)
    
    btnquit = Button(canvas, text = "Exit", command = Exit, anchor = W)
    btnquit.configure(width = 10, activebackground = "#33B5E5")
    btnquit_window =  canvas.create_window(890, 40, anchor=NW, window=btnquit)
                                             
    CL = StringVar()
    CL.set("Choose Cipher Letter")
    optmen = OptionMenu(tk, CL, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    optmen.configure(width = 30)
    optmen_window = canvas.create_window(450,425, window=optmen)

                                          
    TL = StringVar()
    TL.set("Choose Translated Letter")
    optmen = OptionMenu(tk, TL, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    optmen.configure(width = 30)
    optmen_window = canvas.create_window(750,425, window=optmen)


    



    def FreqTot():
        Clear()
        def freq21(var1):
            global info
            info = text.get(1.0, END)
            textTwo.delete(1.0, END)
            textTwo.insert(1.0, info)
            data = info.upper()
            global totalCount
            totalCount = (len(data)-len([c for c in data if c.isdigit()])) #Get cipher outta the box and then put it in the thingy 
            char_counter = collections.Counter(data)
            for char, count in char_counter.most_common():  ####THIS COUNTS ## AND OTHER SYMBOLS... ITS BROKE NEEDS A FIX
                
                
                if char in data.upper():
                    s = (str(count))
                    my_tokens = s.split("|") #split up  thingy (tuple) into bitssss in a dictionary
                    var1[char] = my_tokens[0]
                    print(char)            
                
        var1 = dict()
        freq21(var1)
        
        APerc=round(100* float(var1['A'])/float(totalCount),3)
        BPerc=round(100* float(var1['B'])/float(totalCount),3)
        CPerc=round(100* float(var1['C'])/float(totalCount),3)
        DPerc=round(100* float(var1['D'])/float(totalCount),3)
        EPerc=round(100* float(var1['E'])/float(totalCount),3) #Select dictionary elements by letter
        FPerc=round(100* float(var1['F'])/float(totalCount),3)
        GPerc=round(100* float(var1['G'])/float(totalCount),3)
        HPerc=round(100* float(var1['H'])/float(totalCount),3)
        IPerc=round(100* float(var1['I'])/float(totalCount),3)
        JPerc=round(100* float(var1['J'])/float(totalCount),3)
        KPerc=round(100* float(var1['K'])/float(totalCount),3)
        LPerc=round(100* float(var1['L'])/float(totalCount),3)
        MPerc=round(100* float(var1['M'])/float(totalCount),3)
        NPerc=round(100* float(var1['N'])/float(totalCount),3)
        OPerc=round(100* float(var1['O'])/float(totalCount),3) #BUT THEY SHOULDNT BE BY LETTER THEY SHOULD BE BY SIZEEEE
        PPerc=round(100* float(var1['P'])/float(totalCount),3)#TOFIXTOFIXTOFIX
        QPerc=round(100* float(var1['Q'])/float(totalCount),3)
        RPerc=round(100* float(var1['R'])/float(totalCount),3)
        SPerc=round(100* float(var1['S'])/float(totalCount),3)
        TPerc=round(100* float(var1['T'])/float(totalCount),3)
        UPerc=round(100* float(var1['U'])/float(totalCount),3)# FIX ME
        VPerc=round(100* float(var1['V'])/float(totalCount),3)
        WPerc=round(100* float(var1['W'])/float(totalCount),3)
        XPerc=round(100* float(var1['X'])/float(totalCount),3)
        YPerc=round(100* float(var1['Y'])/float(totalCount),3)
        ZPerc=round(100* float(var1['Z'])/float(totalCount),3)

        strA = str(APerc)
        strB = str(BPerc)
        strC = str(CPerc)
        strD = str(DPerc)
        strE = str(EPerc)
        strF = str(FPerc)
        strG = str(GPerc)
        strH = str(HPerc)
        strI = str(IPerc)
        strJ = str(JPerc)
        strK = str(KPerc)
        strL = str(LPerc)
        strM = str(MPerc)
        strN = str(NPerc)
        strO = str(OPerc)
        strP = str(PPerc)
        strQ = str(QPerc)
        strR = str(RPerc)
        strS = str(SPerc)
        strT = str(TPerc)
        strU = str(UPerc)
        strV = str(VPerc)
        strW = str(WPerc)
        strX = str(XPerc)
        strY = str(YPerc)
        strZ = str(ZPerc)

        entertext1.insert(END,'A = ' + strA + '%')        
        entertext2.insert(END,'B = ' + strB + '%')        
        entertext3.insert(END,'C = ' + strC + '%')        
        entertext4.insert(END,'D = ' + strD + '%')        
        entertext5.insert(END,'E = ' + strE + '%')        
        entertext6.insert(END,'F = ' + strF + '%')        
        entertext7.insert(END,'G = ' + strG + '%')        
        entertext8.insert(END,'H = ' + strH + '%')        
        entertext9.insert(END,'I = ' + strI + '%')        #put all this into text boxes
        entertext10.insert(END,'J = ' + strJ + '%')        
        entertext11.insert(END,'K = ' + strK + '%')        
        entertext12.insert(END,'L = ' + strL + '%')        
        entertext13.insert(END,'M = ' + strM + '%')        
        entertext14.insert(END,'N = ' + strN + '%')        
        entertext15.insert(END,'O = ' + strO + '%')        
        entertext16.insert(END,'P = ' + strP + '%')        
        entertext17.insert(END,'Q = ' + strQ + '%')        
        entertext18.insert(END,'R = ' + strR + '%')        
        entertext19.insert(END,'S = ' + strS + '%')        
        entertext20.insert(END,'T = ' + strT + '%')        
        entertext21.insert(END,'U = ' + strU + '%')        
        entertext22.insert(END,'V = ' + strV + '%')        
        entertext23.insert(END,'W = ' + strW + '%')        
        entertext24.insert(END,'X = ' + strX + '%')        
        entertext25.insert(END,'Y = ' + strY + '%')        
        entertext26.insert(END,'Z = ' + strZ + '%')        

        entertext01.insert(END,'A = 8.167%')        
        entertext02.insert(END,'B = 1.492%')        
        entertext03.insert(END,'C = 2.782%')        
        entertext04.insert(END,'D = 4.253%')        
        entertext05.insert(END,'E = 12.702%')        
        entertext06.insert(END,'F = 2.228%')        
        entertext07.insert(END,'G = 2.015%')        
        entertext08.insert(END,'H = 6.094%')        
        entertext09.insert(END,'I = 6.966%')        #put all this into text boxes
        entertext010.insert(END,'J = 0.153%')        
        entertext011.insert(END,'K = 0.722%')        
        entertext012.insert(END,'L = 4.025%')        
        entertext013.insert(END,'M = 2.406%')        
        entertext014.insert(END,'N = 6.749%')        
        entertext015.insert(END,'O = 7.507%')        
        entertext016.insert(END,'P = 1.929%')        
        entertext017.insert(END,'Q = 0.095%')        
        entertext018.insert(END,'R = 5.987%') #average letters in OED
        entertext019.insert(END,'S = 6.327%')        
        entertext020.insert(END,'T = 9.056%')        
        entertext021.insert(END,'U = 2.758%')        
        entertext022.insert(END,'V = 0.978%')        
        entertext023.insert(END,'W = 2.361%')        
        entertext024.insert(END,'X = 0.150%')        
        entertext025.insert(END,'Y = 1.974%')        
        entertext026.insert(END,'Z = 0.074%')           
        Setup()

    def Setup():
        global List
        List = []
        global ListTwo
        ListTwo = list(text.get(1.0, END))
    def Replace():
        CipherLet = CL.get()
#        print(CipherLet)
        TranslatedLet = TL.get()
#        print(TranslatedLet)
        List.append(CipherLet)
        List.append(TranslatedLet)
#        print(List)
        global Temp
        Temp=list(text.get(1.0, END))
        n = len(List)
        z = int(n/2)
        t = 0
        x = 1
        for i, j in enumerate(Temp):
            if j == CipherLet: 
#                print(i)
                ListTwo[i]=TranslatedLet
 #      print(ListTwo)
#        print(Temp)
        ListThree = ''.join(ListTwo)
        textTwo.delete(1.0, END)
        textTwo.insert(1.0, ListThree)        

    btnquit = Button(canvas, text = "Go", command = Replace, anchor = W)
    btnquit.configure(width = 10, activebackground = "#33B5E5")
    btnquit_window =  canvas.create_window(890, 410, anchor=NW, window=btnquit)
    
    btncont = Button(canvas, text = "Run", command =FreqTot)
    btncont.configure(width = 10, activebackground = "#33B5E5")
    btncont_window =  canvas.create_window(890, 70, anchor=NW, window=btncont) 

def Clear():
    global entertext01
    entertext01.delete(0,END)
    global entertext02
    entertext02.delete(0,END)
    global entertext03
    entertext03.delete(0,END)
    global entertext04
    entertext04.delete(0,END)
    global entertext05
    entertext05.delete(0,END)
    global entertext06
    entertext06.delete(0,END)
    global entertext07
    entertext07.delete(0,END)
    global entertext08
    entertext08.delete(0,END)
    global entertext09
    entertext09.delete(0,END)
    global entertext010
    entertext010.delete(0,END)
    global entertext011
    entertext011.delete(0,END)
    global entertext012
    entertext012.delete(0,END)
    global entertext013
    entertext013.delete(0,END)
    global entertext014
    entertext014.delete(0,END)
    global entertext015
    entertext015.delete(0,END)
    global entertext016
    entertext016.delete(0,END)
    global entertext017
    entertext017.delete(0,END)
    global entertext018
    entertext018.delete(0,END)
    global entertext019
    entertext019.delete(0,END)
    global entertext020
    entertext020.delete(0,END)
    global entertext021
    entertext021.delete(0,END)
    global entertext022
    entertext022.delete(0,END)
    global entertext023
    entertext023.delete(0,END)
    global entertext024
    entertext024.delete(0,END)
    global entertext025
    entertext025.delete(0,END)
    global entertext026
    entertext026.delete(0,END)

    global entertext1
    entertext1.delete(0,END)
    global entertext2
    entertext2.delete(0,END)
    global entertext3
    entertext3.delete(0,END)
    global entertext4
    entertext4.delete(0,END)
    global entertext5
    entertext5.delete(0,END)
    global entertext6
    entertext6.delete(0,END)
    global entertext7
    entertext7.delete(0,END)
    global entertext8
    entertext8.delete(0,END)
    global entertext9
    entertext9.delete(0,END)
    global entertext10
    entertext10.delete(0,END)
    global entertext11
    entertext11.delete(0,END)
    global entertext12
    entertext12.delete(0,END)
    global entertext13
    entertext13.delete(0,END)
    global entertext14
    entertext14.delete(0,END)
    global entertext15
    entertext15.delete(0,END)
    global entertext16
    entertext16.delete(0,END)
    global entertext17
    entertext17.delete(0,END)
    global entertext18
    entertext18.delete(0,END)
    global entertext19
    entertext19.delete(0,END)
    global entertext20
    entertext20.delete(0,END)
    global entertext21
    entertext21.delete(0,END)
    global entertext22
    entertext22.delete(0,END)
    global entertext23
    entertext23.delete(0,END)
    global entertext24
    entertext24.delete(0,END)
    global entertext25
    entertext25.delete(0,END)
    global entertext26
    entertext26.delete(0,END)

    textTwo.delete(1.0, END)
def TutorialAndInfo():
    print('test')

OpeningText()
