import tkinter
window = tkinter.Tk()
window.title("Daenerys Game")
window.geometry("1280x720")
#window.wm_iconbitmap("Icon.ico")
photo = tkinter.PhotoImage(file = "/Users/sony/Desktop/run.gif")
image = tkinter.Label(window, image = photo).pack()
#panel.pack(side = "bottom", fill = "both", expand = "yes")
#photo1 = tkinter.PhotoImage(file = "/Users/sony/Desktop/d.jpg")
#image1 = tkinter.Label(window, image1=photo1) .pack()
#photo.pack(side="bottom")
lbl = tkinter.Entry(window)
btn = tkinter.Button(window, text = "New Game", fg = "#383a39", bg="#a1dbcd", width = 10, height = 2)
btn.pack()
#lbl.pack()
btn3 = tkinter.Button(window, text = "Quit", fg = "#383a39", bg="#a1dbcd")
btn3.pack()
background = tkinter.Canvas(window, width = 1280, height = 720)
background.create_rectangle(0,0,1280,720, fill= "Dark Grey")
background.pack()
window.mainloop()
