import yt_dlp
import pyfiglet
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def display_banner():
    terminal_width = os.get_terminal_size().columns
    font = "big"

    banner = pyfiglet.figlet_format("YouTube Downloader", font=font, width=terminal_width)
    banner_lines = banner.splitlines()
    centered_banner = "\n".join(line.center(terminal_width) for line in banner_lines)

    print(Fore.LIGHTBLUE_EX + Back.BLACK + centered_banner)
    print(Fore.LIGHTGREEN_EX + "Developed by Dev Elijah".center(terminal_width))
    print(Fore.YELLOW + "Download videos, audios, thumbnails, and playlists effortlessly.".center(terminal_width))
    print(Fore.RED + "=" * terminal_width)

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(Fore.GREEN + f"\nFolder '{folder_name}' created successfully!")
    else:
        print(Fore.GREEN + f"\nUsing existing folder: '{folder_name}'")

def validate_url(url):
    """Validate the provided YouTube URL."""
    if url.startswith("http") and ("youtube.com" in url or "youtu.be" in url):
        return True
    print(Fore.RED + "\nInvalid YouTube URL. Please try again.")
    return False

def download_youtube_content(url, folder_name='Youtube downloads', content_type='video', quality='best'):
    create_folder(folder_name)
    url = yt_dlp.utils.sanitize_url(url.strip())

    ydl_opts = {}
    if content_type == 'audio':
        ydl_opts = {
            'format': f'bestaudio[ext=m4a]/{quality}',
            'outtmpl': f'{folder_name}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': False,
        }
    elif content_type == 'video':
        ydl_opts = {
            'format': f'{quality}[ext=mp4]',
            'outtmpl': f'{folder_name}/%(title)s.%(ext)s',
            'noplaylist': False,
        }
    elif content_type == 'playlist':
        ydl_opts = {
            'format': f'{quality}[ext=mp4]',
            'outtmpl': f'{folder_name}/%(playlist)s/%(title)s.%(ext)s',
            'noplaylist': False,
        }
    elif content_type == 'image':
        ydl_opts = {
            'writethumbnail': True,
            'skip_download': True,
            'outtmpl': f'{folder_name}/%(title)s.%(ext)s',
            'noplaylist': True,
        }
    else:
        print(Fore.RED + "\nInvalid content type selected.")
        return

    try:
        print(Fore.YELLOW + f"\nStarting download for URL: {url}\n")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(Fore.GREEN + "\nDownload completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(Fore.RED + f"\nDownload error: {e}")
    except Exception as e:
        print(Fore.RED + f"\nAn unexpected error occurred: {e}")

if __name__ == '__main__':
    while True:
        display_banner()
        print(Fore.MAGENTA + "\nChoose an option:")
        print(Fore.CYAN + "\n1. Download Video")
        print(Fore.CYAN + "\n2. Download Audio")
        print(Fore.CYAN + "\n3. Download Thumbnail")
        print(Fore.CYAN + "\n4. Download Playlist")
        print(Fore.RED + "\n5. Exit")

        choice = input(Fore.LIGHTYELLOW_EX + "\nEnter your choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print(Fore.LIGHTRED_EX + "\nExiting... Goodbye!")
            break

        url = input(Fore.LIGHTBLUE_EX + "\nEnter the YouTube video/playlist URL: ").strip()
        if not validate_url(url):
            continue

        if choice in ['1', '2', '4']:
            print(Fore.LIGHTCYAN_EX + "\nChoose quality:")
            print(Fore.CYAN + "\n1. Best")
            print(Fore.CYAN + "\n2. Medium")
            print(Fore.CYAN + "\n3. Low")
            quality_choice = input(Fore.LIGHTYELLOW_EX + "\nEnter quality choice (1/2/3): ").strip()
            quality = {'1': 'best', '2': 'medium', '3': 'worst'}.get(quality_choice, 'best')
        else:
            quality = 'best'

        if choice == '1':
            download_youtube_content(url, content_type='video', quality=quality)
        elif choice == '2':
            download_youtube_content(url, content_type='audio', quality=quality)
        elif choice == '3':
            download_youtube_content(url, content_type='image')
        elif choice == '4':
            download_youtube_content(url, content_type='playlist', quality=quality)
        else:
            print(Fore.RED + "\nInvalid choice! Please try again.")

        retry = input(Fore.LIGHTCYAN_EX + "\nWould you like to download another file? (yes/no): ").strip().lower()
        if retry != 'yes':
            print(Fore.LIGHTRED_EX + "\nThanks for using YouTube Downloader! See you next time.")
            break
