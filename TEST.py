from tkinter import*

bong = Tk()
bong.title("GUI_TEST")
# bong.geometry("540x800")
bong.geometry("440x700+800+100")

label1 = Label(bong, text = "SELECT LINE")
label1.pack()

def change():
    label1.config(text = "TYPE THE FINAL DIRECTORY")

def btncmd():
    print("BS1")
    line_name = "BS1"
def btncmd2():
    print("BS2")
    line_name = "BS2"
def btncmd3():
    print("BS3")
    line_name = "BS3"

#padx: x여백 / pady:y여백 / fg:foreground / bg: background /

btn2 = Button(bong, padx=5, pady=5, width=5, height=1,fg="darkblue", bg="white", text = "BS2", command = btncmd2)
btn3 = Button(bong, padx=5, pady=5, width=5, height=1,fg="darkblue", bg="white", text = "BS3", command = change)
#아래를 눌러야 실제 루트에 버튼이 포함된다.

btn2.pack()
btn3.pack()

label2 = Label(bong, text = "Final Directory")
label2.pack()

ent = Entry(bong, width=30)
ent.insert(END, "Here")
ent.pack()

def ent_cmd():
    print(ent.get())
    things_own = ent.get()
    print(things_own)

btn_ent = Button(bong, text = "OK", command = ent_cmd)
btn_ent.pack()

frame1 = Frame(bong, relief = "solid", bd=5 )
frame1.pack(side="left", fill = "both", expand = True)
frame2 = Frame(bong, relief = "solid", bd=11 )
frame2.pack(side="right"
                 "", fill = "both", expand = True)

btn1 = Button(frame1, padx=5, pady=5, width=5, height=1,fg="darkblue", bg="white", text = "BS1", command = btncmd)
btn1.pack()

bong.mainloop()
