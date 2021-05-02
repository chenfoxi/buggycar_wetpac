from datetime import datetime, timedelta


# def get_current_date(tz='Pacific/Auckland'):
def get_current_date():
    # spec_tz = timezone(tz)
    spec_dt = datetime.now()
    return spec_dt

def get_date_by_timedelta(local_dt, delta_day=0):
    new_dt = get_dt_by_timedelta(local_dt, delta_day)
    return (new_dt.year, new_dt.month, new_dt.day)

def get_fstr_dt_by_timedelta(local_dt, delta_day=0, fstr="%Y-%m-%d", need_day_suffix=False):
    
    new_dt = get_dt_by_timedelta(local_dt, delta_day)
    if need_day_suffix:
        fstr = fstr + day_suffix(new_dt.day)
    f_str_dt = new_dt.strftime(fstr)
    return f_str_dt

def get_dt_by_timedelta(local_dt, delta_day=0):
    """calculate the datetime by timedelta

    Args:
        local_dt (datetime): local datetime
        delta_day (int, optional): add or substract day. Defaults to 0.

    Returns:
        datetime: new datetime that has been added or substracted
    """    
    if delta_day >= 0:
        new_dt = local_dt + timedelta(days=delta_day)
    else: 
        new_dt = local_dt - timedelta(days=delta_day)
    return new_dt

def day_suffix(day):
  suffix = ""
  if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = "th"
  else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]
  return suffix