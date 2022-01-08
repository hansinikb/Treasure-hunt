###IMPORTING MODULES
import time
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

energy_level=5
###EQUIPMEMTS PAGE
def equipments():
    global value,text,values,v
    i=0
    def equipments_cb():
        if cb1var==1:
            i+=1

    root_equipments=Toplevel()
    root_equipments.title('equipments room')
    root_equipments.geometry('200x200')
    #the foolowing lines not there
    cb1var=IntVar()
    cb2var=IntVar()
    cb3var=IntVar()
    cb4var=IntVar()

    equipments_label=Label(root_equipments,text='Pick any one equipment')
    equipments_label.pack()
    equipments_cb1=Radiobutton(root_equipments,text='sun protection',variable=cb1var)#,onvalue=1,offvalue=0,command=equipments_cb)
    equipments_cb1.pack()#place(x=20,y=20)
    equipments_cb2=Radiobutton(root_equipments,text='energy booster',variable=cb2var)#,onvalue=1,offvalue=0)
    equipments_cb2.pack()#place(x=20,y=50)
    equipments_cb1 = Radiobutton(root_equipments, text='toughener',variable=cb3var)#,onvalue=1,offvalue=0)
    equipments_cb1.pack()#place(x=20, y=80)
    equipments_cb2 = Radiobutton(root_equipments, text='elexir',variable=cb4var)#,onvalue=1,offvalue=0)
    equipments_cb2.pack()#place(x=20, y=110)


    # Dictionary to create multiple buttons
    values = {"sun protection": "1",
              "energy booster": "2",
              "toughener": "3",
              "elexir": "4"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    def clicked(val):
        print(val)

    # v = StringVar(root_equipments)
    # for (text, value) in values.items():
    #
    #     Radiobutton(root_equipments, text=text, variable=v,value=value, indicator=0,background="light blue",command=clicked(value)).pack(fill=X, ipady=5)
    # print(v.get())
    def clicked1():
        print(1)
    def clicked2():
        print(2)
    def clicked3():
        print(3)
    def clicked4():
        print(4)
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    v1.set('1');v2.set('2');v3.set('3');v4.set('4')

    rb1 = Radiobutton(root_equipments, text='sun protection', variable=v1,value=1,command=clicked1,indicator=0).pack()
    rb2=Radiobutton(root_equipments,text='energy booster',variable=v2,value=2,command=clicked2,indicator=0).pack()
    rb3=Radiobutton(root_equipments,text='toughener',variable=v3,value=3,command=clicked3,indicator=0).pack()
    rb4=Radiobutton(root_equipments,text="elexir",variable=v4,value=4,command=clicked4,indicator=0).pack()


    root_equipments.mainloop()
###LEVEL5
def level5():
    pass
####LEVEL 4
def level4():
    pass
####LEVEL 3

def level3():
    def next(a, b):
        a.destroy()
        b.destroy()
        global mirage1

        def on_button_press_mirage(no):
            if no == 1:
                msg_mirage = messagebox.showinfo('showinfo', 'this is correct')
                time.sleep(1)
                level4()

            else:
                msg_mirage2 = messagebox.showinfo('showinfo', 'this is incorrect')
                list1 = [m1, m2]
                random.shuffle(list1)
                print(list1)
                list1[0].place(x=0, y=0)
                list1[1].place(x=700, y=0)

        # mirage1 = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\desert_image_mirage.png')
        image_m = Image.open(r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\desert_image_mirage.png')

        # Resize the image using resize() method
        resize_image_m = image_m.resize((500, 400))

        mirage1 = ImageTk.PhotoImage(resize_image_m)

        m1 = Button(root_level3, image=mirage1)
        m1['command'] = lambda: on_button_press_mirage(1)
        m1.place(x=0, y=0)
        m2 = Button(root_level3, image=mirage1)
        m2['command'] = lambda: on_button_press_mirage(2)
        m2.place(x=700, y=0)

    root_level3 = Tk()
    root_level3.title('lvl3')
    root_level3.geometry("1500x900")
    root_level3.configure(bg='blue')
    # Read the Image
    image = Image.open(r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\desert_img5.png')

    # Resize the image using resize() method
    resize_image = image.resize((1500, 900))

    img = ImageTk.PhotoImage(resize_image)

    # create label and add resize image
    label1 = Label(image=img)
    label1.pack()
    l1 = Label(root_level3,
               text='You have lost your backpack in the quicksand and need energy.\nYou need water .\nYou see an oasis in front of you ,pick the real one.\nYou have two tries.',
               fg='black', bg='orange', font=('ink free', 30))
    l1.place(x=20, y=20)

    ### place when used directly after button or label(in first line) does not work, give separately
    b1 = Button(root_level3, text='next')
    b1['command'] = lambda: next(b1, l1)
    b1.place(x=400, y=300)

    #root_level3.mainloop()

#######level2()
w, g, c = 0, 0, 0
error_count=0

def level2():
    global w,g,c,error_count
    def double_press(widget):
        widget.destroy()
    def on_button_press_boat():
        global w,c,g,error_count
        if (w==1):
            wolf.place(x=20,y=20)
            w=0
        elif(c==1):
            carrot.place(x=200,y=200)
            c=0
        elif(g==1):
            goat.place(x=200,y=20)
            g=0



    def on_button_press_wolf(widget):
        global g, c, w, error_count
        if error_count > 3:
            msg1 = messagebox.showinfo('exit', '4 incorrect attempts, exiting....')
            time.sleep(3)
            root_level2.destroy()
            return None
        if w==0:
            widget.place(x=700, y=250)
        w += 1
        print(w, g, c, error_count,4)############4
        if g==2 and c!=2 and w==2:
            goat.place(x=700, y=250)
            wolf.place(x=900, y=250)
            w = 2
            g = 1
        if (g==2 and c==2 and w==2):
            msg3=messagebox.showinfo('next','yay! you comleted the level! you will be directed to level 3')
            time.sleep(1)
            level3()
        elif (g==2 and c==2 and w!=2)or (g==2 and c!=2 and w==2)or (g==1 and c==1)or(c==1 and w==1) or (g==0 and c==0 and w!=0) or (g==0 and c!=0 and w==0):
            msg = messagebox.showinfo("showinfo", "Incorrect move, try again!")
            error_count += 1
            wolf.place(x=20,y=20)
            goat.place(x=200,y=20)
            carrot.place(x=200,y=200)
            c,w,g=0,0,0
        elif w > 1:
            widget.place(x=900, y=250)

    def on_button_press_carrot(widget):

        global g, c, w, error_count
        print(w, g, c, error_count,5)#############5
        if error_count > 3:
            msg1 = messagebox.showinfo('exit', '4 incorrect attempts, exiting....')
            time.sleep(3)
            root_level2.destroy()
        widget.place(x=700, y=250)
        c += 1
        if (g==2 and c==2 and w==2):
            msg3=messagebox.showinfo('next','yay! you comleted the level! you will be directed to level 3')
            time.sleep(1)
            root_level2.destroy()
            level3()
        elif (g==2 and c==2 and w!=2)or (g==2 and c!=2 and w==2)or (g==1 and c==1)or(c==1 and w==1) or (g==0 and c==0 and w!=0) or (g==0 and c!=0 and w==0):
            msg = messagebox.showinfo("showinfo", "Incorrect move, try again!")
            error_count += 1
            wolf.place(x=20,y=20)
            goat.place(x=200,y=20)
            carrot.place(x=200,y=200)
            c,w,g=0,0,0
        elif c > 1:
            widget.place(x=900, y=250)

    def on_button_press_goat(widget):
        global g,c,w,error_count
        print(w, g, c, error_count,6)##########6
        if error_count > 3:
            msg1 = messagebox.showinfo('exit', '4 incorrect attempts, exiting....')
            time.sleep(3)
            root_level2.destroy()
            return None
        widget.place(x=700, y=250)
        g += 1
        if (g==2 and c==2 and w==2):
            msg3=messagebox.showinfo('next','yay! you comleted the level! you will be directed to level 3')
            time.sleep(1)
            root_level2.destroy()
            level3()
        elif (g==2 and c==2 and w!=2)or (g==2 and c!=2 and w==2)or (g==1 and c==1)or(c==1 and w==1) or (g==0 and c==0 and w!=0) or (g==0 and c!=0 and w==0):
            msg = messagebox.showinfo("showinfo", "Incorrect move, try again!")
            error_count += 1
            wolf.place(x=20, y=20)
            goat.place(x=200, y=20)
            carrot.place(x=200, y=200)
            c, w, g = 0, 0, 0
        elif g > 1:
            widget.place(x=900, y=250)
    root_level2 = Tk()
    root_level2.title('lvl2')
    root_level2.geometry("1500x900")
    root_level2.configure(bg='blue')
    # Read the Image
    image = Image.open(r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\desert_img8.png')

    # Resize the image using resize() method
    resize_image = image.resize((1500, 900))

    img = ImageTk.PhotoImage(resize_image)

    # create label and add resize image
    label1 = Label(image=img)
    label1.pack()
    #root = Tk()
    photogoat = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\goat.png')
    photoboat = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\boat.png')
    photohuman = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\human.png')
    photocarrot = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\carrot.png')

    photowolf = PhotoImage(file=r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\wolf.png')

    goat = Button(root_level2, text="Place Randomly!",image=photogoat)
    goat['command'] = lambda : on_button_press_goat(goat)
    goat.place(x=200, y=20)

    wolf = Button(root_level2, text="Place Randomly!", image=photowolf)
    wolf['command'] = lambda: on_button_press_wolf(wolf)
    wolf.place(x=20, y=20)

    carrot = Button(root_level2, text="Place Randomly!", image=photocarrot)
    carrot['command'] = lambda: on_button_press_carrot(carrot)
    carrot.place(x=200, y=200)

    human = Button(root_level2, text="Place Randomly!", image=photohuman)
    #human['command'] = lambda: on_button_press(human)
    human.place(x=500, y=250)

    boat = Button(root_level2, text="Place Randomly!", image=photoboat)
    boat['command'] = lambda : on_button_press_boat()
    boat.place(x=500, y=500)
    #root_level2.mainloop()
####LEVEL 1
def level1():
    def rearrange():
        global try_count
        #root_level1.destroy()
        root_rearrange_level1=Toplevel()
        root_rearrange_level1.title('rearrange')
        root_rearrange_level1.geometry("1500x900")
        rearrange_level1_label1 = Label(root_rearrange_level1, text='\'Ahlan! ', fg='white', bg='black',
                              font=('ink free', 20))
        rearrange_level1_label1.place(x=150, y=100)
        rearrange_level1_label2 = Label(root_rearrange_level1, text='Aurid aldhahab Wadi Al Hitan.', fg='white',
                              bg='black', font=('ink free', 20))
        rearrange_level1_label2.place(x=150, y=200)
        rearrange_level1_label3 = Label(root_rearrange_level1, text='Kayf tadhhab \'iilaa hunak?',fg='white', bg='black', font=('ink free', 20))
        rearrange_level1_label3.place(x=150, y=300)
        rearrange_level1_label4 = Label(root_rearrange_level1, text='Ashukriyan',
                              fg='white', bg='black', font=('ink free', 20))
        rearrange_level1_label4.place(x=150, y=400)
        rearrange_level1_entry1=Entry(root_rearrange_level1)
        rearrange_level1_entry2=Entry(root_rearrange_level1)
        rearrange_level1_entry3 = Entry(root_rearrange_level1)
        rearrange_level1_entry4 = Entry(root_rearrange_level1)
        rearrange_level1_entry1.place(x=750,y=100)
        rearrange_level1_entry2.place(x=750,y=200)
        rearrange_level1_entry3.place(x=750,y=300)
        rearrange_level1_entry4.place(x=750,y=400)
        print(rearrange_level1_entry1.get())
        try_count = 0
        def rearrange_exit():
            global try_count
            if (rearrange_level1_entry1.get()=='1')and (rearrange_level1_entry2.get()=='2')and(rearrange_level1_entry3.get()=='3')and (rearrange_level1_entry4.get()=='4'):
                msg3 = messagebox.showinfo("showinfo", "The toureg has understood your question.")
                root_rearrange_level1.destroy()
                root_level1.destroy()
                level2()
            elif try_count<4:
                msg1=Message(root_rearrange_level1,text='Try again!')
                msg1.pack()
                try_count+=1
            else:
                msg2=messagebox.showinfo("showinfo", "You have failed. Better luck next time!")
                root_rearrange_level1.destroy()
                root_level1.destroy()



        #bu = Button(root_rearrange_level1, text='done', command=rearrange_exit(rearrange_level1_entry1)).place(x=750, y=700)

        bu = Button(root_rearrange_level1, text='done', command=rearrange_exit).place(x=750,
                                                                                                               y=700)

        #root_rearrange_level1.mainloop()

    root.destroy()
    root_level1=Tk()
    root_level1.title('LEVEL 1')
    root_level1.geometry("1500x900")
    root_level1.configure(bg='black')
    level1_label1=Label(root_level1,text='You are in level 0 of level 5 of the game. ', fg='white', bg='black', font=('ink free',20))
    level1_label1.place(x=150,y=100)
    level1_label2=Label(root_level1,text='You are surrounded by the Touregs, the nomads of Arabia', fg='white', bg='black', font=('ink free',20))
    level1_label2.place(x=150,y=200)
    level1_label3=Label(root_level1,text='To complete this level you will be required to ask the Toureg for', fg='white', bg='black', font=('ink free',20))
    level1_label3.place(x=150,y=300)
    level1_label4=Label(root_level1,text='directions to reach the Wadi Al Hitan,the White Valley before', fg='white', bg='black', font=('ink free',20))
    level1_label4.place(x=150,y=350)
    level1_label5=Label(root_level1,text=' sunset.', fg='white', bg='black', font=('ink free',20))
    level1_label5.place(x=150,y=400)
    level1_label6 = Label(root_level1, text='The nomads speak Arabic.', fg='white', bg='black', font=('ink free', 20))
    level1_label6.place(x=150, y=500)
    level1_label7 = Label(root_level1, text='Rearrange the following questions to be asked.', fg='white', bg='black', font=('ink free', 20))
    level1_label7.place(x=150, y=600)
    level1_label8 = Label(root_level1, text=' You have three tries.', fg='white', bg='black', font=('ink free', 20))
    level1_label8.place(x=150, y=700)
    bu=Button(root_level1,text='ok',command=rearrange).place(x=750,y=700)
    #root_level1.mainloop()




###WELCOME PAGE
root=Tk()
root.title('Welcome to theme Desert')
root.geometry("1500x900")
# Read the Image
image = Image.open(r'C:\Users\hansi\OneDrive\GitHub\Mini-Project\desert_img7.png')

# Resize the image using resize() method
resize_image = image.resize((1500,900))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.pack()

#adding text
welcome_label=Label(root,text='Welcome to a sunny afternoon in the Sahara!', fg='black', bg='orange', font=('ink free',20))
#a.grid(column="0",row="1")
welcome_label.place(x=500, y=650)

theme_label=Label(root,text='You have chosen Theme: Desert.', fg='black', bg='orange', font=('ink free',60))
#a.grid(column="0",row="1")
theme_label.place(x=250, y=500)
equipments_button=Button(root,text='>>equipments',command = equipments)
equipments_button.place(x=900,y=700)
next_button=Button(root,text='>>go to level 1',command = level1)
next_button.place(x=1000,y=700)
root.mainloop()



