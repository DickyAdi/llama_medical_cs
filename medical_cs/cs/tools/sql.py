import mysql.connector
import pymysql
import os
pymysql.install_as_MySQLdb()

def exc_query(query, host='localhost', verbose=True, returnable=True):
    creds = get_db_credentials()
    conn = mysql.connector.connect(host=host, user=creds['db_uname'], password=creds['db_pw'], database=creds['db_name'])
    cur = conn.cursor()
    try:
        cur.execute(query)
        if verbose:
            print('Query executed successfully.')
        
        if returnable:
            results = cur.fetchall()
            return results
    except mysql.connector.Error as err:
        return (f'Error: {err}')
    finally:
        cur.close()
        conn.close()

def schedule_query_builder(field:str, value:str, base_table:str='doctor_schedule', specialist=False) -> tuple[str, str]:
    sql_template = f"""
    SELECT COUNT({field}) FROM {base_table}
    WHERE LOWER({field}) = '{value.lower()}';
    """
    if specialist:
        schedule_template = f"""
        SELECT name, day, start_time, end_time FROM doctor_schedule
        WHERE LOWER({field}) = '{value.lower()}';
        """
    else:
        schedule_template = f"""
        SELECT day, start_time, end_time FROM doctor_schedule
        WHERE LOWER({field}) = '{value.lower()}';
        """
    
    return sql_template, schedule_template

def get_db_credentials():
    return {
        'db_uname' : os.getenv("DATABASE_UNAME"),
        'db_name' : os.getenv("DATABASE_NAME"),
        'db_pw': os.getenv("DATABASE_PASSWORD")
    }