import tkinter

tkinter._test()
mainWindow = tkinter.Tk()

mainWindow.title("Hello Rohit")
mainWindow.geometry('640x480-52+400')  #'640x480' = screen dimension,'-52' takes it to the right,'+400' brings it down

label = tkinter.Label(mainWindow,text = "Hello World")
label.pack(side = 'top')

leftframe = tkinter.Frame(mainWindow)
leftframe.pack(side="left", anchor="n", fill = tkinter.Y, expand = False)
canvas = tkinter.Canvas(leftframe, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor = "n") #side is LEFT, hence EXPAND is required to extend in X direction.
             #if the side would have been TOP or BOTTOM, then EXPAND would be required for Y direction.

rightframe = tkinter.Frame(mainWindow)
rightframe.pack(side="right", anchor="n", expand = True)

button1 = tkinter.Button(rightframe, text="Button1")
button2 = tkinter.Button(rightframe, text="Button2")
button3 = tkinter.Button(rightframe, text="Button3")
button1.pack(side="top")
button2.pack(side="top")   #only N and S play a role bcoz the side chosen is left
button3.pack(side="top") # if the side was top or bottom, then E and W would have played a role.
mainWindow.mainloop()