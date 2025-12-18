import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
print('default root before creating Tk:', tk._default_root)
root = tk.Tk()
root.title("🧠MathsCraft")
print('default root after creating Tk:', tk._default_root)
print('root title:', root.title())
root.destroy()
print('destroyed root; default root now:', tk._default_root)
