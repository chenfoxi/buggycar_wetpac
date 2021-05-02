# execute before the test 
# prepare all data by execute sql files in sql folder

import pymysql.cursors
import os
import sys

def parse_sql(filename):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for line in data:

        if line.strip() == '' or line.startswith('--'):
            continue
        if DELIMITER not in line or DELIMITER != line.strip()[-1]:
            stmt += line
            continue
        if DELIMITER in line:
            if stmt:
                stmt += line
                stmts.append(stmt.strip())
                stmt = ''
            else:
                stmts.append(line.strip())
    return stmts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("arguments number is incorrect, must be: python prepare_sql_data.py [script].sql")
        exit()
    print(os.getenv('INFOODLE_DB_HOST'))
    print(os.getenv('INFOODLE_DB_USER'))
    print(os.getenv('INFOODLE_DB_PASS'))
    print(os.getenv('INFOODLE_DB_NAME'))
    # Connect to the database
    connection = pymysql.connect(host=os.getenv('INFOODLE_DB_HOST', default='127.0.0.1'),
                                 user=os.getenv('INFOODLE_DB_USER', default='root'),
                                 password=os.getenv('INFOODLE_DB_PASS', default=''),
                                 db=os.getenv('INFOODLE_DB_NAME', default='infoodle'),
                                 charset='latin1',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            stmts = parse_sql(sys.argv[1])
            for stmt in stmts:
                cursor.execute(stmt)
    
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()