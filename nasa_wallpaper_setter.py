import os
import datetime
import requests
import ctypes
import logging
import json

# Configuration
NASA_API_KEY = "DEMO_KEY"  # Replace with your NASA API key
SAVE_FOLDER_PATH = r"placeholder"  # Replace with your desired folder path - e.g. "C:\\Users\\myuser\\Pictures\\Nasa_APOD"
JSON_STATE_FILE = f"{SAVE_FOLDER_PATH}\\state.json"
APOD_URL = f"https://api.nasa.gov/planetary/apod"
DATE_TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

logging.basicConfig(
    filename=f"{SAVE_FOLDER_PATH}\\apod_logs.log",
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

def load_state():
    """
    Load the state from the JSON file.
    """
    if os.path.exists(JSON_STATE_FILE):
        with open(JSON_STATE_FILE, "r") as file:
            return json.load(file)
    return {"date": None, "count": 0}

def save_state(state):
    """
    Save the state to JSON file.
    """
    with open(JSON_STATE_FILE, "w") as file:
        json.dump(state, file)

def get_run_count():
    """
    Determine the run count for today.
    """
    state = load_state()

    if state["date"] == DATE_TODAY:
        state["count"] += 1
    else:
        state["date"] = DATE_TODAY
        state["count"] = 1
    
    save_state(state)
    return state["count"]

def get_nasa_apod():
    """
    Fetches the NASA Astronomy Picture of the Day (APOD) and saves it as today's date.
    """
    try:
        # Fetch APOD data
        response = requests.get(APOD_URL, params={"api_key" : NASA_API_KEY})
        response.raise_for_status()  # Raise error for bad responses

        data = response.json()
        media_type = data.get("media_type", "")
        if media_type != "image":
            logging.error(f"NASA APOD is not an image today: {data.get('url')}")
            return None

        image_url = data.get("hdurl")
        image_title = data.get("title")
        file_extension = os.path.splitext(image_url)[-1].lower()
        logging.info(f"Today's image: {image_title}")

        # Download the image
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        wallpaper_path = os.path.join(SAVE_FOLDER_PATH, f"{DATE_TODAY}{file_extension}")

        # Check if the wallpaper already exists
        if os.path.exists(wallpaper_path):
            logging.info(f"Today's wallpaper already exists: {wallpaper_path}")
            return wallpaper_path

        # Save the image
        with open(wallpaper_path, "wb") as img_file:
            img_file.write(img_response.content)

        logging.info(f"Downloaded today's APOD to: {wallpaper_path}")
        return wallpaper_path
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching NASA APOD: {str(e)}")
        return None

def set_wallpaper(image_path):
    """
    Sets the provided image as the desktop wallpaper.
    """
    if os.path.exists(image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        logging.info(f"Wallpaper set to: {image_path}")
    else:
        logging.error(f"Wallpaper file not found: {image_path}")

if __name__ == "__main__":
    # Ensure the folder exists
    os.makedirs(SAVE_FOLDER_PATH, exist_ok=True)

    run_count = get_run_count()

    logging.info(f"Run number: {run_count}")

    # Get NASA's APOD and set it as wallpaper
    if(run_count == 1):
        logging.info(f"Running the script for the {run_count}st time today, downloading and setting wallpaper.")
        apod_path = get_nasa_apod()
        if apod_path:
            set_wallpaper(apod_path)
        else:
            logging.error("Failed to set wallpaper.")
    else:
        logging.info(f"It's {run_count} script run today, no need to execute the download/setting functions.")
        
