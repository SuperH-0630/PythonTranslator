from translate import Translator
flat = 'v' #变量命名法
translator= Translator(from_lang="chinese",to_lang="english")
while True:
    try:
        i = input('Input please : ')
        if i == 'q':break
        if i in 'vtn' and len(i) == 1:
            flat = i
            continue
        translation = translator.translate(i)
        if flat == 'v':
            translation = translation.replace(' ','_')
            translation = translation.lower()
        elif flat == 't':
            translation = translation.title()
            translation = translation.replace(' ','')
        else:
            translation = translation.replace(' ','_')
            translation = translation.upper()
        print(f'\nEnglish : {translation}\n')
    except:
        print('\nSorry:\nplease type q to quit\n')
