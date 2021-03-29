# libraries
from tkinter import *
from WeaponTypes import *

# information needed from GUI:
# Element
# HP Value
# Turn
# Magna/Premium/Elemental Summons

# ============================ GUI code ===================================
# initialization
top = Tk()

# widget code
L1 = Label(top, text = "Input Here")
L1.pack(side = LEFT)


E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)


# main loop to run GUI
top.mainloop()
# ============================ END GUI ===================================


# testing accessing the dictionary of skill values
# prints "12"
print(WeaponSkillDict[('Normal', 'Atk', 'Small', 15)])