def greet(lang):
    if lang == 'en':
        return "Hello"
    elif lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    elif lang == 'kan':
        return "ನಮಸ್ಕಾರ"
    else:
        return "I dont speak your language!!!"


for i in range(4):
    if i == 0:
        language = 'en'
        print(greet(language), "Maddy")
    elif i == 1:
        language = 'es'
        print(greet(language), "Boda")
    elif i == 2:
        language = 'fr'
        print(greet(language), "Rahul")
    elif i == 3:
        language = 'kan'
        print(greet(language), "Chandu")
    else:
        print("That is all!!!")
