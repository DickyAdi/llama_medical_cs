from datetime import datetime
from typing import List

def get_today() -> str:
    """
    Get todays day in string.
    
    Returns:
        str: Todays day in string
    """
    return datetime.now().strftime('%A')

def format_timedelta(td) -> str:
    """
    A function to format from timedelta to HH:MM format.
    
    Args:
        td (timedelta): MySQL timedelta
    
    Returns:
        str: HH:MM Formatted time delta
    """
    total_seconds = td.total_seconds()
    hours, remainder = divmod(int(total_seconds), 3600)
    mins, _ = divmod(remainder, 60)
    return f"{hours:02}:{mins:02}"

def format_specialist_shift(schedule) -> List[str]:
    """
    A function to format specialist time shift.
    
    Args:
        schedule (mysql object): Mysql object from check_specialist_schedule agent.
    
    Returns:
        list: A list of formatted string.
    """
    return '\n'.join([f"* doctor name : {name}, day of shift : {day}, starting at {format_timedelta(start_shift)} through {format_timedelta(end_shift)}" for name, day, start_shift, end_shift in schedule])

def format_doctor_shift(schedule) -> List[str]:
    """
    A function to format doctor time shift.
    
    Args:
        schedule (mysql object): Mysql object from check_schedule agent.
    
    Returns:
        list: A list of formatted string.
    """
    return '\n'.join([f"* day : {day}, shift : starting at {format_timedelta(start)} through {format_timedelta(end)}" for day, start, end in schedule])

