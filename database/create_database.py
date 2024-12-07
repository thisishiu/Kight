import sqlite3

# connect to database
database = sqlite3.connect('database/Knight_database.db')

def info():
    return """
Database:
    TileMap_1(
        x INTEGER
        y INTEGER
        layer TEXT
        type TEXT           # (ground, wall front, wall behind)
        name TEXT           # maybe name of folder
        variant INTEGER     # which one
    )
    
    TileMap_2()
    
    Player
"""

def TileMap_1():
    return """
CREATE TABLE TileMap_1 (
    x INTEGER,
    y INTEGER,
    layer TEXT,
    type TEXT,
    name TEXT,
    variant INTEGER,
    primary key (x,y,layer,type, name, variant);
);
    """

def TileMap_2():
    return """
CREATE TABLE TileMap_2 (
    x INTEGER,
    y INTEGER,
    layer TEXT,
    type TEXT,
    name TEXT,
    variant INTEGER,
    primary key (x,y,layer,type, name, variant)
);
"""

# database.execute(TileMap_2())

database.commit()
database.close()