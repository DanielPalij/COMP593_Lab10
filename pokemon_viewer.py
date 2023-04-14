import poke_api
import os
from tkinter import *
from tkinter import ttk
import ctypes
import image_lib

# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

# Make the image cache folder if it doesnt exist
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the window
root = Tk()
root.title("Pokemon Image Viewer")
root.configure(bg='#856ff8')

# Set the window icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
icon_path = os.path.join(script_dir, 'Poke-Ball.ico')
root.iconbitmap(icon_path)

#create the frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# add the image to frame
img_poke = PhotoImage(file=os.path.join(script_dir, 'pokemon-logo.png'))
lbl_poke = ttk.Label(frame, image=img_poke)
lbl_poke.grid(row=0, column=0)

# Add the pokemon pulldown list
pokemon_name_list = poke_api.get_pokemon_names()
cbox_poke_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_poke_names.set("Select a Pokemon")
cbox_poke_names.grid(row=1, column=0, padx=10, pady=10)

def handle_pokemon_sel(event):
    
    # Get the name of the selected pokemon
    pokemon_name = cbox_poke_names.get()
    
    # Download and save art of selected pokemon
    global image_path
    image_path = poke_api.download_pokemon_artwork(pokemon_name, image_cache_dir)
    
    # Display poke art
    if image_path is not None:
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

cbox_poke_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)


def btn_set_desktop_img():

    image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frame, text='Set As Desktop Image', command=btn_set_desktop_img, state=DISABLED)
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()