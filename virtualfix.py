import ctypes
import time
from datetime import datetime
import os

def set_system_time(new_time):
    """Set the system time to the specified new_time."""
    # Check if the user has admin rights
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Set the system time
        os.system(f"time {new_time.strftime('%H:%M:%S')}")
    else:
        print("This script requires administrative privileges to modify system time.")

def synchronize_time():
    """Synchronize the system time with an internet time server."""
    try:
        # Use the Windows Time Sync command to sync with an internet server
        os.system("w32tm /resync")
        print("System time has been synchronized with the internet time server.")
    except Exception as e:
        print(f"An error occurred while synchronizing time: {e}")

def main():
    print("VirtualFix: Adjusting system clock settings for better time management.")
    
    # Display the current system time
    current_time = datetime.now()
    print(f"Current system time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Synchronize with internet time servers
    synchronize_time()

    # Display the updated system time
    updated_time = datetime.now()
    print(f"Updated system time: {updated_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()