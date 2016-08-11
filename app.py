import sys
import logging
import rds_config
import pymysql
#rds settings

rds_host  = rds_config.host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306

logger = logging.getLogger()
logging.basicConfig()

logger.setLevel(logging.INFO)

server_address = (rds_host, port)
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=15)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    print "error"
    sys.exit()


logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    item_count = 0

    with conn.cursor() as cur:
        cur.execute("drop table Employee3")
        cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        data = event
        for user in data['users']:
            sql = "INSERT INTO `Employee3` (`EmpID`, `Name`) VALUES (%s, %s)"
            cur.execute(sql, (user['id'], user['name']))
        conn.commit()
        cur.execute("select * from Employee3")
        for row in cur:
            item_count += 1
            logger.info(row)


    return "Added %d items from RDS MySQL table" %(item_count)

handler({"users": [{"id":4, "name": "David"}]},"")