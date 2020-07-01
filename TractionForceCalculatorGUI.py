
import tkinter as tk
import math

fgcolour = "white"
bgcolour = "#152238"
err_message = ""

#Applies the input dialogs
root = tk.Tk() #creates a body window to work in
root.title("Traction Force Calculator")

#In case I want to use pop up messages in future I kept this
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
        if(float(grad_input.get())>100.0):
            #standard vehicles do not operate above 45 degrees since it is dangerous so we need to make sure we aren't working 45degrees or less
            errmessage = "Gradient must be\nless than 100%"
            tk.Label(frame, fg="#ff0000", bg=bgcolour, text=errmessage).grid(row=16, column=2, sticky="W")
        elif(float(grad_input.get())<0.0):
            #if the gradient is negative it just means it is working in a different direction so just force the user to use a positive value
            errmessage = "Gradient value\nmust be positive"
            tk.Label(frame, fg="#ff0000", bg=bgcolour, text=errmessage).grid(row=16, column=2, sticky="W")
        else:
            #retrieve all the values in a workable format
            vel = float(vel_input.get())
            acc = float(acc_input.get())
            grad = math.atan(float(grad_input.get())/100)
            mass = float(mass_input.get())
            aero = float(aero_input.get())
            roll= float(roll_input.get())
            area = float(area_input.get())
            dens = float(dens_input.get())
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


    except ValueError:
        #if the input value is invalid i.e. is not a float, display an error to the user
        #I haven't figured out how to clear this label yet but I will figure it out when I have time to come back to this
        err_message = "Invalid Value/Empty Field"
        tk.Label(frame, fg="#ff0000", bg=bgcolour, text=err_message).grid(row=16, column=3, sticky="W")

def app_typ():
    #This is to apply typical values for cars for quick calculations
    aero_input.delete(0,"end")
    aero_input.insert(0, "0.29")

    area_input.delete(0, "end")
    area_input.insert(0, "2.2")

    roll_input.delete(0, "end")
    roll_input.insert(0, "0.01")

    mass_input.delete(0, "1200")
    mass_input.insert(0, "1200")

    dens_input.delete(0, "end")
    dens_input.insert(0, "1.25")

#Making the GUI
canvas = tk.Canvas(root, height=500, width=700) #canvas setup
canvas.pack() #Apply Canvas to root

frame = tk.Frame(root, bg=bgcolour) #a frame to use within canvas, nicer to work in for me
#80% of canvas width and height seems to work the best
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #places the frame in the canvas

tk.Label(frame, text="Basic Vehicle Model Calculator", fg=fgcolour, bg=bgcolour).grid(row=0, column=0)
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

vel_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
vel_input.grid(row=3, column=2)

acc_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
acc_input.grid(row=4, column=2)

grad_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
grad_input.grid(row=5, column=2)

mass_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
mass_input.grid(row=6, column=2)

aero_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
aero_input.grid(row=7, column=2)

roll_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
roll_input.grid(row=8, column=2)

area_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
area_input.grid(row=9, column=2)

dens_input = tk.Entry(frame, fg=bgcolour, bg=fgcolour)
dens_input.grid(row=10, column=2)

tk.Label(frame, bg=bgcolour, text="          ").grid(row=11, column=0)
calc_button = tk.Button(frame, text="Calculate", padx=10, pady=5, fg=fgcolour, bg=bgcolour, command=lambda:calc())
calc_button.grid(row=12,column=2)
typi_button = tk.Button(frame, text="Typical Parameters", padx=10, pady=5, fg=fgcolour, bg=bgcolour, command=lambda:app_typ())
typi_button.grid(row=12,column=0)

#label for final output answer and error message
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="").grid(row=13, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="Traction force  = ").grid(row=14, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="").grid(row=15, column=2, sticky="E")
tk.Label(frame, fg=fgcolour, bg=bgcolour, text="Error Message  = ").grid(row=16, column=2, sticky="E")
# tk.Label(frame, fg=bgcolour, bg=bgcolour, text=err_message).grid(row=16, column=3, sticky="W")

root.mainloop() #run the little GUI
