from pytube import YouTube
import ffmpeg
import os


def download_yt(yt_url, res="2160p"):
    yt = YouTube(yt_url)
    # print(yt.thumbnail_url)
    file_name = yt.title
    video_str = yt.streams.filter(adaptive=True, res="2160p")[0]
    print(f"Video stream: {video_str}")
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
