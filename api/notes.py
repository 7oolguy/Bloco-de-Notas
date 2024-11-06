import oracledb
from datetime import datetime
import uuid

def get_cursor():
    db_user = 'rm558885'  # username
    db_key = '140106'     # password
    try:
        connection = oracledb.connect(
            user=db_user,
            password=db_key,
            dsn="oracle.fiap.com.br/orcl"
        )
        return connection, connection.cursor()
    except Exception as err:
        print("Ops!! - Connect to DB - " + str(datetime.now()) + " - " + str(err))
        return None, None

def create(data):
    connection, cursor = get_cursor()
    if not cursor:
        return {"error": "Failed to connect to the database"}

    # Define SQL as an empty string initially to handle error logging
    SQL = ""

    try:
        print("Successfully connected to Oracle Database: Create - " + str(datetime.now()))

        cursor.execute("SELECT MAX(id) FROM nota")
        max_id = cursor.fetchone()[0]

        new_id = max_id + 1 if max_id is not None else 1

        SQL = f"""INSERT INTO nota
                  (id, title, content)
                  VALUES ({new_id},'{data["title"]}', '{data["content"]}')"""

        cursor.execute(SQL)
        connection.commit()
        print("Record created successfully.")

    except Exception as err:
        print("Ops!! - Create - " + str(datetime.now()) + " - " + str(err))
        print("SQL: ", SQL)  # SQL will now be available for logging even if an error occurs

    finally:
        cursor.close()
        connection.close()


def read(data):
    connection, cursor = get_cursor()
    data_out = {"now": str(datetime.now())}

    if not cursor:
        return {"error": "Failed to connect to the database"}

    try:
        print("Successfully connected to Oracle Database: Read - " + str(datetime.now()))

        SQL = f"SELECT * FROM nota WHERE id = {data['id']}"
        cursor.execute(SQL)

        for registro in cursor:
            print(f"Registro: {registro}")
            data_out["id"], data_out["title"], content = registro

            if isinstance(content, oracledb.LOB):
                data_out["content"] = content.read().decode('utf-8')  # Decode to UTF-8 string
            else:
                data_out["content"] = content

        print(data_out)

    except Exception as err:
        print("Ops!! - Read - " + str(datetime.now()) + " - " + str(err))

    finally:
        cursor.close()
        connection.close()

    return data_out

def delete(data):
    connection, cursor = get_cursor()
    out_message = {"now": str(datetime.now())}

    if not cursor:
        return {"error": "Failed to connect to the database"}

    try:
        print("Successfully connected to Oracle Database: Delete - " + str(datetime.now()))

        SQL = f"DELETE FROM nota WHERE id = {data['id']}"
        cursor.execute(SQL)
        connection.commit()

        print("Record deleted successfully.")

    except Exception as err:
        print("Ops!! - Delete - " + str(datetime.now()) + " - " + str(err))
        print("SQL: ", SQL)
        out_message["error"] = str(err)

    finally:
        cursor.close()
        connection.close()

    return out_message

def update(data):
    connection, cursor = get_cursor()

    if not cursor:
        return {"error": "Failed to connect to the database"}

    try:
        print("Successfully connected to Oracle Database: Update - " + str(datetime.now()))

        SQL = f"""UPDATE nota
                  SET title = '{data["title"]}', content = '{data["content"]}'
                  WHERE id = {data["id"]}"""

        cursor.execute(SQL)
        connection.commit()
        print("Record updated successfully.")

    except Exception as err:
        print("Ops!! - Update - " + str(datetime.now()) + " - " + str(err))
        print("SQL: ", SQL)

    finally:
        cursor.close()
        connection.close()

def get_db_info():
    connection, cursor = get_cursor()
    out_message = {"service_time": str(datetime.now())}

    if not cursor:
        return {"error": "Failed to connect to the database"}

    try:
        print("Successfully connected to Oracle Database: DB Info - " + str(datetime.now()))

        SQL = "SELECT version, SYSDATE db_time, USER, 'ok' STATUS FROM V$INSTANCE"
        cursor.execute(SQL)

        for registro in cursor:
            out_message["db_version"], out_message["now"], out_message["status"] = registro

    except Exception as err:
        print("Ops!! - DB Info - " + str(datetime.now()) + " - " + str(err))
        out_message["error"] = str(err)

    finally:
        cursor.close()
        connection.close()

    return out_message
