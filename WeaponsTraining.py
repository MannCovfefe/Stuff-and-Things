#!/usr/bin/env python

try:
    import re,os,random
except:
    sys.exit("Import error!")

def WeaponSelect(Thinga, PlayerProficiency, PlayerStats):
    Mabob = Thinga
    Proficiency = PlayerProficiency
    Player1 = PlayerStats
    #print Player1
    ProfLevel = int(Player1[Proficiency]/ 4)+1
    #print ProfLevel
    #print Proficiency
    #print Player1
    #print Mabob
    Weapon={"Name":'', "Attack":'', "Type":'', "Acc":'', "Player":{}}
    #weaponSet = random.randint(1,19)
    #weaponSet=2
    #print Mabob

    if re.match('Single Sword', Mabob):
        weaponSet = 1
        SwordType = 1
        MoreSword = 1
    if re.match('Dual Swords', Mabob):
        weaponSet = 1
        SwordType = 1
        MoreSword = 2
    if re.match('1 Sword, 1 Dagger', Mabob):
        weaponSet = 1
        SwordType = 1
        MoreSword = 3
    if re.match('Sword and Shield', Mabob):
        weaponSet = 1
        SwordType = 1
        MoreSword = 4
    if re.match('Single Short Sword', Mabob):
        weaponSet = 1
        SwordType = 2
        MoreSword = 1
    if re.match('Dual Shorts Swords', Mabob):
        weaponSet = 1
        SwordType = 2
        MoreSword = 2
    if re.match('1 Short Sword, 1 Dagger', Mabob):
        weaponSet = 1
        SwordType = 2
        MoreSword = 3
    if re.match('Short Sword and Shield', Mabob):
        weaponSet = 1
        SwordType = 2
        MoreSword = 4
    if re.match('Long Sword', Mabob):
        weaponSet = 2
    if re.match('Pole Axe', Mabob):
        weaponSet = 3
    if re.match('Katana', Mabob):
        weaponSet = 4
    if re.match('Bo Staff', Mabob):
        weaponSet = 5
    if re.match('Nun Chaku', Mabob):
        weaponSet = 6
    if re.match('Single Sickle', Mabob):
        weaponSet = 7
        SickleType = 1
    if re.match('Dual Sickles', Mabob):
        weaponSet = 7
        SickleType = 2
    if re.match('Chain Sickle', Mabob):
        weaponSet = 7
        SickleType = 3
    if re.match('Scythe', Mabob):
        weaponSet = 8
    if re.search('Aerialist', Mabob):
        weaponSet = 9
        MartialStyle = 1
    if re.search('Steel', Mabob):
        weaponSet = 9
        MartialStyle = 2
    if re.search('Universal', Mabob):
        weaponSet = 9
        MartialStyle = 3
    if re.match('Brass Knuckles', Mabob):
        weaponSet = 9
        MartialStyle = 4
    if re.match('Bare Hands', Mabob):
        weaponSet = 9
        MartialStyle = 5
    if re.match('Single Dagger', Mabob):
        weaponSet = 10
        DaggerStyle = 1
    if re.match('Dual Daggers', Mabob):
        weaponSet = 10
        DaggerStyle = 2
    if re.match('Throwing Dagger', Mabob):
        weaponSet = 10
        DaggerStyle = 3
    if re.match('Hatchet', Mabob):
        weaponSet = 10
        DaggerStyle = 4
    if re.match('Rapier', Mabob):
        weaponSet = 11
    if re.match('Single Sai', Mabob):
        weaponSet = 12
        SaiStyle = 1
    if re.match('Dual Sai', Mabob):
        weaponSet = 12
        SaiStyle=2
    if re.match('Battle Axe', Mabob):
        weaponSet = 13
    if re.match('War Hammer', Mabob):
        weaponSet = 14
    if re.match('Great Sword', Mabob):
        weaponSet = 15
    if re.match('Bastard Sword', Mabob):
        weaponSet = 16
    if re.match('Halberd', Mabob):
        weaponSet = 17
    if re.match('Bow', Mabob):
        weaponSet = 18
        BowStyle = 1
    if re.match('Crossbow', Mabob):
        weaponSet = 18
        BowStyle = 2
    if re.match('Mace', Mabob):
        weaponSet = 19
        MaceStyle = 1
    if re.match('Flail', Mabob):
        weaponSet = 19
        MaceStyle = 2
