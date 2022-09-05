from pytube import *
from moviepy.editor import VideoFileClip
import os, re

# Sets the file path to download the audio files to
def setDownloadDir():
    download_dir = ""
    audio_type = input("Please enter the genre that best describes the type of audio in your playlist (Hip-Hop, Pop, Country, Lofi, Audiobook, Other): ")
    
    if audio_type == "Hip-hop" or audio_type == "hip-hop":
        download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\music\\hip-hop"
    elif audio_type == "Pop" or audio_type == "pop":
         download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\music\\pop"
    elif audio_type == "Country" or audio_type == "country":
        download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\music\\country"
    elif audio_type == "Lofi" or audio_type == "lofi" or audio_type == "LoFi":
        download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\music\\lofi"
    elif audio_type == "Audiobook" or audio_type == "audiobook":
        download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\audiobooks"
    elif audio_type == "Other" or audio_type == "other":
        download_dir = "C:\\Users\\cjqga\\Desktop\\projects\\YouTube Audio Downloader\\media\\music\\other"
    else:
        print("Genre not valid. Please try again.")
        setDownloadDir()
    
    return download_dir

# Prints the length of the playlist
def num_playlist(playlist):
    if len(playlist) == 0:
        print("This playlist is empty.")
    elif len(playlist) == 1:
        print("This playlist contains 1 URL: ")
    else:
        print("This playlist contains {num_urls} URLs: ".format(num_urls = len(playlist.video_urls)))

# prints the title of each video in the playlist
def print_playlist(playlist):
    count = 1
    for video in playlist.videos:
        print(str(count) + ". " + video.title)
        count += 1

# Converts mp4 file to mp3 file and downloads the mp3 file
def download_files(playlist, download_dir):
    print("Please wait while we convert your files. This may take a while depending on the size of your playlist.")
    
    for url in playlist.video_urls:
        mp4 = YouTube(url).streams.get_highest_resolution().download(output_path=download_dir)
        mp3 = mp4.split(".mp4", 1)[0] + ".mp3"
        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio

        audio_clip.write_audiofile(mp3)
        audio_clip.close()
        video_clip.close()
        os.remove(mp4)

# MAIN PROGRAM
def runProgram():
    print("\n---------------YOUTUBE AUDIO DOWNLOADER---------------\n")
    download_dir = setDownloadDir()
    playlist_url = input("Enter a YouTube Playlist URL: ")
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    num_playlist(playlist)
    print_playlist(playlist)
    download_files(playlist, download_dir)

runProgram()