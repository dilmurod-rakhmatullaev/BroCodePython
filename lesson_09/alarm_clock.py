import os
import time
import datetime
import pygame

def set_alarm(alarm_time):
    """Setting alarm time"""
    print(f"Alarm set for {alarm_time}")

    # Checking file existence
    sound_file = "alarm.mp3"
    if not os.path.exists(sound_file):
        print(f"Error: '{sound_file}' not found")
        return

    # Download music in advance
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
    except Exception as e:
        print(f" Error loading sound: {e}")
        return

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}", end="\r")

        if current_time == alarm_time:
            print("\nWake Up!")
            pygame.mixer.music.play()

            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():    # Returns True as long as music is playing
                time.sleep(1)   # Check once per second to prevent high CPU usage

            print("Alarm finished")
            is_running = False

        time.sleep(1)

def get_valid_time():
    """Asks the user for the time in the correct format"""
    while True:
        alarm_input = input("Enter the alarm time (HH:MM:SS): ")

        parts = alarm_input.split(":")
        if len(parts) == 3:
            try:
                h, m, s = map(int, parts)
                if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
                    return alarm_input
            except ValueError:
                pass

        print("Invalid format! Please use HH:MM:SS")

if __name__ == "__main__":
    print("Python Alarm Clock")
    alarm_time = get_valid_time()
    set_alarm(alarm_time)