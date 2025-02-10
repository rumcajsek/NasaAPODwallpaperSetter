from pathlib import Path
import os
import datetime
import requests
import logging
import json
import platform
if platform.system() == "Windows":
    import winreg
    import ctypes

# Configuration
NASA_API_KEY = "DEMO_KEY"  # Replace with your NASA API key
SAVE_FOLDER_PATH = os.path.join(Path(__file__).parent, "NASA_APOD")
JSON_STATE_FILE = os.path.join(SAVE_FOLDER_PATH,"state.json")
APOD_URL = f"https://api.nasa.gov/planetary/apod"
DATE_TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
STYLE_MAP = {
        "fill": (10, 0),
        "fit": (6, 0),
        "stretch": (2, 0),
        "tile": (0, 1),
        "center": (0, 0),
        "span": (22, 0),
    }
# Ensure the folder exists
os.makedirs(SAVE_FOLDER_PATH, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(SAVE_FOLDER_PATH,"apod_logs.log"),
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

def get_and_increment_run_count():
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

def get_and_decrement_run_count():
    """
    Resets the run count if error ocurred, so there is no need to change state.json manually after e.g. network error
    """

    state = load_state()

    if state["date"] == DATE_TODAY:
        state["count"] -= 1
    else:
        state["date"] = DATE_TODAY
        state["count"] = 0
    
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
        get_and_decrement_run_count()
        return None

def set_wallpaper(image_path, style="fill"):
    """
    Sets the provided image as the desktop wallpaper.
    """
    system = platform.system()
    if style not in STYLE_MAP:
        logging.error(f"Invalid style '{style}' provided.")
        get_and_decrement_run_count()
        return None
    
    if system == "Windows":
        wp_style, wp_tile = STYLE_MAP[style]
        try:
            if os.path.exists(image_path):
                reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(reg_key, "WallpaperStyle", 0, winreg.REG_SZ, str(wp_style))
                winreg.SetValueEx(reg_key, "TileWallpaper", 0, winreg.REG_SZ, str(wp_tile))
                winreg.CloseKey(reg_key)

                ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
                logging.info(f"Wallpaper set to: {image_path}, Wallpaper style: {style}")
            else:
                logging.error(f"Wallpaper file not found: {image_path}")
        except Exception as e:
            logging.error(f"Error setting registry values for wallpaper: {str(e)}")
            get_and_decrement_run_count()
            return None
    elif system == "Darwin": # MacOS, not tested!
        os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{image_path}\"'")
    elif system == "Linux": 
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
    else:
        logging.error("Unsupported OS for wallpaper setting.")
        return None

if __name__ == "__main__":
    run_count = get_and_increment_run_count()

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
        