#    else:
#        print 'Misspelling?'


    if weaponSet == 1:
        #SwordType = random.randint(1,2)
        if SwordType == 1:
            #MoreSword = random.randint(1,4)
            if MoreSword == 1:
                Weapon['Name'] = 'Single Sword'
                Weapon['Attack'] = 5
                Weapon['Type'] = 'Versatile'
                Weapon['Acc'] = 10
            if MoreSword == 2:
                Weapon['Name'] = 'Dual Swords'
                Weapon['Attack'] = 7
                Weapon['Type'] = 'Dex'
                Weapon['Acc'] = 7
            if MoreSword == 3:
                Weapon['Name'] = '1 Sword, 1 Dagger'
                Weapon['Attack'] = 6
                Weapon['Type'] = 'Dex'
                Weapon['Acc'] = 8
            if MoreSword == 4:
                Weapon['Name'] = 'Sword and Shield'
                Weapon['Attack'] = 5
                Weapon['Type'] = 'Versatile'
                Weapon['Acc'] = 9
        if SwordType == 2:
            #MoreSword = random.randint(1,4)
            if MoreSword == 1:
                Weapon['Name'] = 'Single Short Sword'
                Weapon['Attack'] = 4
                Weapon['Type'] = 'Versatile'
                Weapon['Acc'] = 10
            if MoreSword == 2:
                Weapon['Name'] = 'Dual Short Swords'
                Weapon['Attack'] = 6
                Weapon['Type'] = 'Dex'
                Weapon['Acc'] = 8
            if MoreSword == 3:
                Weapon['Name'] = '1 Short Sword, 1 Dagger'
                Weapon['Attack'] = 5
                Weapon['Type'] = 'Dex'
                Weapon['Acc'] = 9
            if MoreSword == 4:
                Weapon['Name'] = 'Short Sword and Shield'
                Weapon['Attack'] = 4
                Weapon['Type'] = 'Versatile'
                Weapon['Acc'] = 9
    if weaponSet == 2:
        Weapon['Name'] = 'Long Sword'
        Weapon['Attack'] = 6
        Weapon['Type'] = 'Versatile'
        Weapon['Acc'] = 10
    if weaponSet == 3:
        Weapon['Name'] = 'Pole Axe'
        Weapon['Attack'] = 7
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 8
    if weaponSet == 4:
        Weapon['Name'] = 'Katana'
        Weapon['Attack'] = 7
        Weapon['Type'] = 'Dex'
        Weapon['Acc'] = 12
    if weaponSet == 5:
        Weapon['Name'] = 'Bo Staff'
        Weapon['Attack'] = 6
        Weapon['Type'] = 'Versatile'
        Weapon['Acc'] = 10
    if weaponSet == 6:
        Weapon['Name'] = 'Nun Chaku'
        Weapon['Attack'] = 4
        Weapon['Type'] = 'Dex'
        Weapon['Acc'] = 7
    if weaponSet == 7:
        #SickleType = random.randint(1,3)
        if SickleType == 1:
            Weapon['Name'] = 'Single Sickle'
            Weapon['Attack'] = 3
            Weapon['Dex'] = 'Versatile'
            Weapon['Acc'] = 10
        if SickleType == 2:
            Weapon['Name'] = 'Dual Sickles'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 7
        if SickleType == 3:
            Weapon['Name'] = 'Chain Sickle'
            Weapon['Attack'] = 3
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 8
    if weaponSet == 8:
        Weapon['Name'] = 'Scythe'
        Weapon['Attack'] = 6
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 9
    if weaponSet == 9:
        #MartialStyle = random.randint(1,5)
        if MartialStyle == 1:
            Weapon['Name'] = 'Aerialist Martial Arts'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 10
        if MartialStyle == 2:
            Weapon['Name'] = 'Steel Soul Martial Arts'
            Weapon['Attack'] = 5
            Weapon['Type'] = 'Str'
            Weapon['Acc'] = 11
        if MartialStyle == 3:
            Weapon['Name'] = 'Universal Way Martial Arts'
            Weapon['Attack'] = 5
            Weapon['Type'] = 'Versatile'
            Weapon['Acc'] = 12
        if MartialStyle == 4:
            Weapon['Name'] = 'Brass Knuckles'
            Weapon['Attack'] = 6
            Weapon['Type'] = 'Str'
            Weapon['Acc'] = 10
        if MartialStyle == 5:
            Weapon['Name'] = 'Bare Hands'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Str'
            Weapon['Acc'] = 7
    if weaponSet == 10:
        #DaggerStyle = random.randint(1,4)
        if DaggerStyle == 1:
            Weapon['Name'] = 'Single Dagger'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 11
        if DaggerStyle == 2:
            Weapon['Name'] = 'Dual Daggers'
            Weapon['Attack'] = 5
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 9
        if DaggerStyle == 3:
            Weapon['Name'] = 'Throwing Daggers'
            Weapon['Attack'] = 3
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 8
        if DaggerStyle == 4:
            Weapon['Name'] = 'Hatchet'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Versatile'
            Weapon['Acc'] = 9
    if weaponSet == 11:
        Weapon['Name'] = 'Rapier'
        Weapon['Attack'] = 6
        Weapon['Type'] = 'Dex'
        Weapon['Acc'] = 11
    if weaponSet == 12:
        #SaiStyle = random.randint(1,2)
        if SaiStyle == 1:
            Weapon['Name'] = 'Single Sai'
            Weapon['Attack'] = 4
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 10
        if SaiStyle == 2:
            Weapon['Name'] = 'Dual Sai'
            Weapon['Attack'] = 5
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 9
    if weaponSet == 13:
        Weapon['Name'] = 'Battle Axe'
        Weapon['Attack'] = 8
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 8
    if weaponSet == 14:
        Weapon['Name'] = 'War Hammer'
        Weapon['Attack'] = 7
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 8
    if weaponSet == 15:
        Weapon['Name'] = 'Great Sword'
        Weapon['Attack'] = 7
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 10
    if weaponSet == 16:
        Weapon['Name'] = 'Bastard Sword'
        Weapon['Attack'] = 8
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 9
    if weaponSet == 17:
        Weapon['Name'] = 'Halberd'
        Weapon['Attack'] = 8
        Weapon['Type'] = 'Str'
        Weapon['Acc'] = 9
    if weaponSet == 18:
        #BowStyle = random.randint(1,2)
        if BowStyle == 1:
            Weapon['Name'] = 'Bow'
            Weapon['Attack'] = 6
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 13
        if BowStyle == 2:
            Weapon['Name'] = 'Crossbow'
            Weapon['Attack'] = 5
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 12
    if weaponSet == 19:
        #MaceStyle = random.randint(1,2)
        if MaceStyle == 1:
            Weapon['Name'] = 'Mace'
            Weapon['Attack'] = 6
            Weapon['Type'] = 'Str'
            Weapon['Acc'] = 10
        if MaceStyle == 2:
            Weapon['Name'] = 'Flail'
            Weapon['Attack'] = 6
            Weapon['Type'] = 'Dex'
            Weapon['Acc'] = 8


    if re.match('Versatile', Weapon['Type']):
        Choosey = raw_input("For a {Wep} do you want to use strength or dexterity?[Dex|Str] ".format(Wep=Weapon['Name']).rstrip("/n"))
        try:
            if re.match('[d|D][e|E][x|X]$', Choosey):
                if Proficiency == 'Dex':
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                    Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
                else:
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*1.5)
                    Weapon['Player']['Damage']=int(Weapon['Attack']+Player1['Dex'])
            if re.match('[s|S][t|T][r|R]$', Choosey):
                if Proficiency == 'Str':
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                    Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
                else:
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*1.5)
                    Weapon['Player']['Damage']=int(Weapon['Attack']+Player1['Str'])
            if Choosey == '':
                if Proficiency == 'Str':
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                    Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
                if Proficiency == 'Dex':
                    Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                    Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
        except ValueError:
            if Proficiency == 'Dex':
                Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                Weapon['Player']['Damage']=int(Weapon['Attack']+int(ProfLevel))
            if Proficiency == 'Str':
                Weapon['Player']['ToHit']=int((Weapon['Acc']+int(ProfLevel))*2)
                Weapon['Player']['Damage']=int(Weapon['Attack']+int(ProfLevel))
              

    if re.match('Dex', Weapon['Type']):
        if Proficiency == 'Dex':
            Weapon['Player']['ToHit']=(Weapon['Acc']+int(ProfLevel))*2
            Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
        else:
            Weapon['Player']['ToHit']=int((Weapon['Acc']+Player1['Dex'])*1.5)
            Weapon['Player']['Damage']=Weapon['Attack']+Player1['Dex']

    if re.match('Str', Weapon['Type']):
        if Proficiency == 'Str':
            Weapon['Player']['ToHit']=(Weapon['Acc']+int(ProfLevel))*2
            Weapon['Player']['Damage']=Weapon['Attack']+int(ProfLevel)
        else:
            Weapon['Player']['ToHit']=int((Weapon['Acc']+Player1['Str'])*1.5)
            Weapon['Player']['Damage']=Weapon['Attack']+Player1['Str']

    #print Weapon
    return(Weapon)

