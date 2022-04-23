
head_list = ["Red Eye", "Blue Eye", "Yellow Eye", "Green Eye", "Red Shades", "Purple Shades", "Yellow Shades", "Shades", "Black Scarf", "Scarf and Shades", "Red Scarf"];
hair_list = ["Long", "Goku", "Dreads", "Frizzy", "Conan", "Short", "Spikes", "Straight", "Wild", "Surfer", "Slick", "Messy", "Punk", "Santa"];
torso = ["Ak-47 Ammo", "M16 Ammo", "Ak-47 Dual", "M16 Dual", "RPG Ammo", "Linkgun Ammo", "M79 Ammo", "Camo", "Camo 2", "Camo Ammo", "Camo 2 Ammo", "Tech 1", "Tech 2", "Tech 3", "Snow Camo", "Snow Camo RPG", "Shuriken", "Silver Chain", "Gold Chain", "White X", "Blue X", "Red X", "Green X", "Yellow X", "Purple Camo", "Fire Camo", "Aqua Camo", "Brown Camo"];
right_shoulder = ["Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"];
left_shoulder = ["Camoflague", "Shoulderpad", "Arm Plate", "Snow Camo", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"];
right_hand = ["Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"];
left_hand = ["Wolverine", "Glove Grey", "Glove Brown", "Glove Metal", "Camo", "Wrist Blue", "Wrist Green", "Wrist Yellow", "Wrist Red", "Wrist Pink", "Wrist Navy", "Glove Red", "Glove Yellow", "Glove Marine", "Glove Pink", "Glove Green", "Plate", "Camo Snow", "Camo Purple", "Camo Fire", "Camo Aqua", "Camo Brown"];
belt = ["Belt Metal", "Belt Camo", "Belt Plate Full", "Belt Camo Full", "Belt Brown", "Camo Snow", "Belt Purple", "Belt Fire", "Belt Aqua", "Belt Brown Full"];
right_leg = ["Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"];
left_leg = ["Plates", "Camo", "Snow Camo", "Purple Camo", "Fire", "Aqua", "Brown Camo"];
shell = ["Storm", "Bubble", "Fractal"];
shell_color = ["Blue", "Red", "Pink", "Magenta", "Turquoise", "Green", "Teal", "Cyan", "Orange", "Navy"];
right_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"];
left_foot = ["Spikes", "Plates", "Boot", "Boot 2", "Rings", "Rings Gold", "Rings Pink", "Rings Green", "Rings Red", "Wrap", "Camo Wrap", "Wrap Red", "Wrap Blue", "Wrap Gold", "Wrap Green", "Boot Black"];
function choose(choices) {
  var index = Math.floor(Math.random() * choices.length);
  return choices[index];
}

function main(equivalent=true, hand=true){
    my_head = choose(head_list);
    my_hair = choose(hair_list);
    my_torso = choose(torso);
    my_shoulder = choose(right_shoulder);
    if (equivalent == true) {
        my_other_shoulder = my_shoulder;
    } else {
        my_other_shoulder = choose(left_shoulder);
    }
    my_hand = choose(right_hand);
    if (hand == true) {
        my_other_hand = my_hand;
    } else {
        my_other_hand = r.choice(left_hand);
    }
    my_belt = choose(belt);
    my_leg = choose(right_leg);
    if (equivalent == true) {
        my_other_leg = my_leg;
    } else {
        my_other_leg = r.choice(left_leg);
    }
    my_shell = choose(shell);
    my_color = choose(shell_color);
    my_foot = choose(right_foot);
    if (equivalent == true) {
        my_other_foot = my_foot;
    } else {
        my_other_foot = r.choice(left_foot);
    }
    console.log("Face: ", my_head);
    console.log("Hair Style: ", my_hair);
    console.log("Torso: ", my_torso);
    console.log("Right shoulder: ", my_shoulder);
    console.log("Left shoulder: ", my_other_shoulder);
    console.log("Right hand: ", my_hand);
    console.log("Left hand: ", my_other_hand);
    console.log("Belt: ", my_belt);
    console.log("Right leg: ", my_leg);
    console.log("Left leg: ", my_other_leg);
    console.log("Flight aura: ", my_shell);
    console.log("Flight aura color: ", my_color);
    console.log("Right foot: ", my_foot);
    console.log("Left foot: ", my_other_foot);
}
main(equivalent=true, hand=false);
