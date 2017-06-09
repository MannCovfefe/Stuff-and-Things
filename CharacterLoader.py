#!/usr/bin/env python

try:
    import sys,re,mysql.connector,base64,subprocess,os,shutil,random
except:
    sys.exit("Import error!")
    
#Load NPCs

#Barbarians
Ophren_Cleave = {'Race':'Gnome', 'Stats':{'Dex':9,'Int':19,'Wis':11,'Str':12,'Cha':11,'Con':10}, 'Name':{'First':'Ophren', 'Last':'Cleave'}, 'Gender':'m', 'Age':'35', 'Hair-Colour':'Grey', 'Weapon':'Great Sword', 'Class':'Barbarian', 'Eye-Colour':'Black'}
Sera_Warsong = {'Race':'Elf', 'Stats':{'Dex':21,'Cha':18,'Int':19,'Wis':13,'Str':13,'Con':13}, 'Name':{'First':'Sera', 'Last':'Warsong'}, 'Gender':'f', 'Age':'85', 'Hair-Colour':'Black', 'Weapon':'Rapier', 'Class':'Barbarian', 'Eye-Colour':'Grey'}
Ophren_Copperback = {'Race':'Dragonbourne', 'Stats': {'Dex': 7, 'Cha': 11, 'Int': 17, 'Wis': 13, 'Str': 23, 'Con':21}, 'Name':{'First':'Ophren', 'Last':'Copperback'}, 'Gender':'m', 'Age':'18', 'Hair-Colour':'Copper', 'Weapon':'Pole Axe', 'Class':'Barbarian', 'Eye-Colour':'Black'}
Zaak_Mithrilfist = {'Race': 'Dwarf', 'Stats': {'Dex': 11, 'Cha': 18, 'Int': 10, 'Wis': 13, 'Str': 20, 'Con':21}, 'Name':{'First':'Zaak', 'Last':'Mithrilfist'}, 'Gender': 'm', 'Age': '27', 'Hair-Colour': 'Grey', 'Weapon': 'Katana', 'Class': 'Barbarian', 'Eye-Colour': 'Grey'}

#Bards
Vivian_Silvest = {'Race': 'Half Elf', 'Stats': {'Dex': 11, 'Cha': 19, 'Int': 10, 'Wis': 6, 'Str': 15, 'Con':6}, 'Name':{'First':'Vivian', 'Last':'Silvest'}, 'Gender': 'f', 'Age': '43', 'Hair-Colour': 'Blonde', 'Weapon': 'Rapier', 'Class': 'Bard', 'Eye-Colour': 'Green'}
Ione_Gemdance = {'Race': 'Gnome', 'Stats': {'Dex': 7, 'Cha': 9, 'Int': 11, 'Wis': 18, 'Str': 10, 'Con':10}, 'Name': {'First':'Ione', 'Last':'Gemdance'}, 'Gender': 'f', 'Age': '21', 'Hair-Colour': 'Blonde', 'Weapon': 'Katana', 'Class': 'Bard', 'Eye-Colour': 'Blue'}
Ophelia_Silvervien = {'Race': 'Dragonbourne', 'Stats': {'Dex': 7, 'Cha': 12, 'Int': 13, 'Wis': 7, 'Str': 10, 'Con':12}, 'Name':{'First':'Ophelia', 'Last':'Silvervien'}, 'Gender': 'f', 'Age': '19', 'Hair-Colour': 'Silver', 'Weapon': 'Long Sword', 'Class': 'Bard', 'Eye-Colour': 'Black'}
Tye_Lingon = {'Race': 'Human', 'Stats': {'Dex': 18, 'Cha': 19, 'Int': 14, 'Wis': 17, 'Str': 8, 'Con':11}, 'Name':{'First':'Tye', 'Last':'Lingon'}, 'Gender': 'm', 'Age': '21', 'Hair-Colour': 'Red', 'Weapon': 'Bo Staff', 'Class': 'Bard', 'Eye-Colour': 'Blue'}

