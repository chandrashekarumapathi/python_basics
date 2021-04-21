def greet(lang):
    if lang == 'en':
        print("Hello")
    elif lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    elif lang == 'kan':
        print("ನಮಸ್ಕಾರ")
    else:
        print("I dont speak your language!!!")


for i in range(4):
    if i == 0:
        language = 'en'
        greet(language)
    elif i == 1:
        language = 'es'
        greet(language)
    elif i == 2:
        language = 'fr'
        greet(language)
    elif i == 3:
        language = 'kan'
        greet(language)
    else:
        print("That is all!!!")
        break
