from file_CRUD import *

pets = load_pets()
id_counter = 5
while True:
    print_info()
    answer = input()
    match answer:
        case '1':
            print_pets(pets)
        case '2':
            id_counter = pet_adding(pets, id_counter)
        case '3':
           pets_managing(pets)
        case '4':
            pets_remove(pets)
        case '5':
            print('Close a program.')
            break
































# mass = [1, 5, 10, 30, 50, 80, 100]
#
# dictionary = {'diena':1, 'valandos':5, 'minutes':10}
# print(dictionary['diena'])
#
# studentas = {
#     'vardas':'Jonas',
#     'pavarde': 'Jakubaitis',
#     'amzius':35,
#     'mokomieji dalykai':["lietuviu", "anglu", "pitonas"]
# }
#
# print(studentas['mokomieji dalykai'][2])
# .keys() - keywords / .values() - what after keywords is
# print('iveskite kazka')
# ivestis = input()
# print(f"jus ivedete'{ivestis}'") # vedam i kodo dali, ka parasem nugula i ivestis

# match ivestis: - kaip if tik patogiau programoje nes svaresne
#     case "1":
    # case _: - #as def if non using values
# while True - крутит пока не находит искомое или не натыкается на break