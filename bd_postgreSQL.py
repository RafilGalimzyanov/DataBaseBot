import psycopg2
from bd_google import verify_data
from handlers.users.parsing import dollar

'''
Запрос на удаление таблицы
'''
def delete_table():
    con = psycopg2.connect(
      database="delivery_db",
      user="postgres",
      password="admin",
      host="localhost",
      port="5433"
    )

    print("Database opened successfully")
    cur = con.cursor()

    cur.execute('''DROP TABLE DATA;''')

    print("Table delete")
    con.commit()
    con.close()

def filling_bd():
    data = verify_data()
    doll = dollar()

    try:
        delete_table()
    except:
        pass

    con = psycopg2.connect(
      database="delivery_db",
      user="postgres",
      password="admin",
      host="localhost",
      port="5433"
    )

    print("Database opened successfully")
    cur = con.cursor()

    cur.execute('''CREATE TABLE DATA
        (NUMBER INT NOT NULL,
        NUM_ORD CHAR(7) NOT NULL,
        PRICE_D DOUBLE PRECISION,
        PRICE_R DOUBLE PRECISION,
        TIMING DATE);''')


    for i in range(len(data)):
        num = data[i][0]
        num_ord = data[i][1]
        price_d = data[i][2]
        price_r = float(data[i][2])*doll
        price_r = float('{:.3f}'.format(price_r))
        time = data[i][3].replace('.', '-')
        time = time[6:]+time[2:6]+time[:2]

        cur.execute(
           f"INSERT INTO DATA (NUMBER, NUM_ORD, PRICE_D, PRICE_R, TIMING) VALUES ({num}, {num_ord}, {price_d}, {price_r},'{time}')"
        )

    print("Table created successfully")
    con.commit()
    con.close()