#Clerics
Ana_Harroweth = {'Race': 'Half Elf', 'Stats': {'Dex': 11, 'Cha': 13, 'Int': 12, 'Wis': 14, 'Str': 15, 'Con':16}, 'Name':{'First':'Ana', 'Last':'Harroweth'}, 'Gender': 'f', 'Age': '25', 'Hair-Colour': 'White', 'Weapon': 'Nun Chaku', 'Class': 'Cleric', 'Eye-Colour': 'Blue'}
Azoth_Glimmertouch = {'Race': 'Gnome', 'Stats': {'Dex': 10, 'Cha': 15, 'Int': 13, 'Wis': 18, 'Str': 13, 'Con':14}, 'Name':{'First':'Azoth', 'Last':'Glimmertouch'}, 'Gender': 'm', 'Age': '26', 'Hair-Colour': 'Bald', 'Weapon': 'Single Sickle', 'Class': 'Cleric', 'Eye-Colour': 'Hazel'}
Wes_Vernia = {'Race': 'Halfling', 'Stats': {'Dex': 18, 'Cha': 19, 'Int': 16, 'Wis': 8, 'Str': 13, 'Con':17}, 'Name':{'First':'Wes', 'Last':'Vernia'}, 'Gender': 'm', 'Age': '35', 'Hair-Colour': 'Bald', 'Weapon': 'Flail', 'Class': 'Cleric', 'Eye-Colour': 'Blue'}
Wes_Goldfinger = {'Race': 'Dwarf', 'Stats': {'Dex': 9, 'Cha': 15, 'Int': 10, 'Wis': 9, 'Str': 12, 'Con':18}, 'Name':{'First':'Wes', 'Last':'Goldfinger'}, 'Gender': 'm', 'Age': '53', 'Hair-Colour': 'Red', 'Weapon': 'Bastard Sword', 'Class': 'Cleric', 'Eye-Colour': 'Blue'}

#Mages
Meera_Hazelthorn = {'Race': 'Half Elf', 'Stats': {'Dex': 9, 'Cha': 10, 'Int': 15, 'Wis': 10, 'Str': 15, 'Con':7}, 'Name':{'First':'Meera', 'Last':'Hazelthorn'}, 'Gender': 'f', 'Age': '39', 'Hair-Colour': 'Brown', 'Weapon': 'Bastard Sword', 'Class': 'Mage', 'Eye-Colour': 'Red'}
Neela_Grum = {'Race': 'Half Orc', 'Stats': {'Dex': 9, 'Cha': 11, 'Int': 19, 'Wis': 18, 'Str': 19, 'Con':10}, 'Name':{'First':'Neela', 'Last':'Grum'}, 'Gender': 'f', 'Age': '36', 'Hair-Colour': 'Grey', 'Weapon': 'Katana', 'Class': 'Mage', 'Eye-Colour': 'Hazel'}
Julia_Ablestone = {'Race': 'Gnome', 'Stats': {'Dex': 9, 'Cha': 17, 'Int': 12, 'Wis': 13, 'Str': 16, 'Con':11}, 'Name':{'First':'Julia', 'Last':'Ablestone'}, 'Gender': 'f', 'Age': '35', 'Hair-Colour': 'Grey', 'Weapon': 'Rapier', 'Class': 'Mage', 'Eye-Colour': 'Hazel'}
Zaak_Viperspit = {'Race': 'Dragonbourne', 'Stats': {'Dex': 18, 'Cha': 11, 'Int': 14, 'Wis': 14, 'Str': 14, 'Con':12}, 'Name':{'First':'Zaak', 'Last':'Viperspit'}, 'Gender': 'm', 'Age': '36', 'Hair-Colour': 'Blue', 'Weapon': 'Katana', 'Class': 'Mage', 'Eye-Colour': 'Green'}

