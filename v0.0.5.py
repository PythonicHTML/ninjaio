''' Version 0.0.5 released April 26th, 2022
No external modules currently required. Runs on Python versions 2.7 and 3.5 or above. '''


import random as r
head_list = ["Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"]
hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"]
torso = ["Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Camo", "Camo 2", "Camo Ammo", "Camo 2 Ammo", "Tech 1", "Tech 2", "Tech 3", "Snow Camo", "Snow Camo RPG", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X", "Purple Camo", "Fire Camo", "Aqua Camo", "Brown Camo"]
right_shoulder = ["Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
left_shoulder = ["Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
right_hand = ["Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
left_hand = ["Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"]
belt = ["Belt Metal", "Belt Camo", "Belt Plate Full", "Belt Camo Full", "Belt Brown", "Camo Snow", "Belt Purple", "Belt Fire", "Belt Aqua", "Belt Brown Full"]
right_leg = ["Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
left_leg = ["Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"]
shell = ["Storm", "Bubble", "Fractal"]
shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"]
right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"]
def main(shoulders=True, hands=True, feet=True):
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
    if feet == True:
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
    print("Face: ", my_head)
    print("Hair Style: ", my_hair)
    print("Torso: ", my_torso)
    print("Right shoulder: ", my_shoulder)
    print("Left shoulder: ", my_other_shoulder)
    print("Right hand: ", my_hand)
    print("Left hand: ", my_other_hand)
    print("Belt: ", my_belt)
    print("Right leg: ", my_leg)
    print("Left leg: ", my_other_leg)
    print("Flight aura: ", my_shell)
    print("Flight aura color: ", my_color)
    print("Right foot: ", my_foot)
    print("Left foot: ", my_other_foot)
main()
