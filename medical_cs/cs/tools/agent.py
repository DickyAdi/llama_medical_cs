from .utils.time import get_today, format_doctor_shift, format_specialist_shift
from .sql import exc_query, schedule_query_builder
import calendar

def check_schedule(doctor:str) -> str:
    """Check doctor schedule availability. Only call this tool/function when user asks for a doctor availability or has an intent of checking doctor availability BASED ON THE DOCTORS NAME NOT THE SPECIALIZATIONS NAME.

    Usage:
        - This function should only be called when the user explicitly asks for a doctor's availability BASED ON THE NAME.
          or has an intent to check whether a specific doctor is available.
        - The `doctor` parameter must contain the doctor's name (with titles like Dr., dr. for example dr. dummy).
        - `doctor` parameter must contain doctor's name and with the degree, if only name provided then the degree supposed to be added for example doctor dummy to dr. dummy or dummy to dr. dummy

    Args:
        doctor (str): The name of the doctor whose schedule needs to be checked.
    """
    today = get_today()
    sql_query, schedule_query = schedule_query_builder('name', doctor)
    res = exc_query(sql_query, returnable=True, verbose=False)
    if res[0][0] > 0:
        schedule = exc_query(schedule_query, returnable=True, verbose=False)
        time_shift = format_doctor_shift(schedule)
        # response_template = """
        # today is {today} and {doctor} schedule is below.
        # {shift}
        # explain the schedule to the user.
        # Never over complicate things.
        # If {today} is not listed in the schedule above, then {today} is not available for {doctor}.
        # """
        response_template = """
        You are a helpful hospital customer service chatbot.
        
        Today is {today}. Based on the provided schedule for {doctor}, first explain the doctor's weekly schedule, then inform the user of today's availibility. Do not assume anything outside the schedule.
        
        Schedule:
        {shift}
        
        Instructions:
        1. Start by summarizing and explaining the full weekly schedule clearly and concisely
        2. Then, describe the doctor's availibility for today ({today}) or the specific time if the user is asking for a specific day.
        3. Do not say a day is unavailable if it's listed in the schedule.
        4. Be friendly and clear.
        5. Remember, you could help the user for their booking if they want.
        6. Never assume the gender of the doctor, just say the name of the doctor if you refer to the doctor.
        """
        return response_template.format(today=today, doctor=doctor, shift=time_shift)
    else:
        return f'{doctor} might not exists on the database or not available'

def check_specialist_schedule(specialist:str) -> str:
    """Check doctor schedule based on specialization of the doctor. Only call this tool/function when user asks for a doctor availability or has an intent of checking doctor availability based on the name of a doctor specializations.
    
    Usage:
        - This function or tool should only be called when the user explicitely asks for a doctor schedule based on the doctor specializations or has an intent to check whether a specific specializations available.
        - `specialist` parameter should be a valid doctor specialization name in a medical fields.
        - Never make up a name of a specialist, if you do not know the name of the specializations, SKIP AND NEVER CALL THIS TOOL, instead asks for clarification to the user.
        
    Args:
        - specialist (str): The name of the doctor specializations whose schedule needs to be checked.
    """
    sql_template, schedule_template = schedule_query_builder('specialization_name', specialist, specialist=True)
    today = get_today()
    res = exc_query(sql_template, returnable=True, verbose=False)
    if res[0][0] > 0:
        schedule = exc_query(schedule_template, returnable=True, verbose=False)
        time_shift = format_specialist_shift(schedule)
        response_template = """
        You are a helpful hospital customer service chatbot.
        
        Today is {today}. Based on the provided schedule for {specialist} specialist, first explain the specialist's weekly schedule, then inform the user of today's availability. Do not assume anything outside the schedule.
        
        Schedule:
        {shift}
        
        Instructions:
        1. Start by summarizing and explaining the full weekly schedule clearly and concisely
        2. Then, describe the specialist's availibility for today ({today}) or the specific time if the user is asking for a specific day.
        3. Do not say a day is unavailable if it's listed in the schedule.
        4. Be friendly and clear.
        5. Remember, you could help the user for their booking if they want.
        6. Never assume the gender of the doctor, just say the name of the doctor if you refer to the doctor.
        """
        return response_template.format(today=today, specialist=specialist, shift=time_shift)
    else:
        return f'{specialist} specialists may not exists in the database or hospital'

def validate_booking(doctor_name:str, booking_day:str, booking_time:str) -> str:
    """The validate_booking tool checks whether a doctor’s appointment can be scheduled based on the provided doctor’s name, booking day, and booking time. It validates the input format and queries the doctor’s availability from the database.
    
    Usage:
        - Requests to book an appointment with a doctor.
        - Inquires about whether a doctor is available at a specific time.
        - Confirms if a selected appointment time is valid.
        
    Args:
        - doctor_name (str): The name of the doctor whose schedule is being checked.
        - booking_day (str): The day of the week for the requested appointment (e.g., “Monday”).
        - booking_time (str): The time of the appointment in HH:MM format.
    """
    if booking_day.capitalize() not in list(calendar.day_name):
        return f'day {booking_day} is not valid!'
    if booking_time:
        try:
            booking_time = datetime.strptime(booking_time, '%H:%M').time()
        except:
            return f'There is an error when parsing the time, make sure the `booking_time` parameter is in HH:MM format!'
    sql_template = """
    SELECT name, day, start_time, end_time FROM doctor_schedule
    WHERE LOWER(name) = '{doctor_name}' AND LOWER(day) = '{booking_day}' AND '{booking_time}' BETWEEN start_time AND end_time;
    """
    sql_query = sql_template.format(doctor_name=doctor_name, booking_day=booking_day, booking_time=booking_time)
    res = exc_query(sql_query, returnable=True, verbose=False)
    if len(res) > 0:
        return f'Booking of {doctor_name} in {booking_day} at {booking_time} has been proceed. Kindly inform the user and only asks for a confirmation about the booking without any other details!'
    else:
        return f'Booking of {doctor_name} in {booking_day} at {booking_time} cannot been proceed as the schedule or booking might be invalid.'