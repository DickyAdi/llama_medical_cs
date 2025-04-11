from datetime import datetime
from typing import List

def get_today() -> str:
    return datetime.now().strftime('%A')

def format_timedelta(td) -> str:
    total_seconds = td.total_seconds()
    hours, remainder = divmod(int(total_seconds), 3600)
    mins, _ = divmod(remainder, 60)
    return f"{hours:02}:{mins:02}"

def format_specialist_shift(schedule) -> List[str]:
    return [f"doctor name : {name}, day of shift : {day}, starting at {format_timedelta(start_shift)} through {format_timedelta(end_shift)}" for name, day, start_shift, end_shift in schedule]

def format_doctor_shift(schedule) -> List[str]:
    return [f"day : {day}, shift : starting at {format_timedelta(start)} through {format_timedelta(end)}" for day, start, end in schedule]

