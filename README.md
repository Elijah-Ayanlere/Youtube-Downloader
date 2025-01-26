# YouTube Downloader

A versatile and user-friendly **YouTube Downloader** script developed in Python. With this tool, you can easily download YouTube videos, audios, thumbnails, and playlists in various qualities. The script provides a sleek terminal interface with vibrant colors for an engaging experience.

---

## Features

- **Download Videos**: Save YouTube videos in MP4 format with customizable quality (Best, Medium, or Low).
- **Download Audio**: Extract high-quality audio tracks and save them as MP3.
- **Download Thumbnails**: Fetch and download video thumbnails.
- **Download Playlists**: Download entire playlists seamlessly in your preferred quality.
- **User-Friendly Interface**: Engaging terminal interface with clear instructions and vibrant colors.

---

## Requirements

Make sure you have the following installed:

- Python 3.7 or higher
- Required Python packages:
  - `yt_dlp`
  - `pyfiglet`
  - `colorama`

You can install the required packages by running:
```bash
pip install yt-dlp pyfiglet colorama
```

## Usage

1. **Clone or download this repository** to your system.
2. **Open your terminal** and navigate to the directory containing the script.
3. **Run the script** with the following command:
   ```bash
   python3 youtube_downloader.py
   ```
# Follow the on-screen prompts to:
- Choose the type of content to download (Video, Audio, Thumbnail, or Playlist).
- Enter the YouTube URL.
- Select the desired quality (for Video and Playlist).

---

## Features Overview

### Download Videos
- Saves YouTube videos in **MP4 format**.
- Options for quality:
  - **Best**: Highest quality available.
  - **Medium**: Moderate quality.
  - **Low**: Lower quality to save storage space.

### Download Audio
- Extracts audio in **MP3 format**.
- Uses `yt_dlp`'s built-in **FFmpeg support** for audio processing.

### Download Thumbnails
- Downloads the **thumbnail image** of the provided YouTube video.
- Saves the image in the specified folder.

### Download Playlists
- Downloads all videos in a **YouTube playlist**.
- Saves each video in a structured folder for better organization.

---

## Script Highlights

- **Banner Display**: Displays a stylish **ASCII-art banner** using `pyfiglet`.
- **Colorful Output**: Uses `colorama` for vibrant, readable terminal output.
- **Error Handling**: Provides helpful error messages for invalid URLs or download failures.
- **Customizable Output Folder**: Saves downloaded content in a default folder (`Youtube downloads`) or a user-defined folder.

---

## Example Walkthrough

### Starting the Script
Run the following command:
```bash
python3 youtube_downloader.py
```
# Main Menu
You will be presented with the following options:

1: Download Video  
2: Download Audio  
3: Download Thumbnail  
4: Download Playlist  
5: Exit the program  

---

# Enter YouTube URL
Provide a valid YouTube video or playlist URL when prompted.

---

# Select Quality (if applicable)
- **Best**  
- **Medium**  
- **Low**  

---

# Download Progress
The script will display progress and save the downloaded content to the designated folder.

---

# Troubleshooting
- **Invalid URL**: Ensure the provided URL starts with `http` and contains `youtube.com` or `youtu.be`.  
- **Dependencies Missing**: Install missing dependencies using `pip install` as shown in the requirements section.  
- **Permission Errors**: Run the script with appropriate permissions or adjust folder write permissions.  

---

# Credits
- **Developed by**: Dev Elijah  
- **Powered by the following Python libraries**:  
  - `yt_dlp`  
  - `pyfiglet`  
  - `colorama`  

---

# License
This project is open-source and available under the **MIT License**.
