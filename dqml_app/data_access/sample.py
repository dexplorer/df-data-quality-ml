import datetime as dt 

def query_random_sample(table: str, time_column: str, eff_date: dt.date, sample_size: int):
    ticket_data_today = [
        {
            'listid': 219247,
            'listtime': '2022-05-03 11:04:54', 
            'sellerid' 12619, 
            'numtickets': 4, 
            'venuecity': 'New York City', 
            'venuestate': 'NY', 
            'venueseats': 0, 
        }, 
        {
            'listid': 7743,
            'listtime': '2022-05-03 19:36:02', 
            'sellerid' 4474, 
            'numtickets': 24, 
            'venuecity': 'Green Bay', 
            'venuestate': 'WI', 
            'venueseats': 72922, 
        }, 
    ] 

    ticket_data_not_today = [
        {
            'listid': 227155,
            'listtime': '2022-05-02 00:31:03', 
            'sellerid' 385, 
            'numtickets': 6, 
            'venuecity': 'New York City', 
            'venuestate': 'NY', 
            'venueseats': 0, 
        }, 
        {
            'listid': 41479,
            'listtime': '2022-05-02 14:19:31', 
            'sellerid' 1674, 
            'numtickets': 8, 
            'venuecity': 'Mountain View', 
            'venuestate': 'CA', 
            'venueseats': 22900, 
        }, 
    ] 

    if table == 'ticket':
        if eff_date == '2022-05-03':
            return ticket_data_today 
        else:
            return ticket_data_not_today 
    