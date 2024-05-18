from pytube import YouTube
import ffmpeg
import os
from slugify import slugify


def download_yt(yt_url, res="2160p"):
    yt = YouTube(yt_url)
    # print(yt.thumbnail_url)
    file_name = yt.title
    file_name = slugify(file_name, allow_unicode=True)
    # print(yt.streams.filter(adaptive=True).order_by('resolution').desc())
    video_str = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()
    print(f"Video stream: {video_str}")
    # try:
    #     video_str = yt.streams.filter(adaptive=True, res="2160p")[0]
    # except IndexError:
    #     print("2160p stream not found, try 1080p instead.")
    #     video_str = yt.streams.filter(adaptive=True, res="1080p")[0]
    # print(f"Video stream: {video_str}")
    audio_str = yt.streams.filter(adaptive=True, only_audio=True)[-1]
    print(f"Audio stream: {audio_str}")
    yt.streams.get_by_itag(video_str.itag).download(filename="video.mp4")
    yt.streams.get_by_itag(audio_str.itag).download(filename="audio.mp4")
    vid = ffmpeg.input("video.mp4")
    aud = ffmpeg.input("audio.mp4")
    ffmpeg.concat(vid, aud, v=1, a=1).output(f'{file_name}.mp4').run()
    os.remove("video.mp4")
    os.remove("audio.mp4")


def main():
    yt_url = input("Enter the YouTube video URL: ")
    download_yt(yt_url)


if __name__ == '__main__':
    main()
