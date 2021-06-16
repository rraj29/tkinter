import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()


#the code below helps to take control of it by the main window.
mainWindow = tkinter.Tk()

mainWindow.title("Hello Rohit")
mainWindow.geometry('640x480-52+400')  #'640x480' = screen dimension,'-52' takes it to the right,'+400' brings it down
mainWindow.mainloop()