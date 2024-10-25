# class Fraction:
#     def __init__(self, numer, denom):
#         self._numer = numer
#         self._denom = denom

#     def __eq__(self, other):
#         a, b = self._numer, self._denom
#         c, d = other._numer, other._denom
#         return a * d == b * c


# p = Fraction(2, 3)
# q = Fraction(4, 6)
# print(bool(p == q))


# class Fraction:
#     def __init__(self, numer, denom):
#         self._numer = numer
#         self._denom = denom

#     def __add__(self, other):
#         a, b = self._numer, self._denom
#         c, d = other._numer, other._denom
#         return Fraction(a * d + c * b, b * d)


# p = Fraction(2, 3)
# q = Fraction(1, 2)
# print(p + q)

# C(B).fg(self) = super().fg() * self.y
# super().fg() = self.f() - self.g()
# b.f() = self.x, b.g() = self.x **2
# c.f() = self.x, c.g() = se.f.x **2


import tkinter as tk

# window = tk.Tk()

# alice = tk.Label(text="Alice", background="pink")
# alice.pack(fill=tk.BOTH)

# tk.mainloop()

# root = tk.Tk()
# root.geometry("400x400")
# frame = tk.Frame(root)
# frame.pack(side=tk.TOP)

# alice = tk.Label(frame, text="Alice", background="yellow")
# alice.pack(side=tk.LEFT)
# bob = tk.Label(frame, text="Bob", bg="purple")
# bob.pack(side=tk.RIGHT)

# tk.mainloop()

# import tkinter as tk


# def handler(event):
#     global label
#     label.config(text=f"{event.char}, {event.keysym}, {event.keycode}")


# root = tk.Tk()
# root.geometry("300x300")

# label = tk.Label(root, text="0, 0, 0")
# label.pack(expand=tk.TRUE)

# root.bind_all("<Key>", handler)

# root.mainloop()

# from tkinter import messagebox  # importing a submodule

# mbox = messagebox.showinfo(title="Title", message="Hello World")
# messagebox.showwarning(title=None, message="what the fuck???")
# Title is OS specific; OSX doesn't display it.

# from typing import Callable
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import filedialog


# def bg_change(colour: str) -> Callable:
#     def handler():
#         root.config(bg=colour)
#         label.config(bg=colour)

#     return handler


# def fg_change(colour: str) -> Callable:
#     def handler():
#         label.config(fg=colour)

#     return handler


# root = tk.Tk()
# root.geometry("201x201")

# label = tk.Label(
#     text="Squid Game",
#     font=("Courier", 20),
# )

# label.pack(expand=tk.TRUE)

# menu = tk.Menu(root)
# root.config(menu=menu)

# # Customize >
# customize_menu = tk.Menu(menu)
# menu.add_cascade(label="Customize", menu=customize_menu)

# # Customize > Background >
# bg_colours_menu = tk.Menu(customize_menu)
# customize_menu.add_cascade(label="Background", menu=bg_colours_menu)

# # Customize > Background > Red
# bg_colours_menu.add_command(label="Red", command=bg_change("red"))

# # Customize > Background > Blue
# bg_colours_menu.add_command(label="Blue", command=bg_change("blue"))

# # Customize > Background > Green
# bg_colours_menu.add_command(label="Green", command=bg_change("green"))

# # Customize > Foreground >
# fg_colours_menu = tk.Menu(customize_menu)
# customize_menu.add_cascade(label="Foreground", menu=fg_colours_menu)

# # Customize > Foreground > Red
# fg_colours_menu.add_command(label="Red", command=fg_change("red"))

# # Customize > Foreground > Blue
# fg_colours_menu.add_command(label="Blue", command=fg_change("blue"))

# # Customize > Foreground > Green
# fg_colours_menu.add_command(label="Green", command=fg_change("green"))

# root.mainloop()
root = tk.Tk()

canvas = tk.Canvas(root, width=100, heigh=100, bg="pink")

canvas.create_line(50, 50, 100, 100, fill="blue", width=10)

canvas.pack()

root.mainloop()
