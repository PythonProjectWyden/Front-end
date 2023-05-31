import sqlite3


class RoomDB:
    CREATE_ROOM_TABLE_QUERY = (
        'CREATE TABLE IF NOT EXISTS room(name text, check_in date, check_out date, CPF text primary key, number text, occupied int)')
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
    SELECT_ALL_OCCUPIED_QUERY = 'SELECT occupied FROM room WHERE number = ?'
    DELETE_ROOM_QUERY = 'DELETE FROM room WHERE CPF = ?'

    def __init__(self):
        self.connection = sqlite3.connect("banco.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.CREATE_ROOM_TABLE_QUERY)
        self.connection.commit()

    def insert_room(self, name, check_in, check_out, CPF, number, occupied):
        self.cursor.execute(self.INSERT_ROOM_QUERY,
                            (name, check_in, check_out, CPF, number, occupied))
        self.connection.commit()

    def update_name(self, new_name, CPF):
        self.cursor.execute(self.UPDATE_NAME_QUERY, (new_name, CPF))
        self.connection.commit()

    def update_checkin(self, new_checkin, CPF):
        self.cursor.execute(self.UPDATE_CHECKIN_QUERY, (new_checkin, CPF))
        self.connection.commit()

    def update_checkout(self, new_checkout, CPF):
        self.cursor.execute(self.UPDATE_CHECKOUT_QUERY, (new_checkout, CPF))
        self.connection.commit()

    def update_CPF(self, new_CPF, old_CPF):
        self.cursor.execute(self.UPDATE_CPF_QUERY, (new_CPF, old_CPF))
        self.connection.commit()

    def update_number(self, new_number, CPF):
        self.cursor.execute(self.UPDATE_NUMBER_QUERY, (new_number, CPF))
        self.connection.commit()

    def update_occupied(self, new_occupied, CPF):
        self.cursor.execute(self.UPDATE_OCCUPIED_QUERY, (new_occupied, CPF))
        self.connection.commit()

    def delete_room(self, CPF):
        self.cursor.execute(self.DELETE_ROOM_QUERY, (CPF))
        self.connection.commit()

    def select_name(self, CPF):
        self.c.execute(self.SELECT_NAME_QUERY, (CPF))
        return self.c.fetchall()

    def select_checkin(self, CPF):
        self.c.execute(self.SELECT_CHECKIN_QUERY, (CPF))
        return self.c.fetchall()

    def select_checkout(self, CPF):
        self.c.execute(self.SELECT_CHECKOUT_QUERY, (CPF))
        return self.c.fetchall()

    def select_CPF(self, name):
        self.c.execute(self.SELECT_CPF_QUERY, (name))
        return self.c.fetchall()

    def select_number(self, CPF):
        self.c.execute(self.SELECT_NUMBER_QUERY, (CPF))
        return self.c.fetchall()

    def select_occupied(self, CPF):
        self.c.execute(self.SELECT_OCCUPIED_QUERY, (CPF))
        return self.c.fetchall()

    def select_all_occupied(self):
        self.c.execute(self.SELECT_ALL_OCCUPIED_QUERY)
        return self.c.fetchall()

    def __del__(self):
        self.conect.close()
