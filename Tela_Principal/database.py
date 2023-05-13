import sqlite3
from wsgiref.handlers import format_date_time

class RoomDB:
    CREAT_CHECK_TABLE_QUERY=("CREATE TABLE IF NOT EXISTS check(checkin date,checkout date,cpf int primary key)")
    CREAT_ROOM_TABLE_QUERY = ('CREATE TABLE IF NOT EXISTS room(name text,number int, CPF text primary key,occupied text)')  
    INSERT_CHECK_TABLE_QUERY=("INSERT INTO CHECK(checkin,checkout,cpf) VALUES(?,?,?)")
    INSERT_ROOM_QUERY = 'INSERT INTO room(name,number,CPF,room) VALUES (?,?,?,?)'
    UPDATE_DATE_ROOM_QUERY = 'UPDATE check SET checkin = ? WHERE cpf = ?'
    UPDATE_OCCUPIED_ROOM_QUERY = 'UPDATE room SET occupied = ? WHERE number = ?'
    SELECT_ROOM_QUERY = 'SELECT * FROM room WHERE CPF = ?'
    SELECT_BY_DATE_AND_NUMBER_QUERY = 'SELECT occupied FROM room WHERE number = ?'
    DELETE_ROOM_QUERY = 'DELETE FROM room WHERE CPF = ?'
    DELETE_CHECK_QUERY = 'DELETE FROM check WHERE CPF = ?'

    
    def __init__(self):
        self.conect = sqlite3.connect("banco.db")
        self.c = self.conect.cursor()
        self.c.execute(self.CREAT_ROOM_TABLE_QUERY)
        self.conect.commit()

    def insert_room(self,name,number,CPF,occupied):
        self.c.execute(self.INSERT_ROOM_QUERY,(name,number,CPF,occupied))
        self.conect.commit()

    def insert_check(self,checking,checkout,cpf):
        self.c.execute(self.INSERT_ROOM_QUERY,(checking,checkout,cpf))
        self.conect.commit()    

    def update_date_room(self,chekin,cpf):
        self.c.execute(self.UPDATE_DATE_ROOM_QUERY,(chekin,cpf))
        self.conect.commit()
        
    def update_occupied_room(self, number):
        current_occupied = self.c.execute("SELECT occupied FROM room WHERE number = ?", (number,)).fetchone()[0]
        new_occupied = not current_occupied
        self.c.execute(self.UPDATE_OCCUPIED_ROOM_QUERY, (new_occupied, number))
        self.conect.commit()
        
    def select_room(self,CPF):
        self.c.execute(self.SELECT_ROOM_QUERY,(CPF,))
        return self.c.fetchall()
    
    def select_by_date_and_number(self, occupied, number):
        self.c.execute(self.SELECT_BY_DATE_AND_NUMBER_QUERY, (occupied, number))
        return self.c.fetchone()
    
    def delete_room(self,CPF):
        self.c.execute(self.DELETE_ROOM_QUERY,(CPF,))
        self.conect.commit()
    
    def delete_room(self,CPF):
        self.c.execute(self.DELETE_CHECK_QUERY,(CPF,))
        self.conect.commit()
        
    def __del__(self):
        self.conect.close()