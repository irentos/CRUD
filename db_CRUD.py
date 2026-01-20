import mysql.connector
DB_CONFIG = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password':'root',
    'database':'pets'
}
headers = ['id','name','species','birth_year']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_pets():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_pets')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    #print(rows) # viskas kas zemiau funkcijoje yra tam, kad rezulata paverstu listu su dictionariais
    pets_list = []
    for row in rows:
        single_pet = {}
        for col_num in range(len(headers)):
            single_pet[headers[col_num]] = str(row[col_num])
        pets_list.append(single_pet)
    return pets_list

def print_info():
    print('---------------------------------------------------------')
    print('1. Show all pets.')
    print('2. Add new pet.')
    print('3. Manage my pets.')
    print('4. Delete pet.')
    print('5. Close a program.')
    print('-------------------------Select:-------------------------')

def print_pets():
    pets = load_pets()
    for pet in pets:
        print(f'{pet['id']}. Name: {pet['name']}. Pet species: {pet['species']}. Birth year: {pet['birth_year']}.')

def pet_adding():
    print('Adding new pet.')
    print('Type name:')
    name = input()
    print("Type pet's species:")
    species = input()
    print("Type birth year:")
    birth_year = int(input())  # MUST BE INT FOR NUM = NUM. if without int: text - text
    conn= get_conn()
    cur = conn.cursor()
    cur.execute(f'INSERT INTO my_pets(name, species, birth_year) VALUES(%s,%s,%s)',
                (name,species,birth_year))
    conn.commit()
    cur.close()
    conn.close()

def pets_managing():
    print('My pets managing')
    print('Enter a pet ID to manage the selected pet.')
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_pets where id = %s', (edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Name: {row[1]}. Pet species: {row[2]}. Age: {row[3]}.')
        print('Type name:')
        name = input()
        print("Type pet's species:")
        species = input()
        print("Type birth year:")
        birth_year = int(input())
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE `my_pets` SET `name` = %s, `species` = %s,`birth_year`= %s WHERE `id`=%s;",
                    (name,species,birth_year,edit_id))
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("No ID found")

def pets_remove():
    print('Delete my pet.')
    print('Enter a pet ID to manage the selected pet.')
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_pets where id = %s',(del_id,))
    row = cur.fetchone()
    if row:
        print(f'{row[0]}. Name: {row[1]}. Pet species: {row[2]}. Age: {row[3]}.')
        cur.execute("DELETE FROM `my_pets` WHERE id = %s;",(del_id,))
        conn.commit()
    else:
        print("No ID found")
    cur.close()
    conn.close()