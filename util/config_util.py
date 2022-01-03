import pymysql
from util import property
from util import deeplab

login_user = {}

file_path = '../source/config.properties'
properties = property.parse(file_path)

host = properties.get('host')
user = properties.get('user')
password = properties.get('password')
database = properties.get('database')
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
deeplab_model = deeplab.DeepLabModel(properties.get('deeplab_weights'))
# if __name__ == '__main__'
# connection = pymysql.connect(host='localhost',
#                                  user='root',
#                                  password='root1234',
#                                  database='project',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor
#                                  )
