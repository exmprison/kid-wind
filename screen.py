import tkinter

FONT_MAIN = ("Helvetica", 36)
BG_MAIN = "black"
FG_MAIN = "white"
BG_BOX = "white"
FG_BOX = "black"
PAD_X = 20
PAD_Y = 5
window = tkinter.Tk()
window.title("Wind Power Station")
window.minsize(width=1100, height=450)
window.config(padx=20, pady=30, bg="black")


row_1 = tkinter.Label(text="Power", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_1.grid(column=1, row=1, pady=PAD_Y, sticky="E")
row_1_box = tkinter.Label(text="0.00", fg=FG_BOX, bg=BG_BOX, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_1_box.grid(column=2, row=1, pady=PAD_Y)
row_1_units = tkinter.Label(text="Watts", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_1_units.grid(column=3, row=1, pady=PAD_Y, sticky="W")

row_2 = tkinter.Label(text="Current", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_2.grid(column=1, row=2, pady=PAD_Y, sticky="E")
row_2_box = tkinter.Label(text="0.00", fg=FG_BOX, bg=BG_BOX, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_2_box.grid(column=2, row=2, pady=PAD_Y)
row_2_units = tkinter.Label(text="milli Amps", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_2_units.grid(column=3, row=2, pady=PAD_Y, sticky="W")

row_3 = tkinter.Label(text="Voltage", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_3.grid(column=1, row=3, pady=PAD_Y, sticky="E")
row_3_box = tkinter.Label(text="0.00", fg=FG_BOX, bg=BG_BOX, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_3_box.grid(column=2, row=3, pady=PAD_Y)
row_3_units = tkinter.Label(text="Volts", fg=FG_MAIN, bg=BG_MAIN, font=FONT_MAIN, padx=PAD_X, pady=PAD_Y)
row_3_units.grid(column=3, row=3, pady=PAD_Y, sticky="W")


window.mainloop()
