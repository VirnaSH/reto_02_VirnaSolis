from config import config
from mysql import connector
from prefect import task

@task(name="Carga de data en bd")
def task_load_user(user_data):
  with connector.connect(**config.MYSQL_CONFIG) as db:
    with db.cursor() as cursor:
      query_insert = """
        insert into usuario(ruc, razon_social, direccion)
        values(%s, %s, %s)
      """
      cursor.execute(query_insert, user_data)
      db.commit()