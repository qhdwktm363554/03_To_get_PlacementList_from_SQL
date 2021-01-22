import tkinter as tk

class Placement_List(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="line을 입력하시오~!!!", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)


        def func1():
            line = "BS1"
            print(line)
            return "BS1"
        def func2():
            line = "BS2"
            print(line)
        def func3():
            line = "BS3"
            print(line)

        def funcB(): return master.switch_frame(DirectoryPage)
        tk.Button(self, text="BS1", command=lambda: [func1(), funcB()]).pack()

        tk.Button(self, text="BS2", command=lambda: [func2(), funcB()]).pack()

        tk.Button(self, text="BS3", command=lambda: [func3(), funcB()]).pack()

        tk.Button(self, text="BS3", command=lambda: master.switch_frame(PageTwo)).pack()

class DirectoryPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='skyblue')
        tk.Label(self, text="final_directory를 입력하시오", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로 가자!!",command=lambda: master.switch_frame(StartPage)).pack()

        def ent_cmd():
            print(ent.get())
            things_own = ent.get()
            print(things_own)

        def funcBong(): return master.switch_frame(Bong_page)
        tk.Button(self, text="이걸 입력하자", command = lambda:[ent_cmd(), funcBong()]).pack()
        # tk.Button(self, text="이걸 입력하자", command=ent_cmd).pack()
        ent = tk.Entry(self,text="final_directory" ,width=30)
        ent.pack()
        # tk.Entry(self,text="final_directory" ,width=30).pack()
        things_own = ent.get()

class Bong_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.line = StartPage(self).line
        tk.Label(self, text="Line is {}".format(self.line), font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)




        # ent = Entry(bong, width=30)
        # ent.insert(END, "Here")
        # ent.pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = Placement_List()
    app.mainloop()