# Z-score to Approximate Probability
# Version 0.3
# By noob_undone

def isValidInput(value):
    try: float(value)
    except: return False
    else: return True

def updateTextZ(input):
    if isValidInput(input):
        zScore = input
        if precomputed.getProbabilityFromZ(zScore):
            t4.config(text=f"Probability of Z-score {zScore} is: {precomputed.getProbabilityFromZ(zScore)}")
    else:
        t4.config(text=f"Error: {input} is not a valid input.")

def updateTextP(input):
    if isValidInput(input) and 0 <= float(input) <= 0.5:
        probability = input
        if precomputed.getZFromProbability(probability):
            t6.config(text=f"Z-score of Probability {probability} is: {precomputed.getZFromProbability(probability)}")
    else:
        t6.config(text=f"Error: {input} is not a valid input.")

import precomputed
import tkinter
m = tkinter.Tk()
m.geometry("400x500")
m.title('Z-score to Approximate Probability')

# Prepare GUI
t1 = tkinter.Label(m, text="Z-score to Approximate Probability", font=("Calibri", 15, "bold"))
t1.pack(pady=5)

t2 = tkinter.Label(m, text="Version 0.2", font=("Calibri", 15, "bold"))
t2.pack()

spacer1 = tkinter.Label(m, text="")
spacer1.pack(pady=15)

# ZScore Input

t3 = tkinter.Label(m, text="Enter Z-score", font=("Calibri", 12))
t3.pack()

e1 = tkinter.Entry(m, width=30, font=("Calibri", 12))
e1.pack()

b1 = tkinter.Button(m, text="Calculate", font=("Calibri", 12), command=lambda: updateTextZ(e1.get()))
b1.pack(pady=5)

spacer2 = tkinter.Label(m, text="")
spacer2.pack(pady=3)

t4 = tkinter.Label(m, text="", font=("Calibri", 12), fg="red")
t4.pack()

spacer3 = tkinter.Label(m, text="")
spacer3.pack(pady=15)

# Probability Input

t5 = tkinter.Label(m, text="Enter Probability", font=("Calibri", 12))
t5.pack()

e2 = tkinter.Entry(m, width=30, font=("Calibri", 12))
e2.pack()

b2 = tkinter.Button(m, text="Calculate", font=("Calibri", 12), command=lambda: updateTextP(e2.get()))
b2.pack(pady=5)

spacer4 = tkinter.Label(m, text="")
spacer4.pack(pady=3)

t6 = tkinter.Label(m, text="", font=("Calibri", 12), fg="red")
t6.pack()

m.mainloop()