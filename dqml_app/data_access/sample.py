import datetime as dt 
from dqml_app import dataset as ds 
from dqml_app import settings as sc 
from dqml_app.app_calendar import eff_date as ed 

def query_random_sample(dataset_id: str, eff_date: dt.date):
    # table: str, time_column: str, eff_date: dt.date, sample_size: int

    eff_date_str = ed.fmt_date_as_yyyymmdd(eff_date)
    src_file_path = sc.resolve_app_path(dataset.resolve_file_path(eff_date_str))
    src_file_records = uff.uf_read_delim_file_to_list_of_dict(file_path=src_file_path)

    sample_size = dataset.sample_size

    return random.sample(src_file_records, sample_size)

    # ticket_data_today = [
    #     {
    #         'listid': 219247,
    #         'listtime': '2022-05-03 11:04:54', 
    #         'sellerid' 12619, 
    #         'numtickets': 4, 
    #         'venuecity': 'New York City', 
    #         'venuestate': 'NY', 
    #         'venueseats': 0, 
    #     }, 
    #     {
    #         'listid': 7743,
    #         'listtime': '2022-05-03 19:36:02', 
    #         'sellerid' 4474, 
    #         'numtickets': 24, 
    #         'venuecity': 'Green Bay', 
    #         'venuestate': 'WI', 
    #         'venueseats': 72922, 
    #     }, 
    # ] 

    # ticket_data_not_today = [
    #     {
    #         'listid': 227155,
    #         'listtime': '2022-05-02 00:31:03', 
    #         'sellerid' 385, 
    #         'numtickets': 6, 
    #         'venuecity': 'New York City', 
    #         'venuestate': 'NY', 
    #         'venueseats': 0, 
    #     }, 
    #     {
    #         'listid': 41479,
    #         'listtime': '2022-05-02 14:19:31', 
    #         'sellerid' 1674, 
    #         'numtickets': 8, 
    #         'venuecity': 'Mountain View', 
    #         'venuestate': 'CA', 
    #         'venueseats': 22900, 
    #     }, 
    # ] 

    # if table == 'ticket':
    #     if eff_date == '2022-05-03':
    #         return ticket_data_today 
    #     else:
    #         return ticket_data_not_today 
    