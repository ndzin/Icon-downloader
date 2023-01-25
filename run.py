import os
from pathlib import Path
import requests

mainUrl = 'https://api.ambr.top/assets/UI/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

char_name = input('Type the Character Name:\n')

char_check = char_name.capitalize()

if char_check == 'Yanfei':
    char = 'Feiyan'
elif char_check == 'Jean':
    char = 'Qin'
else:
    char = char_check

valid = mainUrl+'UI_Gacha_AvatarImg_'+char+'.png'

response = requests.get(valid)
try:
    if response.status_code == 200:  
        createFolder('./data/'+char+'/Abilities')
        createFolder('./data/'+char+'/Passives')
        createFolder('./data/'+char+'/Constellation')
        e_a = mainUrl+'Skill_E_'+char+'_01.png'
        e_x = mainUrl+'Skill_S_'+char+'_01.png'

        p1 = mainUrl+'UI_Talent_S_'+char+'_05.png'
        p2 = mainUrl+'UI_Talent_S_'+char+'_06.png'
        p3 = mainUrl+'UI_Talent_S_'+char+'_07.png'

        c1 = mainUrl+'UI_Talent_S_'+char+'_01.png'
        c2 = mainUrl+'UI_Talent_S_'+char+'_02.png'
        c3 = mainUrl+'Skill_E_'+char+'_01.png'
        c4 = mainUrl+'UI_Talent_S_'+char+'_03.png'
        c5 = mainUrl+'Skill_S_'+char+'_01.png'
        c6 = mainUrl+'UI_Talent_S_'+char+'_04.png'


        if char == 'Qin':
            e_a = mainUrl+'Skill_S_'+char+'_02.png'
            e_x = mainUrl+'UI_Talent_U_'+char+'_02.png'
            c3 = mainUrl+'Skill_S_'+char+'_02.png'
            c5 = mainUrl+'UI_Talent_U_'+char+'_02.png'


        ai = mainUrl+'UI_AvatarIcon_'+char+'.png'
        namecard = mainUrl+'/namecard/UI_NameCardPic_'+char+'_P.png'
        splash = mainUrl+'UI_Gacha_AvatarImg_'+char+'.png'

        isntbeta = 'https://enka.network/ui/UI_AvatarIcon_'+char+'_Card.png'

        response = requests.get(isntbeta)
        if response.status_code == 200:
            card = 'https://enka.network/ui/UI_AvatarIcon_'+char+'_Card.png'
            side = 'https://enka.network/ui/UI_AvatarIcon_Side_'+char+'.png'
        else:
            card = 'https://raw.githubusercontent.com/ndzin/ndzin.github.io/main/gi-library/UI/UI_AvatarIcon_'+char+'_Card.png'
            side = 'https://raw.githubusercontent.com/ndzin/ndzin.github.io/main/gi-library/UI/UI_AvatarIcon_Side_'+char+'.png'
            

        req = requests.get(side)
        filename = req.url[side.rfind('/')+1:]
        print('\nDownloaded '+filename)

        with open('./data/'+char+'/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(card)
        filename = req.url[card.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(ai)
        filename = req.url[ai.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(namecard)
        filename = req.url[namecard.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(splash)
        filename = req.url[splash.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(e_a)
        filename = req.url[e_a.rfind('/')+1:]
        print('\nDownloaded '+filename)

        with open('./data/'+char+'/Abilities/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(e_x)
        filename = req.url[e_x.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Abilities/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


        req = requests.get(p1)
        filename = req.url[p1.rfind('/')+1:]
        print('\nDownloaded '+filename)

        with open('./data/'+char+'/Passives/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(p2)
        filename = req.url[p2.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Passives/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(p3)
        filename = req.url[p3.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Passives/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c1)
        filename = req.url[c1.rfind('/')+1:]
        print('\nDownloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c2)
        filename = req.url[c2.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c3)
        filename = req.url[c3.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c4)
        filename = req.url[c4.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c5)
        filename = req.url[c5.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        req = requests.get(c6)
        filename = req.url[c6.rfind('/')+1:]
        print('Downloaded '+filename)

        with open('./data/'+char+'/Constellation/'+filename, 'wb') as f:
            
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
except:
    exit