#Monks
Ophelia_Rageeye = {'Race': 'Half Orc', 'Stats': {'Dex': 15, 'Cha': 12, 'Int': 13, 'Wis': 16, 'Str': 18, 'Con':8}, 'Name':{'First':'Ophelia', 'Last':'Rageeye'}, 'Gender': 'f', 'Age': '18', 'Hair-Colour': 'Brown', 'Weapon': 'Mace', 'Class': 'Monk', 'Eye-Colour': 'Hazel'}
Alistair_Silverwind = {'Race': 'Human', 'Stats': {'Dex': 14, 'Cha': 12, 'Int': 18, 'Wis': 18, 'Str': 17, 'Con':7}, 'Name':{'First':'Alistair', 'Last':'Silverwind'}, 'Gender': 'm', 'Age': '37', 'Hair-Colour': 'Bald', 'Weapon': 'Bow', 'Class': 'Monk', 'Eye-Colour': 'Hazel'}
Akai_Darkharrow = {'Race': 'Elf', 'Stats': {'Dex': 20, 'Cha': 11, 'Int': 13, 'Wis': 14, 'Str': 19, 'Con':14}, 'Name':{'First':'Akai', 'Last':'Darkharrow'}, 'Gender': 'm', 'Age': '82', 'Hair-Colour': 'Silver', 'Weapon': 'Dual Sai', 'Class': 'Monk', 'Eye-Colour': 'Purple'}
Justinia_Klien = {'Race': 'Halfling', 'Stats': {'Dex': 16, 'Cha': 16, 'Int': 9, 'Wis': 7, 'Str': 10, 'Con':8}, 'Name':{'First':'Justinia', 'Last':'Klien'}, 'Gender': 'f', 'Age': '29', 'Hair-Colour': 'Brown', 'Weapon': 'Rapier', 'Class': 'Monk', 'Eye-Colour': 'Green'}

#Paladins
Cyrion_Nyxmore = {'Race': 'Half Elf', 'Stats': {'Dex': 11, 'Int': 13, 'Wis': 13, 'Str': 10, 'Cha': 20, 'Con':12}, 'Name':{'First':'Cyrion', 'Last':'Nyxmore'}, 'Gender': 'm', 'Age': '49', 'Hair-Colour': 'Bald', 'Weapon': 'Single Sword', 'Class': 'Paladin', 'Eye-Colour': 'Green'}
Spyder_Brunsworth = {'Race': 'Halfling', 'Stats': {'Dex': 13, 'Int': 19, 'Wis': 7, 'Str': 14, 'Cha': 20, 'Con':10}, 'Name':{'First':'Spyder', 'Last':'Brunsworth'}, 'Gender': 'm', 'Age': '22', 'Hair-Colour': 'Brown', 'Weapon': 'Rapier', 'Class': 'Paladin', 'Eye-Colour': 'Green'}
Adai_Fallondow = {'Race': 'Elf', 'Stats': {'Dex': 18, 'Cha': 18, 'Int': 8, 'Wis': 8, 'Str': 11, 'Con':18}, 'Name':{'First':'Adai', 'Last':'Fallondow'}, 'Gender': 'f', 'Age': '45', 'Hair-Colour': 'Brown', 'Weapon': 'Throwing Daggers', 'Class': 'Paladin', 'Eye-Colour': 'Purple'}
Jimaru_Raeyvenh = {'Race': 'Elf', 'Stats': {'Dex': 12, 'Cha': 17, 'Int': 12, 'Wis': 19, 'Str': 8, 'Con':9}, 'Name':{'First':'Jimaru', 'Last':'Raeyvenh'}, 'Gender': 'm', 'Age': '90', 'Hair-Colour': 'Brown', 'Weapon': 'Bo Staff', 'Class': 'Paladin', 'Eye-Colour': 'Blue'}

#Rangers
Alistair_Undire = {'Race': 'Elf', 'Stats': {'Dex': 21, 'Cha': 11, 'Int': 13, 'Wis': 12, 'Str': 16, 'Con':17}, 'Name':{'First':'Alistair', 'Last':'Undire'}, 'Gender': 'm', 'Age': '75', 'Hair-Colour': 'White', 'Weapon': 'Nun Chaku', 'Class': 'Ranger', 'Eye-Colour': 'Purple'}
Smith_Stonevien = {'Race': 'Dwarf', 'Stats': {'Dex': 20, 'Cha': 15, 'Int': 9, 'Wis': 15, 'Str': 10, 'Con':11}, 'Name':{'First':'Smith', 'Last':'Stonevein'}, 'Gender': 'm', 'Age': '34', 'Hair-Colour': 'Blond', 'Weapon': 'Rapier', 'Class': 'Ranger', 'Eye-Colour': 'Green'}
Azoth_Faethre = {'Race': 'Half Elf', 'Stats': {'Dex': 12, 'Cha': 12, 'Int': 12, 'Wis': 7, 'Str': 11, 'Con':11}, 'Name':{'First':'Azoth', 'Last':'Faethre'}, 'Gender': 'm', 'Age': '52', 'Hair-Colour': 'White', 'Weapon': 'Nun Chaku', 'Class': 'Ranger', 'Eye-Colour': 'Blue'}
Lupe_Thistleberg = {'Race': 'Halfling', 'Stats': {'Dex': 12, 'Cha': 16, 'Int': 9, 'Wis': 16, 'Str': 15, 'Con':12}, 'Name':{'First':'Lupe', 'Last':'Thistleberg'}, 'Gender': 'f', 'Age': '21', 'Hair-Colour': 'Red', 'Weapon': 'Bo Staff', 'Class': 'Ranger', 'Eye-Colour': 'Black'}

