import csv

headers = ['id', 'name', 'species', 'birth_year']
def load_pets():
    with open('pets_data.csv',mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))
def save_pets(pets):
    with open("pets_data.csv",mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(pets)

def print_info():
    print('---------------------------------------------------------')
    print('1. Show all pets.')
    print('2. Add new pet.')
    print('3. Manage my pets.')
    print('4. Delete pet.')
    print('5. Close a program.')
    print('-------------------------Select:-------------------------')

def print_pets(pets):
    for pet in pets:
        print(f'{pet['id']}. Name: {pet['name']}. Pet species: {pet['species']}. Birth year: {pet['birth_year']}.')

def pet_adding(pets, id_counter):
    print('Adding new pet.')
    print('Type name:')
    name = input()
    print("Type pet's species:")
    species = input()
    print("Type birth year:")
    birth_year = int(input())  # MUST BE INT FOR NUM = NUM. if without int: text - text
    id_counter = int(pets[-1]['id']) + 1 if len(pets) > 0 else 1
    pet = {
        'id': id_counter,
        'name': name,
        'species': species,
        'birth_year': birth_year
    }
    pets.append(pet)
    save_pets(pets)
    return id_counter

def pets_managing(pets):
    print('My pets managing')
    print('Enter a pet ID to manage the selected pet.')
    edit_id = input()
    for pet in pets:
        if edit_id == str(pet['id']):
            print(f'{pet['id']}. Name: {pet['name']}. Pet species: {pet['species']}. Birth year: {pet['birth_year']}.')
            print('Type name:')
            pet['name'] = input()
            print("Type pet's species:")
            pet['species'] = input()
            print("Type birth year:")
            pet['birth_year'] = int(input())
    save_pets(pets)

def pets_remove(pets):
    print('Delete my pet.')
    print('Enter a pet ID to manage the selected pet.')
    del_id = input()
    for pet in pets:
        if del_id == str(pet['id']):
            print(f'{pet['id']}. Deleting pet: {pet['name']} {pet['species']} {pet['birth_year']}')
            pets.remove(pet)
    save_pets(pets)