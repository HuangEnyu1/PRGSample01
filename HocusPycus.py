#Huang Enyu #S10274277E
print("Available spells: \n1. Rain of Fire\n2. Ice Lance\n3. Teleport\n4. Mana Wand\n5. Arcane Missle")
print("\n")
#INPUT
spell_list=["Rain of Fire","Ice Lance","Teleport","Mana Wand","Arcane Missle"]
spell=input("Enter 5 spell numbers for activation (space-seperated): ")
print("\n")
#------BEGIN PROCESSING-------
spell=spell.split(" ") # make the player input into a list by speerating the space
#-------END PROCESSING--------
#OUTPUT
#Use Spell as an index for spell_list and integer the string to ensure no index error. Minus the spell by 1 to ensure that it is affecting the proper index
print("Activation Sequence:\n{}\n{}\n{}\n{}\n{}".format(spell_list[int(spell[0])-1],spell_list[int(spell[1])-1],spell_list[int(spell[2])-1],spell_list[int(spell[3])-1],spell_list[int(spell[4])-1])) 
print("\n")
print("Ultimate Secret Spell: {} + {} + {}".format(spell_list[int(spell[0])-1],spell_list[int(spell[2])-1],spell_list[int(spell[4])-1]))



