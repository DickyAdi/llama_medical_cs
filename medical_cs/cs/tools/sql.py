import mysql.connector
import pymysql
import os
pymysql.install_as_MySQLdb()

def exc_query(query, host='localhost', verbose=True, returnable=True):
    """
    This function execute an sql query.
    
    Args:
        query (str): A valid sql query.
        host (str): The host or ip address where the database's located. Default is localhost
        verbose (bool): Whether to print if query is executed successfuly. Default is True
        returnable (bool): Whether to return a value from the given sql operation. Default is True
    """
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
    """
    A query builder for schedule checking.
    
    Args:
        field (str): A database column that needs to be checked.
        value (str): A value that needs to be matched.
        base_table (str): A table where the operation is executed. Default is doctor_schedule.
        specialist (bool): Whether it's a specialist or doctor schedule checking. Default is False.
    Returns:
        tuple: A tuple that contains the query of doctor/specialist checking and the schedule checking.
    """
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
    """
    A wrapper for getting the credentials from .env
    
    Returns:
        dict: A dictionary containing all the necessary credentials.
    """
    return {
        'db_uname' : os.getenv("DATABASE_UNAME"),
        'db_name' : os.getenv("DATABASE_NAME"),
        'db_pw': os.getenv("DATABASE_PASSWORD")
    }