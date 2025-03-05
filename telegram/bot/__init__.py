from .handlers import start, recieve_message

from env_reader import ENVReader

start_handler = start
repeat_message = recieve_message
env = ENVReader()
