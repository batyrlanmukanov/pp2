import psycopg2 as pgsql

def insert_or_update():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='Batyr2402',
            host='localhost',
        )
        con = connection.cursor()

        con.execute("""
            CREATE OR REPLACE FUNCTION insert_or_update_user(name_param TEXT, surname_param TEXT, phone_param TEXT) 
            RETURNS VOID AS 
            $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phone_number WHERE name = name_param OR surname = surname_param) THEN
                    UPDATE phone_number SET number_value = phone_param WHERE name = name_param OR surname = surname_param;
                ELSE
                    INSERT INTO phone_number (name, surname, number_value) VALUES (name_param, surname_param, phone_param);
                END IF;
            END;
            $$
            LANGUAGE plpgsql;
        """)

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

def insert_or_update_user(name, surname, phone):
    try:
        connection = pgsql.connect(
            database="Phonebook",
            user='postgres',
            password='qwerty',
            host='localhost',
        )
        con = connection.cursor()
        con.callproc('insert_or_update_user', (name, surname, phone))
        
        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

insert_or_update()
insert_or_update_user('Nuriman', 'Baltabayev', '1234567890')