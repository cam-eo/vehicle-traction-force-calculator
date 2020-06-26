
import tkinter as tk
import math

fgcolour = "white"
bgcolour = "#152238"

#Applies the input dialogs
root = tk.Tk() #creates a body window to work in
root.title("Traction Force Calculator")

# def popupmessage(popmsg):
#     popup = tk.Tk();
#     popup.wm_title("Error!")
#     poplabel = tk.Label(popup, text=popmsg)
#     poplabel.pack(side="top", fill="x", pady=10)
#     popButton = tk.Button(popup, text="Okay", command=popup.destroy, padx=5, pady=5)
#     popButton.pack()
#     popup.mainloop()


def calc():

    try:
        # get all the variables in a workable float format (convert string inputs)
        if(float(gradInput.get())>100.0):
            #standard vehicles do not operate above 45 degrees since it is dangerous so we need to make sure we aren't working 45degrees or less
            errmessage = "Gradient must be\nless than 100%"
            tk.Label(frame, fg="#ff0000", bg=bgcolour, text=errmessage).grid(row=16, column=2, sticky="W")
        elif(float(gradInput.get())<0.0):
            #if the gradient is negative it just means it is working in a different direction so just force the user to use a positive value
            errmessage = "Gradient value\nmust be positive"
            tk.Label(frame, fg="#ff0000", bg=bgcolour, text=errmessage).grid(row=16, column=2, sticky="W")
        else:
            #retrieve all the values in a workable format
            vel = float(velInput.get())
            acc = float(accInput.get())
            grad = math.atan(float(gradInput.get())/100)
            mass = float(massInput.get())
            aero = float(aeroInput.get())
            roll= float(rollInput.get())
            area = float(areaInput.get())
            dens = float(densInput.get())
            #Calculate force due to aerodynamics drag
            faero = aero*area*((dens*(vel**2))/2)
            #Calculate force due to rolling resistance
            froll = 0.0
            if(vel != 0.0):
                froll = roll*mass*9.81*math.cos(grad)

            #Calculate the force due to gradient of slope
            fgrad = mass*9.81*math.sin(grad)
            #Calculate the force due to acceleration of the vehicle
            fnet = mass*acc
            #Finally calculate the final traction force
            ftrac = round(faero+fgrad+froll+fnet, 2)

            tracforcestring = str(ftrac) + "N"
            tk.Label(frame, fg=fgcolour, bg=bgcolour, text=tracforcestring).grid(row=14, column=3, sticky="W")


    except ValueError as ve:
        #if the input value is invalid i.e. is not a float, display an error to the user
        errmessage = "Invalid Value/Empty Field"
        tk.Label(frame, fg="#ff0000", bg=bgcolour, text=errmessage).grid(row=16, column=3, sticky="W")



def appTy():
    #This is to apply typical values for cars for quick calculations
    aeroInput.delete(0,"end")
    aeroInput.insert(0, "0.29")

    areaInput.delete(0, "end")
    areaInput.insert(0, "2.2")

    rollInput.delete(0, "end")
    rollInput.insert(0, "0.01")

    massInput.delete(0, "1200")
    massInput.insert(0, "1200")

    densInput.delete(0, "end")
    densInput.insert(0, "1.25")

#Making the GUI
canvas = tk.Canvas(root, height=500, width=700) #canvas setup
canvas.pack() #Apply Canvas to root

frame = tk.Frame(root, bg=bgcolour) #a frame to use within canvas, nicer to work in for me
#80% of canvas width and height seems to work the best
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #places the frame in the canvas

title = tk.Label(frame, text="Basic Vehicle Model Calculator", fg=fgcolour, bg=bgcolour).grid(row=0, column=0)
tk.Label(frame, bg=bgcolour, text="          ").grid(row=1, column=0)
tk.Label(frame, bg=bgcolour, text=" ").grid(row=0, column=1)
tk.Label(frame, bg=bgcolour, text=" ").grid(row=2, column=0)
tk.Label(frame, text="Velocity", fg=fgcolour, bg=bgcolour).grid(row=3, column=0, sticky="E")
tk.Label(frame, text="Acceration", fg=fgcolour, bg=bgcolour).grid(row=4, column=0, sticky="E")
tk.Label(frame, text="Gradient", fg=fgcolour, bg=bgcolour).grid(row=5, column=0, sticky="E")
tk.Label(frame, text="Vehicle Mass", fg=fgcolour, bg=bgcolour).grid(row=6, column=0, sticky="E")
tk.Label(frame, text="Aero Drag Coefficient", fg=fgcolour, bg=bgcolour).grid(row=7, column=0, sticky="E")
tk.Label(frame, text="Roll Drag", fg=fgcolour, bg=bgcolour).grid(row=8, column=0, sticky="E")
tk.Label(frame, text="Surface Area", fg=fgcolour, bg=bgcolour).grid(row=9, column=0, sticky="E")
tk.Label(frame, text="Air Density", fg=fgcolour, bg=bgcolour).grid(row=10, column=0, sticky="E")
#labels to display the units that the values need to be in
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="m/s").grid(row=3, column=3, sticky="W")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="m/s^2").grid(row=4, column=3, sticky="W")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="%").grid(row=5, column=3, sticky="W")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="kg").grid(row=6, column=3, sticky="W")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="m^2").grid(row=9, column=3, sticky="W")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="kg/m^3").grid(row=10, column=3, sticky="W")

velInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
velInput.grid(row=3, column=2)

accInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
accInput.grid(row=4, column=2)

gradInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
gradInput.grid(row=5, column=2)

massInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
massInput.grid(row=6, column=2)

aeroInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
aeroInput.grid(row=7, column=2)

rollInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
rollInput.grid(row=8, column=2)

areaInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
areaInput.grid(row=9, column=2)

densInput = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
densInput.grid(row=10, column=2)

tk.Label(frame, bg=bgcolour, text="          ").grid(row=11, column=0)
calcButton = tk.Button(frame, text="Calculate", padx=10, pady=5, fg=fgcolour, bg=bgcolour, command=lambda:calc())
calcButton.grid(row=12,column=2)
typiButton = tk.Button(frame, text="Typical Parameters", padx=10, pady=5, fg=fgcolour, bg=bgcolour, command=lambda:appTy())
typiButton.grid(row=12,column=0)

#label for final output answer and error message
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="").grid(row=13, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="Traction force  = ").grid(row=14, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="").grid(row=15, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="Error Message  = ").grid(row=16, column=2, sticky="E")

root.mainloop() #run the little GUI







