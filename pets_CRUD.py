import datetime
def load_default_data():
  return[
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

def print_info():
    print('---------------------------------------------------------')
    print('1. Show all pets.')
    print('2. Add new pet.')
    print('3. Manage my pets.')
    print('4. Delete pet.')
    print('5. Close a program.')
    print('-------------------------Select:-------------------------')

def print_all_pets(pets, now_year):
    for pet in pets:
        now_year = datetime.date.today().year
        age = now_year - pet['birth_year']
        print(f'{pet['id']}. '
              f'Pet species: {pet['species']}. '
              f'Name: {pet['name']}. '
              f'Age: {age}.')  # how to make age?

def pet_adding(pets, id_counter):
    now_year = datetime.date.today().year
    print('Adding new pet.')
    print('Type name:')
    name = input()
    print("Type pet's species:")
    species = input()
    print("Type birth year:")
    birth_year = int(input())  # MUST BE INT FOR NUM = NUM. if without int: text - text
    id_counter += 1
    pet = {
        'id': id_counter,
        'name': name,
        'species': species,
        'birth_year': birth_year
    }
    pets.append(pet)
    return id_counter
def pets_managing(pets, now_year):
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
            pet['birth_year'] = int(input())

def pets_remove(pets):
    print('Delete my pet.')
    print('Enter a pet ID to manage the selected pet.')
    del_id = input()
    for pet in pets:
        if del_id == str(pet['id']):
            print(f'{pet['id']}. Deleting pet: {pet['species']} {pet['name']} {pet['birth_year']}')
            pets.remove(pet)