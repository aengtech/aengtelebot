from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hi', 'hello', 'sup'):
        return "Hey! How's it going?"

    if user_message in ('Who are you', 'Who are you?', 'Who you?'):
        return "I am Aeng Fist Bot!"

    if user_message in ('time', 'date?', 'when?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you, try asking me for the 'time' or say Hello"