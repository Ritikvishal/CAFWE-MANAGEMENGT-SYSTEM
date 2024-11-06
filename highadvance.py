import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Install pillow if you haven't already

# Define the menu of the cafe
menu = {
    'Simple Pizza': 199,
    'Cheese Pizza': 249,
    'Regular Pizza': 299,
    'Paneer Pizza': 299,
    'Mushroom Pizza': 399,
    'Sandwich': 149,
    'Cheese Sandwich': 299,
    'Burger': 99,
    'Cheese Burger': 149,
    'Garlic Bread': 99,
    'Water': 20,
    'Coke': 40,
    'Mint Mojito': 99,
    'Normal Tea': 49,
    'Masala Tea': 99,
    'Coffee': 149,
    'Cold Coffee': 99,
    'French Fries': 49,
    'Noodles': 149,
}

# Initialize order total
order_total = 0

# Function to add item to order
def add_item():
    global order_total
    item = item_entry.get()
    if item in menu:
        order_total += menu[item]
        order_label.config(text=f"Total Amount: Rs {order_total}")
        messagebox.showinfo("Success", f"Your item '{item}' has been added to your order.")
    else:
        messagebox.showwarning("Unavailable", f"Sorry, '{item}' is not available in the menu.")

# Function to finish order
def finish_order():
    messagebox.showinfo("Order Complete", f"The total amount to pay is: Rs {order_total}")
    root.destroy()

# Setting up the GUI
root = tk.Tk()
root.title("Cafe Management System")
root.geometry("400x400")

# Set background image
bg_image = Image.open(r"D:\clg python\PROJECTS\abc.jpg")  # Replace with your background image file path
bg_image = bg_image.resize((1500,1500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Font style
font_title = ("Pacifico", 24)  # Unique title font
font_text = ("Pacifico", 14)    # Unique text font


# Greeting
greeting_label = tk.Label(root, text="Welcome to Loving Cafe", font=font_title, bg="#f0e4d7")
greeting_label.pack(pady=10)

# Display Menu
menu_label = tk.Label(root, text="Menu:", font=("Arial", 12, "bold"), bg="#f0e4d7")
menu_label.pack()

menu_text = "\n".join([f"{item}: Rs{price}" for item, price in menu.items()])
menu_display = tk.Label(root, text=menu_text, justify="left", bg="#f0e4d7", font=font_text)
menu_display.pack()

# Entry field for item
item_label = tk.Label(root, text="Enter the name of the item you want to order:", font=font_text, bg="#f0e4d7")
item_label.pack(pady=5)

item_entry = tk.Entry(root, width=30, font=font_text)
item_entry.pack(pady=5)

# Button to add item to order
add_button = tk.Button(root, text="Add Item", command=add_item, font=font_text)
add_button.pack(pady=10)

# Label to show the current order total
order_label = tk.Label(root, text="Total Amount: Rs 0", font=font_text, bg="#FFFDD0")
order_label.pack(pady=10)

# Button to finish order
finish_button = tk.Button(root, text="Finish Order", command=finish_order, font=font_text)
finish_button.pack(pady=10)

# Ensure background image appears behind all widgets
bg_label.lower()

# Run the GUI
root.mainloop()