#Rogues
Sirus_Honneath = {'Race': 'Halfling', 'Stats': {'Dex': 22, 'Cha': 18, 'Int': 11, 'Wis': 10, 'Str': 8, 'Con':14}, 'Name':{'First':'Sirus', 'Last':'Honneath'}, 'Gender': 'm', 'Age': '21', 'Hair-Colour': 'Black', 'Weapon': 'Battle Axe', 'Class': 'Rogue', 'Eye-Colour': 'Green'}
Sirus_Darkstrider = {'Race': 'Half Elf', 'Stats': {'Dex': 13, 'Cha': 16, 'Int': 9, 'Wis': 10, 'Str': 9, 'Con':18}, 'Name':{'First':'Sirus', 'Last':'Darkstrider'}, 'Gender': 'm', 'Age': '55', 'Hair-Colour': 'Black', 'Weapon': 'Great Sword', 'Class': 'Rogue', 'Eye-Colour': 'Silver'}
Hikari_Silviana = {'Race': 'Half Elf', 'Stats': {'Dex': 10, 'Cha': 12, 'Int': 9, 'Wis': 17, 'Str': 8, 'Con':12}, 'Name':{'First':'Hikari', 'Last':'Silviana'}, 'Gender': 'f', 'Age': '55', 'Hair-Colour': 'Brown', 'Weapon': 'Bo Staff', 'Class': 'Rogue', 'Eye-Colour': 'Purple'}
Akai_Onikiri = {'Race': 'Half Elf', 'Stats': {'Dex': 12, 'Cha': 9, 'Int': 10, 'Wis': 12, 'Str': 7, 'Con':9}, 'Name':{'First':'Akai', 'Last':'Onikiri'}, 'Gender': 'm', 'Age': '24', 'Hair-Colour': 'Silver', 'Weapon': 'Halbred', 'Class': 'Rogue', 'Eye-Colour': 'Red'}

#Warriors
Solace_Nactri = {'Race': 'Halfling', 'Stats': {'Dex': 19, 'Int': 16, 'Wis': 9, 'Str': 16, 'Cha': 16, 'Con':13}, 'Name':{'First':'Solace', 'Last':'Nactri'}, 'Gender': 'f', 'Age': '31', 'Hair-Colour': 'Brown', 'Weapon': 'Great Sword', 'Class': 'Warrior', 'Eye-Colour': 'Green'}
Kimi_Hammerhand = {'Race': 'Dwarf', 'Stats': {'Dex': 9, 'Cha': 19, 'Int': 8, 'Wis': 8, 'Str': 18, 'Con':15}, 'Name':{'First':'Kimi', 'Last':'Hammerhand'}, 'Gender': 'f', 'Age': '39', 'Hair-Colour': 'Brown', 'Weapon': 'Bo Staff', 'Class': 'Warrior', 'Eye-Colour': 'Grey'}
Ione_Vallen = {'Race': 'Half Elf', 'Stats': {'Dex': 16, 'Int': 11, 'Wis': 15, 'Str': 20, 'Cha': 13, 'Con':19}, 'Name':{'First':'Ione', 'Last':'Vallen'}, 'Gender': 'f', 'Age': '32', 'Hair-Colour': 'Blonde', 'Weapon': 'Scyth', 'Class': 'Warrior', 'Eye-Colour': 'Red'}
Xion_Durgas = {'Race': 'Halfling', 'Stats': {'Dex': 10, 'Cha': 13, 'Int': 7, 'Wis': 15, 'Str': 20, 'Con':10}, 'Name':{'First':'Xion', 'Last':'Durgas'}, 'Gender': 'm', 'Age': '32', 'Hair-Colour': 'Black', 'Weapon': 'Battle Axe', 'Class': 'Warrior', 'Eye-Colour': 'Green'}

