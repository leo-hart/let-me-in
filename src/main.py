import tkinter as tk
import random
import string

#Generate a random password
def button_click():
    password_length = 5
    custom_punctuation = ''.join(c for c in string.punctuation if c not in ['~', '´', '`', '^'])
    password0 = ''.join(random.choices(string.ascii_letters + string.digits + custom_punctuation, k=password_length)) + "-"
    password1 = ''.join(random.choices(string.ascii_letters + string.digits + custom_punctuation, k=password_length)) + "-"
    password2 = ''.join(random.choices(string.ascii_letters + string.digits + custom_punctuation, k=password_length))
    password = str(password0 + password1 + password2)
    password_label.config(text=password)
    
    label1.config(text="Password copied to clipboard.")
    window.clipboard_clear()
    window.clipboard_append(password)

background_color = "white"
window = tk.Tk()
window.title("Secure Password Generator")
window.geometry("500x450")
window.resizable(False, False)
window.configure(bg=background_color)
frame = tk.Frame(window)

#Fonts
font1 = ("Verdana", 24  )
font2 = ("Arial", 16, 'bold')

#Content
label1 = tk.Label(window, text="Click to generate a strong password.", bg=background_color, pady=50, font=font2)
button = tk.Button(window, text="Generate", command=button_click, font=font1)
password_label = tk.Label(frame, text=" ", bg=background_color, pady=20, font=('Arial', 12, 'bold'))

possible_combinations = tk.Label(window, text="Number of possible combinations: 4.4012667e+31", bg=background_color, font=('Arial', 10))
time_to_bruteforce = tk.Label(window, text="Time to brute force (in days): 6.503742275589586e+21 (over trillions of years)", bg=background_color, font=('Arial', 10))

canvas = tk.Canvas(window, width=450, height=-3)

reminder1 = tk.Label(window, text="Don't forget to store it in a secure folder*", bg=background_color, font=('Arial', 10))
reminder2 = tk.Label(window, text="Never share it with anyone*", bg=background_color, font=('Arial', 10))

label1.pack()
button.pack()
password_label.pack()
frame.pack(pady=20)
possible_combinations.pack()
time_to_bruteforce.pack()
canvas.pack(pady=20)
reminder1.pack()
reminder2.pack()

window.mainloop()