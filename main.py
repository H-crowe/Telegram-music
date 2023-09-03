# This Telegram bot is designed to help users discover and share new music from YouTube To a Telegram channel.
# - Searches for new music on YouTube.
# - Provides an easy and efficient way to share music with Telegram channel.
# - Prevents duplicate music posts to keep the channel content fresh.

# Author: H-crowe
# Repository: https://github.com/H-crowe/Telegram-music


from telethon.sync import TelegramClient
import time
from youtubesearchpython import VideosSearch
from pyfiglet import Figlet
from termcolor import colored

custom_banner = Figlet(font='slant')
banner_text = custom_banner.renderText('H-Crowe')

colored_banner = colored(banner_text, 'red', attrs=['bold'])
Bot_name = "Telegram-music"
print(colored_banner)
print(colored(f"Bot is running : {Bot_name}\n", 'green', attrs=['bold']))

# Your API credentials (api_id and api_hash)
api_id = 'api_id'
api_hash = 'api_hash'
# Your bot's API token
bot_token = 'API token'
# Name of the channel you want to send music to (with the '@' symbol)
channel_username = '@channel-Name'

# Initialize the Telegram client
client = TelegramClient('bot_session', api_id, api_hash)

# Connect to Telegram
client.start(bot_token=bot_token)

def search_youtube_for_music(query, limit=2):
    videos_search = VideosSearch(query, limit=limit)
    return videos_search.result().get('result', [])

def send_music_to_channel(video_title, video_url):
    try:
        # Send the video URL to the channel
        client.send_message(entity=channel_username, message=f"New Music: {video_title}\n{video_url}")
        print(f"Music sent successfully: {video_title}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        # Search for new music on YouTube (replace 'QUERY' with your search query)
        search_query = 'trending music'

        try:
            # search results with a limit of 2
            results = search_youtube_for_music(search_query, limit=2)

            # Iterate through the search results and send each video to the channel
            for video in results:
                video_title = video.get('title', '')
                video_url = video.get('link', '')
                # Check if the music title has already been sent
                if video_title and video_url:
                    send_music_to_channel(video_title, video_url)

            # Wait for an interval before checking for new music again
            time.sleep(3600)  # Wait for 1 hour (adjust as needed)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
