import datetime

pets = [
        {
            'id': 1,
            'name': 'Aurora',
            'species': 'Dog',
            'birth_year': 2020
        },
        {
            'id': 2,
            'name': 'Marshall',
            'species': 'Dog',
            'birth_year': 2021
        },
        {
            'id': 4,
            'name': 'Nibbles',
            'species': 'cat',
            'birth_year': 2076
        },
        {
            'id': 5,
            'name': 'Roach',
            'species': 'horse',
            'birth_year': 1272
        }
    ]
id_counter = 5
now_year = datetime.date.today().year # making this year
while True:
    print('---------------------------------------------------------')
    print('1. Show all pets.')
    print('2. Add new pet.')
    print('3. Manage my pets.')
    print('4. Delete pet.')
    print('5. Close a program.')
    print('-------------------------Select:-------------------------')
    answer = input()
    match answer:
        case '1':
            for pet in pets:
                age = now_year - pet['birth_year']
                print(f'{pet['id']}. '
                      f'Pet species: {pet['species']}. '
                      f'Name: {pet['name']}. '
                      f'Age: {age}.') # how to make age?
        case '2':
            print('Add pet:')
            print('Type name:')
            name = input()
            print("Type pet's species:")
            species = input()
            print("Type birth year:")
            birth_year = int(input()) # MUST BE INT FOR NUM = NUM. if without int: text - text
            id_counter += 1
            pet = {
                'id': id_counter,
                'name': name,
                'species': species,
                'birth_year': birth_year
            }
            pets.append(pet)
        case '3':
            print('My pets managing')
            print('Enter a pet ID to manage the selected pet.')
            edit_id = input()
            for pet in pets:
                age = now_year - pet['birth_year']
                if edit_id == str(pet['id']):
                    print(f'{pet['id']}. '
                          f'Pet species: {pet['species']}. '
                          f'Name: {pet['name']}. '
                          f'Age: {age}.')
                    print('Type name:')
                    pet['name'] = input()
                    print("Type pet's species:")
                    pet['species'] = input()
                    print("Type birth year:")
                    pet['birth_year'] = input()
        case '4':
            print('Delete my pet.')
            print('Enter a pet ID to manage the selected pet.')
            del_id = input()
            for pet in pets:
                if del_id == str(pet['id']):
                    print(f'{pet['id']}. '
                          f'Delete: Pet {pet['species']}'
                          f'{pet['name']}'
                          f'{pet['birth_year']}')
                    pets.remove(pet)
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