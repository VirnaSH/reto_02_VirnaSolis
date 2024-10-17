from prefect import flow
from tasks.task_utils import task_init_table
from tasks.task_utils import task_init_table, task_get_user_from_db
from tasks.task_extract_RUC import task_extract_csv, task_extract_ruc
from tasks.utils import validate_ruc, handle_invalid_ruc
from tasks.task_load_ruc import task_load_user


BASELINE_TASKS = True
DATA_PATH = "./resources/user.csv"


@flow(name="ETL APIPERU", log_prints=True)
def main_flow():

  if BASELINE_TASKS:
    task_init_table()

  initial_user_data = task_extract_csv(DATA_PATH)
  for user in initial_user_data:
    ruc = user[0]
    razon_social = user[1]
    
    if validate_ruc(ruc):
      user_exists = task_get_user_from_db(ruc)
      
      if not user_exists:
        api_user_data = task_extract_ruc(ruc)
        print(api_user_data)
        user_data = (ruc, *api_user_data)
        task_load_user(user_data)
    else:
      handle_invalid_ruc(ruc)

if __name__ == "__main__":
  main_flow()