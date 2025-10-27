import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO
from fetch_menus import fetch_menus, fetch_translations, fetch_image_url

def load_data():
    """Fetch and display menu data"""
    try:
        menus = fetch_menus()
        for row in tree.get_children():
            tree.delete(row)
        for menu in menus:
            tree.insert("", "end", values=menu)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch data: {e}")

def on_menu_select(event):
    """Handles menu selection and opens the translations window"""
    selected_item = tree.focus()
    if not selected_item:
        return
    shop_name = tree.item(selected_item)['values'][2]

    try:
        translations = fetch_translations(shop_name)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch translations: {e}")
        return

    # Create a new window to show translations
    trans_window = tk.Toplevel(root)
    trans_window.title(f"Translations - {shop_name}")
    trans_window.geometry("1000x600")  # Adjusted size for better UI

    columns = ("Item ID", "Thai Name", "English Name", "Description", "Image URL")
    trans_tree = ttk.Treeview(trans_window, columns=columns, show="headings")

    for col in columns:
        trans_tree.heading(col, text=col)
        trans_tree.column(col, anchor=tk.CENTER, width=200)

    trans_tree.pack(expand=True, fill='both')

    # Frame for description & image (Side by side layout)
    content_frame = tk.Frame(trans_window)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Description Section
    desc_frame = tk.Frame(content_frame)
    desc_frame.pack(side="left", fill="both", expand=True, padx=10)

    desc_label = tk.Label(desc_frame, text="Item Description:", font=("Arial", 12, "bold"), anchor="w")
    desc_label.pack(anchor="w")

    desc_text = tk.Text(desc_frame, height=10, wrap=tk.WORD, font=("Arial", 11))
    desc_text.pack(expand=True, fill='both', padx=10, pady=5)

    # Image Section
    img_frame = tk.Frame(content_frame)
    img_frame.pack(side="right", fill="both", expand=True, padx=10)

    img_label = tk.Label(img_frame, text="No Image Available", font=("Arial", 10))
    img_label.pack()

    # Insert values into table
    for trans in translations:
        item_id = trans[1]  # Get the Item ID
        thai_name = trans[2]  # Thai Name
        english_name = trans[3]  # English Name
        description = trans[4]  # Correctly fetch the Description from Translation Table
        image_url = fetch_image_url(item_id)  # Fetch the image URL

        trans_tree.insert("", "end", values=(item_id, thai_name, english_name, description, image_url))

    def on_translation_select(event):
        """Updates description and displays image in GUI"""
        selected_trans = trans_tree.focus()
        if not selected_trans:
            return
        item_values = trans_tree.item(selected_trans)['values']

        if len(item_values) < 5:
            return  # No valid data, do nothing

        item_id, thai_name, english_name, description, image_url = item_values

        # Display full description in the text box
        desc_text.delete("1.0", tk.END)  # Clear previous text
        desc_text.insert(tk.END, description)  # Show full description

        # Load and display the image from URL
        if image_url:
            try:
                response = requests.get(image_url, timeout=5)
                response.raise_for_status()
                img_data = BytesIO(response.content)
                img = Image.open(img_data)
                img = img.resize((250, 250), Image.LANCZOS)  # Resize properly
                img_tk = ImageTk.PhotoImage(img)

                img_label.config(image=img_tk, text="")  # Remove text, show image
                img_label.image = img_tk  # Keep a reference to avoid garbage collection

            except requests.exceptions.RequestException:
                img_label.config(image="", text="Image could not be loaded (Invalid URL)")

        else:
            img_label.config(image="", text="No Image Available")

    # Bind event to update description and show image
    trans_tree.bind('<<TreeviewSelect>>', on_translation_select)

# Main GUI Setup
root = tk.Tk()
root.title("Digital Menu System")
root.geometry("700x400")

# Table (Treeview) to display menus
columns = ("Menu ID", "Menu Name", "Shop Name")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200, anchor=tk.CENTER)

tree.pack(pady=20, expand=True, fill='both')

# Bind event to open translations window
tree.bind('<<TreeviewSelect>>', on_menu_select)

# Load button
load_btn = ttk.Button(root, text="Load Menus", command=load_data)
load_btn.pack(pady=10)

# Run the GUI
root.mainloop()
