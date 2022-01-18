import pytube.exceptions
from pytube import YouTube
from pathlib import Path
import os

'''
    Author: Berkan Kütük
    Username: Berkanktk
'''

divider = "*******************************************"


def downloader():
    flag = True

    # Standard download folder
    destination = str(os.path.join(Path.home(), "Downloads"))

    while flag:
        try:
            # Url input from the user
            link = YouTube(input("Enter the URL: \n>> "))

            # Choose download format
            choose = input("Which format do you prefer?: \n1. MP3\n2. MP4\n3. Help\n>> ")

            if choose == "1":
                print("Extracting....")

                try:
                    # Extracting the audio only
                    video = link.streams.filter(only_audio=True).first()

                    print("Downloading....")

                    # Downloading the file
                    out_file = video.download(output_path=destination)

                    print("Saving....")

                    # Saving the file
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)

                    # Result of success
                    print("'" + link.title + "'" + " has been successfully downloaded.\n" + divider)

                except FileExistsError:
                    print("Download failed. File already exists.\n" + divider)
                except pytube.exceptions.VideoUnavailable:
                    print("Download failed. The video is unavailable.\n" + divider)
                finally:
                    anotherMedia()

            elif choose == "2":
                print("Extracting....")

                try:
                    # Extracting the video in highest resolution
                    video = link.streams.get_highest_resolution()

                    print("Downloading....")

                    # Downloading the video
                    video.download(destination)

                    print("Saving....")

                    # Result of success
                    print("'" + link.title + "'" + " has been successfully downloaded.\n" + divider)

                except pytube.exceptions.VideoUnavailable:
                    print("Download failed. The video is unavailable.")
                finally:
                    anotherMedia()

            elif choose == "3":
                print(divider)
                print("MP3 = Music\nMP4 = Video\n\nThe downloaded files can be found under the 'Downloads' folder.")
                print(divider)
            else:
                print("Invalid option.\n" + divider)
        except pytube.exceptions.RegexMatchError:
            print("The URL is invalid.\n" + divider)


def anotherMedia():
    another_media = input("Do you wanna download another media?[y/n]\n")

    if another_media == "y":
        downloader()
    elif another_media == "n":
        raise SystemExit


if __name__ == '__main__':
    downloader()
    anotherMedia()
