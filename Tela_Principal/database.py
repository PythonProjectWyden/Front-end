import sqlite3
from wsgiref.handlers import format_date_time

class RoomDB:
<<<<<<< Updated upstream
    # CREAT_CHECKS_TABLE_QUERY=("CREATE TABLE IF NOT EXISTS checks(check_in date,check_out date,cpf text primary key)")
    CREAT_ROOM_TABLE_QUERY = ('CREATE TABLE IF NOT EXISTS room(name text,check_in text,check_out text, CPF text primary key,number text,occupied int)')  
    # INSERT_CHECKS_TABLE_QUERY=("INSERT INTO checks(check_in,check_out,cpf) VALUES(?,?,?)")
    INSERT_ROOM_QUERY = 'INSERT INTO room(name,check_in,check_out,CPF,number,occupied) VALUES (?,?,?,?,?,?)'
    # UPDATE_DATE_ROOM_QUERY = 'UPDATE checks SET check_in = ? WHERE cpf = ?'
    UPDATE_OCCUPIED_ROOM_QUERY = 'UPDATE room SET occupied = ? WHERE number = ?'
    SELECT_ROOM_QUERY = 'SELECT * FROM room WHERE CPF = ?'
    SELECT_BY_DATE_AND_NUMBER_QUERY = 'SELECT occupied FROM room WHERE number = ?'
=======
    CREATE_ROOM_TABLE_QUERY = (
        'CREATE TABLE IF NOT EXISTS room(name text(20), check_in date, check_out date, CPF text primary key, number text, occupied int)')
    INSERT_ROOM_QUERY = 'INSERT INTO room(name, check_in, check_out, CPF, number, occupied) VALUES (?,?,?,?,?,?)'
    UPDATE_NAME_QUERY = 'UPDATE room SET name = ? WHERE CPF = ?'
    UPDATE_CHECKIN_QUERY = 'UPDATE room SET check_in = ? WHERE CPF = ?'
    UPDATE_CHECKOUT_QUERY = 'UPDATE room SET check_out = ? WHERE CPF = ?'
    UPDATE_CPF_QUERY = 'UPDATE room SET CPF = ? WHERE CPF = ?'
    UPDATE_NUMBER_QUERY = 'UPDATE room SET number = ? WHERE CPF = ?'
    UPDATE_OCCUPIED_QUERY = 'UPDATE room SET occupied = ? WHERE CPF = ?'
    SELECT_NAME_QUERY = 'SELECT name FROM room WHERE CPF = ?'
    SELECT_CHECKIN_QUERY = 'SELECT check_in FROM room WHERE CPF = ?'
    SELECT_CHECKOUT_QUERY = 'SELECT check_out FROM room WHERE CPF = ?'
    SELECT_CPF_QUERY = 'SELECT CPF FROM room WHERE name = ?'
    SELECT_NUMBER_QUERY = 'SELECT number FROM room WHERE CPF = ?'
    SELECT_OCCUPIED_QUERY = 'SELECT occupied FROM room WHERE CPF = ?'
    SELECT_ALL_CHECKIN_QUERY = 'SELECT check_in FROM room' 
    SELECT_ALL_CHECKOUT_QUERY = 'SELECT check_out FROM room' 
    SELECT_ALL_OCCUPIED_QUERY = 'SELECT occupied FROM room WHERE number = ?' 
>>>>>>> Stashed changes
    DELETE_ROOM_QUERY = 'DELETE FROM room WHERE CPF = ?'
    # DELETE_CHECKS_QUERY = 'DELETE FROM checks WHERE CPF = ?'

    
    def __init__(self):
        self.conect = sqlite3.connect("banco.db")
        self.c = self.conect.cursor()
        self.c.execute(self.CREAT_ROOM_TABLE_QUERY)
        # self.c.execute(self.CREAT_CHECKS_TABLE_QUERY)
        self.conect.commit()

    def insert_room(self,name,check_in,check_out,CPF,number,occupied):
        self.c.execute(self.INSERT_ROOM_QUERY,(name,check_in,check_out,CPF,number,occupied))
        self.conect.commit()
 

    def update_date_room(self,check_in,cpf):
        self.c.execute(self.UPDATE_DATE_ROOM_QUERY,(check_in,cpf))
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
    
    def select_occupied(self,number,data):
        self.c.execute("SELECT occupied FROM room WHERE number = ? AND date = ?", (number,data)).fetchone()[0]
    
    def delete_room(self,CPF):
        self.c.execute(self.DELETE_ROOM_QUERY,(CPF,))
        self.conect.commit()
    
    # def delete_room(self,CPF):
    #     self.c.execute(self.DELETE_CHECKS_QUERY,(CPF,))
    #     self.conect.commit()
        
    def __del__(self):
        self.conect.close()