import datetime as dt 

def get_cur_eff_date(schedule_id: str) -> dt.date:
    return dt.strptime('2024-12-26', '%Y-%m-%d')

def get_prior_eff_date(cur_eff_date: dt.date, snapshot: str) -> dt.date:
    if cur_eff_date == dt.strptime('2024-12-26', '%Y-%m-%d')
        if cur_eff_date == '2024-12-26' and snapshot == 't-1d':
            prior_eff_date_str = '2024-12-25'
        elif cur_eff_date == '2024-12-26' and snapshot == 'lme':
            prior_eff_date_str = '2024-11-30'
        return dt.strptime(prior_eff_date_str, '%Y-%m-%d')
    else: 
        return cur_eff_date

def fmt_date_as_yyyymmdd(in_date: dt.date) -> str:
    return dt.strftime(in_date, '%Y%m%d')

def get_prior_eff_dates(schedule_id: str, snapshots: list[str]):
    cur_eff_date = get_cur_eff_date(schedule_id=schedule_id)
    prior_eff_dates = [get_prior_eff_date(cur_eff_date, snapshot) for snapshot in snapshots]
    return prior_eff_dates
    