#Wizards
Jimaru_Northcutt = {'Race': 'Human', 'Stats': {'Dex': 10, 'Int': 8, 'Wis': 13, 'Str': 15, 'Cha': 14, 'Con':15}, 'Name':{'First':'Jimaru', 'Last':'Northcutt'}, 'Gender': 'm', 'Age': '38', 'Hair-Colour': 'Blond', 'Weapon': 'Single Sickle', 'Class': 'Wizard', 'Eye-Colour': 'Black'}
Ceil_Faeren = {'Race': 'Human', 'Stats': {'Dex': 19, 'Cha': 14, 'Int': 12, 'Wis': 16, 'Str': 19, 'Con':16}, 'Name':{'First':'Ciel', 'Last':'Faeren'}, 'Gender': 'm', 'Age': '39', 'Hair-Colour': 'Bald', 'Weapon': 'Pole Axe', 'Class': 'Wizard', 'Eye-Colour': 'Black'}
Diniwedd_Mithrilshine = {'Race': 'Gnome', 'Stats': {'Dex': 8, 'Cha': 15, 'Int': 12, 'Wis': 17, 'Str': 10, 'Con':18}, 'Name':{'First':'Diniwedd', 'Last':'Mithrilshine'}, 'Gender': 'f', 'Age': '36', 'Hair-Colour': 'Brown', 'Weapon': 'Single Sai', 'Class': 'Wizard', 'Eye-Colour': 'Blue'}
Vivian_Silvermane = {'Race': 'Dwarf', 'Stats': {'Dex': 13, 'Cha': 11, 'Int': 15, 'Wis': 11, 'Str': 14, 'Con':13}, 'Name':{'First':'Vivian', 'Last':'Silvermane'}, 'Gender': 'f', 'Age': '54', 'Hair-Colour': 'Grey', 'Weapon': 'Great Sword', 'Class': 'Wizard', 'Eye-Colour': 'Hazel'}


Barbarians = [Ophren_Cleave, Sera_Warsong, Ophren_Copperback, Zaak_Mithrilfist]
Bards = [Vivian_Silvest, Ione_Gemdance, Ophelia_Silvervien, Tye_Lingon]
Clerics = [Ana_Harroweth, Azoth_Glimmertouch, Wes_Vernia, Wes_Goldfinger]
Mages = [Meera_Hazelthorn, Neela_Grum, Julia_Ablestone, Zaak_Viperspit]
Monks = [Ophelia_Rageeye, Alistair_Silverwind, Akai_Darkharrow, Justinia_Klien]
Paladins = [Cyrion_Nyxmore, Spyder_Brunsworth, Adai_Fallondow, Jimaru_Raeyvenh]
Rangers = [Alistair_Undire, Smith_Stonevien, Azoth_Faethre, Lupe_Thistleberg]
Rogues = [Sirus_Honneath, Sirus_Darkstrider, Hikari_Silviana, Akai_Onikiri]
Warriors = [Solace_Nactri, Kimi_Hammerhand, Ione_Vallen, Xion_Durgas]
Wizards = [Jimaru_Northcutt, Ceil_Faeren, Diniwedd_Mithrilshine, Vivian_Silvermane]


PlayerClasses = [Barbarians, Bards, Clerics, Mages, Monks, Paladins, Rangers, Rogues, Warriors, Wizards]

Class = random.randint(0, len(PlayerClasses)-1)
Person = random.randint(0, len(PlayerClasses[Class])-1)

NPC = PlayerClasses[Class][Person]
NPC['Health'] = (NPC['Stats']['Str'] * 2) + (NPC['Stats']['Con'] / 4)
NPC['Dodge'] = int(NPC['Stats']['Dex'] * 1.5)
#print NPC




