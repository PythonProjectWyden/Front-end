import sqlite3

class RoomDB:
    CREAT_ROOM_TABLE_QUERY = ('CREATE TABLE IF NOT EXISTS room(name text, check_in date, check_out date, CPF text primary key,number text,occupied int)')  
    INSERT_ROOM_QUERY = 'INSERT INTO room(name,check_in,check_out,CPF,number,occupied) VALUES (?,?,?,?,?,?)'
    UPDATE_DATE_ROOM_QUERY = 'UPDATE room SET check_in = ? WHERE cpf = ?'
    UPDATE_OCCUPIED_ROOM_QUERY = 'UPDATE room SET occupied = ? WHERE number = ?'
    SELECT_NAME_QUERY = 'SELECT name FROM room WHERE CPF = ?'
    SELECT_CHECKIN_QUERY = 'SELECT check_in FROM room WHERE CPF = ?'
    SELECT_CHECKOUT_QUERY = 'SELECT check_out FROM room WHERE CPF = ?'
    SELECT_CPF_QUERY = 'SELECT CPF FROM room WHERE name = ?'
    SELECT_NUMBER_QUERY = 'SELECT number FROM room WHERE CPF = ?'
    SELECT_OCCUPIED_QUERY = 'SELECT occupied FROM room WHERE CPF = ?'
    DELETE_ROOM_QUERY = 'DELETE FROM room WHERE CPF = ?'

    def __init__(self):
        self.conect = sqlite3.connect("banco.db")
        self.c = self.conect.cursor()
        self.c.execute(self.CREAT_ROOM_TABLE_QUERY)
        self.conect.commit()

    def insert_room(self, name, check_in, check_out, CPF, number, occupied):
        self.c.execute(self.INSERT_ROOM_QUERY, (name, check_in, check_out, CPF, number, occupied))
        self.conect.commit()

    def update_date_room(self, check_in, cpf):
        self.c.execute(self.UPDATE_DATE_ROOM_QUERY, (check_in, cpf))
        self.conect.commit()
        
    def update_occupied_room(self, number):
        current_occupied = self.c.execute("SELECT occupied FROM room WHERE number = ?", (number)).fetchone()[0]
        new_occupied = not current_occupied
        self.c.execute(self.UPDATE_OCCUPIED_ROOM_QUERY, (new_occupied, number))
        self.conect.commit()
    
    def delete_room(self, CPF):
        self.c.execute(self.DELETE_ROOM_QUERY, (CPF))
        self.conect.commit()

    def select_name(self, cpf):
        self.c.execute(self.SELECT_NAME_QUERY, (cpf))
        return self.c.fetchall()
    
    def select_checkin(self, cpf):
        self.c.execute(self.SELECT_CHECKIN_QUERY, (cpf))
        return self.c.fetchall()
    
    def select_checkout(self, cpf):
        self.c.execute(self.SELECT_CHECKOUT_QUERY, (cpf))
        return self.c.fetchall()
    
    def select_cpf(self, name):
        self.c.execute(self.SELECT_CPF_QUERY, (name))
        return self.c.fetchall()
    
    def select_number(self, cpf):
        self.c.execute(self.SELECT_NUMBER_QUERY, (cpf))
        return self.c.fetchall()
    
    def select_occupied(self, cpf):
        self.c.execute(self.SELECT_OCCUPIED_QUERY, (cpf))
        return self.c.fetchall()

    def __del__(self):
        self.conect.close()