def Main():
    '''Weapon={}
    Weapon=WeaponSelect()
    Attack={"ToHit":[], "Damage":[]}
    Player1={'Race':'Elf', 'Stats':{'Dex':21,'Cha':18,'Int':19,'Wis':13,'Str':13,'Con':13}, 'Name':{'First':'Sera', 'Last':'Warsong'}, 'Gender':'f', 'Age':'85', 'Hair-Colour':'Black', 'Weapon':'Rapier', 'Class':'Barbarian', 'Eye-Colour':'Grey'}
    Player1['Health'] = (Player1['Stats']['Str'] * 2) + (Player1['Stats']['Con'] / 4)
    Player1['Dodge'] = int(Player1['Stats']['Dex'] * 1.5)
    Player1['Level'] = 1
    Player1['Proficiency'] = 'Str'
    Player1['ProficiencyLevel'] = int(Player1['Stats']['Str']+(Player1['Level']*1.5))

    #print Weapon
    '''
    '''
    if re.match('Versatile', Weapon['Type']):
        Choosey = raw_input("For a {Wep} do you want to use strength or dexterity?[Dex|Str] ".format(Wep=Weapon['Name']).rstrip("/n"))
        if re.match('[d|D][e|E][x|X]$', Choosey):
            if Player1['Proficiency'] == 'Dex':
                Weapon['Attack']['ToHit']=(Weapon['Acc']+Player1['ProficiencyLevel'])*2
                Weapon['Attack']['Damage']=Weapon['Attack']+Player1['ProficiencyLevel']
            else:
                Weapon['Attack']['ToHit']=int((Weapon['Acc']+Player1['Stats']['Dex'])*1.5)
                Weapon['Attack']['Damage']=Weapon['Attack']+Player1['Stats']['Dex']
        if re.match('[s|S][t|T][r|R]$', Choosey):
            if Player1['Proficiency'] == 'Str':
                Weapon['Attack']['ToHit']=(Weapon['Acc']+Player1['ProficiencyLevel'])*2
                Weapon['Attack']['Damage']=Weapon['Attack']+Player1['ProficiencyLevel']
            else:
                Weapon['Attack']['ToHit']=int((Weapon['Acc']+Player1['Stats']['Str'])*1.5)
                Weapon['Attack']['Damage']=Weapon['Attack']+Player1['Stats']['Str']

    if re.match('Dex', Weapon['Type']):
        if Player1['Proficiency'] == 'Dex':
            Weapon['Attack']['ToHit']=(Weapon['Acc']+Player1['ProficiencyLevel'])*2
            Weapon['Attack']['Damage']=Weapon['Attack']+Player1['ProficiencyLevel']
        else:
            Weapon['Attack']['ToHit']=int((Weapon['Acc']+Player1['Stats']['Dex'])*1.5)
            Weapon['Attack']['Damage']=Weapon['Attack']+Player1['Stats']['Dex']

    if re.match('Str', Weapon['Type']):
        if Player1['Proficiency'] == 'Str':
            Weapon['Attack']['ToHit']=(Weapon['Acc']+Player1['ProficiencyLevel'])*2
            Weapon['Attack']['Damage']=Weapon['Attack']+Player1['ProficiencyLevel']
        else:
            Weapon['Attack']['ToHit']=int((Weapon['Acc']+Player1['Stats']['Str'])*1.5)
            Weapon['Attack']['Damage']=Weapon['Attack']+Player1['Stats']['Str']

    else:
        print 'Eh wot?'

    '''

    '''
    print Weapon['Name'], Weapon['Attack'], Weapon['Type']
    print 'To hit: {Hit},  Damage: {Dam}'.format(Hit=Attack['ToHit'], Dam=Attack['Damage'])
    Whammy = random.randint(1, 100)
    print Whammy
    if Whammy <= Attack['ToHit']:
        print 'Hit'
    else:
        print 'Miss'
    '''
Main()
