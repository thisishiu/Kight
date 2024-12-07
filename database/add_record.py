import sqlite3

# connect to database
database = sqlite3.connect('database/Knight_database.db')
cursor = database.cursor()

def add_TileMap_1():
    data = [
    (1, 1, 1, 'ground', 'grass', 1),
	(1, 2, 1, 'ground', 'grass', 21),
	
	(2, 1, 1, 'ground', 'grass', 3),
	(2, 2, 1, 'ground', 'grass', 13),
	(2, 3, 1, 'ground', 'grass', 11),
	(2, 4, 1, 'ground', 'grass', 11),
	(2, 5, 1, 'ground', 'grass', 11),
	(2, 6, 1, 'ground', 'grass', 11),
	(2, 7, 1, 'ground', 'grass', 21),
	
	(3, 1, 1, 'ground', 'grass', 4),
	(3, 2, 1, 'ground', 'grass', 13),
	(3, 3, 1, 'ground', 'grass', 13),
	(3, 4, 1, 'ground', 'grass', 13),
	(3, 5, 1, 'ground', 'grass', 13),
	(3, 6, 1, 'ground', 'grass', 13),
	(3, 7, 1, 'ground', 'grass', 23),
	
	(4, 2, 1, 'ground', 'grass', 3),
	(4, 3, 1, 'ground', 'grass', 13),
	(4, 4, 1, 'ground', 'grass', 13),
	(4, 5, 1, 'ground', 'grass', 13),
	(4, 6, 1, 'ground', 'grass', 14),
	(4, 7, 1, 'ground', 'grass', 24),
	
	(5, 2, 1, 'ground', 'grass', 3),
	(5, 3, 1, 'ground', 'grass', 13),
	(5, 4, 1, 'ground', 'grass', 14),
	(5, 5, 1, 'ground', 'grass', 24),

	(6, 1, 1, 'ground', 'grass', 1),
	(6, 2, 1, 'ground', 'grass', 13),
	(6, 3, 1, 'ground', 'grass', 23),
	
	(7, 1, 1, 'ground', 'grass', 3),
	(7, 2, 1, 'ground', 'grass', 13),
	(7, 3, 1, 'ground', 'grass', 23),
	
	(8, 1, 1, 'ground', 'grass', 4),
	(8, 2, 1, 'ground', 'grass', 14),
	(8, 3, 1, 'ground', 'grass', 24),
    ]
    
    cursor.executemany("""
    INSERT INTO TileMap_1
    VALUES (?, ?, ?, ?, ?, ?)
""", data)
    
# add_TileMap_1()

database.commit()
database.close()

