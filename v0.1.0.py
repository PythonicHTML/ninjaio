''' Version 0.0.6 released April 26th, 2022
No external modules currently required. Runs on Python versions 3.5 or above. '''

import tkinter as tk
import random as r
head_list = ["White fire", "Red fire", "Green fire", "Blue fire", "Yellow fire", "Pink fire", "Orange fire", "Cowboy", "Brown cowboy hat", "Black cowboy hat", "Cowboy/black", "Roundshades - black", "Roundshades - green", "Roundshades - pink", "Roundshades - red", "Roundshades - yellow", "Roundshades - blue", "Shades - green", "Shades - blue", "Shades - orange", "Pirate bandana", "Combat helmet", "Combat helmet winter", "Combat helmet jungle", "Combat helmet desert", "Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"]
hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"]
torso = ["Desert camo", "Winter camo", "Jungle camo", "Vest 1", "Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Camo", "Camo 2", "Camo Ammo", "Camo 2 Ammo", "Tech 1", "Tech 2", "Tech 3", "Snow Camo", "Snow Camo RPG", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X", "Purple Camo", "Fire Camo", "Aqua Camo", "Brown Camo"]
right_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
left_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
right_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
left_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
belt = ["Jungle camo", "Winter camo", "Desert camo", "Belt Metal", "Belt Camo", "Belt Plate Full", "Belt Camo Full", "Belt Brown", "Camo Snow", "Belt Purple", "Belt Fire", "Belt Aqua", "Belt Brown Full"]
right_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
left_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
shell = ["Storm", "Bubble", "Fractal", "Dragon", "Jet feet", "Energy vacuum", "Jet feet 2"]
shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"]
right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
cape_list = ["Black", "Green", "Red", "Yellow", "Blue", "Pink", "Orange", "BW camo", "Jungle camo", "Winter camo", "Desert camo"]
def main(first_time=False, shoulders=True, hands=True, legs=True, feet=True, camo_used="All", hair_blockage=True):
    global results_label
    if camo_used == "All":
        head_list = ["White fire", "Red fire", "Green fire", "Blue fire", "Yellow fire", "Pink fire", "Orange fire", "Cowboy", "Brown cowboy hat", "Black cowboy hat", "Cowboy/black", "Roundshades - black", "Roundshades - green", "Roundshades - pink", "Roundshades - red", "Roundshades - yellow", "Roundshades - blue", "Shades - green", "Shades - blue", "Shades - orange", "Pirate bandana", "Combat helmet", "Combat helmet winter", "Combat helmet jungle", "Combat helmet desert", "Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"]
        hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"]
        torso = ["Desert camo", "Winter camo", "Jungle camo", "Vest 1", "Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Camo", "Camo 2", "Camo Ammo", "Camo 2 Ammo", "Tech 1", "Tech 2", "Tech 3", "Snow Camo", "Snow Camo RPG", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X", "Purple Camo", "Fire Camo", "Aqua Camo", "Brown Camo"]
        right_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
        left_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
        right_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
        left_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
        belt = ["Jungle camo", "Winter camo", "Desert camo", "Belt Metal", "Belt Camo", "Belt Plate Full", "Belt Camo Full", "Belt Brown", "Camo Snow", "Belt Purple", "Belt Fire", "Belt Aqua", "Belt Brown Full"]
        right_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
        left_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
        shell = ["Storm", "Bubble", "Fractal", "Dragon", "Jet feet", "Energy vacuum", "Jet feet 2"]
        shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"]
        right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        cape_list = ["Black", "Green", "Red", "Yellow", "Blue", "Pink", "Orange", "BW camo", "Jungle camo", "Winter camo", "Desert camo"]
    elif camo_used == "None":
        head_list = ["White fire", "Red fire", "Green fire", "Blue fire", "Yellow fire", "Pink fire", "Orange fire", "Cowboy", "Brown cowboy hat", "Black cowboy hat", "Cowboy/black", "Roundshades - black", "Roundshades - green", "Roundshades - pink", "Roundshades - red", "Roundshades - yellow", "Roundshades - blue", "Shades - green", "Shades - blue", "Shades - orange", "Pirate bandana", "Combat helmet", "Combat helmet winter", "Combat helmet jungle", "Combat helmet desert", "Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"]
        hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"]        
        torso = ["Vest 1", "Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Tech 1", "Tech 2", "Tech 3", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X"]
        right_shoulder = ["Shoulderpad", "Arm Plate"]
        left_shoulder = ["Shoulderpad", "Arm Plate"]
        right_hand = ["Blade", "Twin blade", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate"]
        left_hand = ["Blade", "Twin blade", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate"]
        belt = ["Belt Metal", "Belt Plate Full", "Belt Brown"]
        right_leg = ["Plates"]
        left_leg = ["Plates"]
        shell = ["Storm", "Bubble", "Fractal", "Dragon", "Jet feet", "Energy vacuum", "Jet feet 2"]
        shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"]
        right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        cape_list = ["Black", "Green", "Red", "Yellow", "Blue", "Pink", "Orange", "BW camo", "Jungle camo", "Winter camo", "Desert camo"]
    elif camo_used == "Neutral":
        head_list = ["White fire", "Red fire", "Green fire", "Blue fire", "Yellow fire", "Pink fire", "Orange fire", "Cowboy", "Brown cowboy hat", "Black cowboy hat", "Cowboy/black", "Roundshades - black", "Roundshades - green", "Roundshades - pink", "Roundshades - red", "Roundshades - yellow", "Roundshades - blue", "Shades - green", "Shades - blue", "Shades - orange", "Pirate bandana", "Combat helmet", "Combat helmet winter", "Combat helmet jungle", "Combat helmet desert", "Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"]
        hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"]
        torso = ["Desert camo", "Winter camo", "Jungle camo", "Vest 1", "Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Camo", "Camo 2", "Camo Ammo", "Camo 2 Ammo", "Tech 1", "Tech 2", "Tech 3", "Snow Camo", "Snow Camo RPG", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X"]
        right_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo"]
        left_shoulder = ["Winter camo", "Desert camo", "Jungle camo", "Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo"]
        right_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow"]
        left_hand = ["Winter camo", "Jungle camo", "Desert camo", "Blade", "Twin blade", "Wrist - winter", "Wrist - jungle", "Wrist - desert", "Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow"]
        belt = ["Jungle camo", "Winter camo", "Desert camo", "Belt Metal", "Belt Camo", "Belt Plate Full", "Belt Camo Full", "Belt Brown", "Camo Snow", "Belt Brown Full"]
        right_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo"]
        left_leg = ["Winter camo", "Jungle camo", "Desert camo", "Plates", "Camo", "Snow Camo"]
        shell = ["Storm", "Bubble", "Fractal", "Dragon", "Jet feet", "Energy vacuum", "Jet feet 2"]
        shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"]
        right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
        cape_list = ["Black", "Green", "Red", "Yellow", "Blue", "Pink", "Orange", "BW camo", "Jungle camo", "Winter camo", "Desert camo"]
    else:
        pass

    my_head = r.choice(head_list)
    my_hair = r.choice(hair_list)
    my_torso = r.choice(torso)
    my_shoulder = r.choice(right_shoulder)
    if shoulders == True:
        my_other_shoulder = my_shoulder
    else:
        my_other_shoulder = r.choice(left_shoulder)
    my_hand = r.choice(right_hand)
    if hands == True:
        my_other_hand = my_hand
    else:
        my_other_hand = r.choice(left_hand)
    my_belt = r.choice(belt)
    my_leg = r.choice(right_leg)
    if legs == True:
        my_other_leg = my_leg
    else:
        my_other_leg = r.choice(left_leg)
    my_shell = r.choice(shell)
    my_color = r.choice(shell_color)
    my_foot = r.choice(right_foot)
    if feet == True:
        my_other_foot = my_foot
    else:
        my_other_foot = r.choice(left_foot)
    cape = r.choice(cape_list)
    if first_time == True:
        results_label = tk.Label(root, font=('Stencil', 14), bg='#176ca5', relief='raised', text=("Face: " + my_head + "\nHair Style: " + my_hair + "\nTorso: " + my_torso + "\nRight shoulder: " + my_shoulder + "\nLeft shoulder: " + my_other_shoulder + "\nRight hand: " + my_hand + "\nLeft hand: " + my_other_hand + "\nBelt: " + my_belt + "\nRight leg: " + my_leg + "\nLeft leg: " + my_other_leg + "\nFlight aura: " + my_shell + "\nFlight Aura Color: " + my_color + "\nRight Foot: " + my_foot + "\nLeft Foot: " + my_other_foot)) 
        results_label.place(relx=0.5, rely=0.3, anchor='center')
    elif first_time == False:
        results_label.destroy()
        results_label = tk.Label(root, font=('Stencil', 14), bg='#176ca5', relief='raised', text=("Face: " + my_head + "\nHair Style: " + my_hair + "\nTorso: " + my_torso + "\nRight shoulder: " + my_shoulder + "\nLeft shoulder: " + my_other_shoulder + "\nRight hand: " + my_hand + "\nLeft hand: " + my_other_hand + "\nBelt: " + my_belt + "\nRight leg: " + my_leg + "\nLeft leg: " + my_other_leg + "\nFlight aura: " + my_shell + "\nFlight Aura Color: " + my_color + "\nRight Foot: " + my_foot + "\nLeft Foot: " + my_other_foot)) 
        results_label.place(relx=0.5, rely=0.3, anchor='center')

        
root = tk.Tk()
root.config(bg='#6E6B6C')
root.geometry('800x600+150+25')
root.title('Beta v0.1.0')
gen_button = tk.Button(root, text='Generate', bg='#176ca5', width=8, font=('Stencil', 25), command=lambda: [destroy_button(gen_button), main(first_time=True)])
gen_button.place(relx=0.5, rely=0.8, anchor='center')
def destroy_button(param):
    gen_button.destroy()
    new_button = tk.Button(root, text='Generate', bg='#176ca5', width=8, font=('Stencil', 25), command=lambda: main(first_time=False))
    new_button.place(relx=0.5, rely=0.8, anchor='center')
