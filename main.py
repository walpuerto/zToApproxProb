# Z-score to Approximate Probability
# Version 0.2
# By noob_undone

def isValidFloat(value):
    try: float(value)
    except: return False
    else: return True

def updateText(input):
    if isValidFloat(input):
        zScore = input
        t4.config(text=f"Probability of Z-score {zScore} is: {precomputed.getProbabilityFromZ(zScore)}")
    else:
        t4.config(text=f"{input} is not a valid input.")

import precomputed
import tkinter
m = tkinter.Tk()
m.geometry("400x300")
m.title('Z-score to Approximate Probability')

# Prepare GUI
t1 = tkinter.Label(m, text="Z-score to Approximate Probability", font=("Calibri", 15, "bold"))
t1.pack(pady=5)

t2 = tkinter.Label(m, text="Version 0.2", font=("Calibri", 15, "bold"))
t2.pack()

spacer1 = tkinter.Label(m, text="")
spacer1.pack(pady=15)

t3 = tkinter.Label(m, text="Enter Z-score", font=("Calibri", 12))
t3.pack()

e1 = tkinter.Entry(m, width=30, font=("Calibri", 12))
e1.pack()

b1 = tkinter.Button(m, text="Calculate", font=("Calibri", 12), command=lambda: updateText(e1.get()))
b1.pack(pady=5)

spacer1 = tkinter.Label(m, text="")
spacer1.pack(pady=3)

t4 = tkinter.Label(m, text="", font=("Calibri", 12))
t4.pack()

m.mainloop()