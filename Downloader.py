import pytube.exceptions
from pytube import YouTube
from pathlib import Path
import os
import pyfiglet
from tabulate import tabulate

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
            choose = input("Choose an option: \n1. Download MP3\n2. Download MP4\n3. Analyze Video\n9. Help\n>> ")

            if choose == "1":
                print("Downloading....")

                try:
                    # Extracting the audio only
                    video = link.streams.filter(only_audio=True).first()

                    print("Extracting....")

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
                print("Downloading....")

                try:
                    # Extracting the video in highest resolution
                    video = link.streams.get_highest_resolution()

                    print("Extracting....")

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
                print(analyzeVideo(link))

            elif choose == "9":
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


def analyzeVideo(link):
    print("Fetching...")

    table = [
             ["Data", "Value"],
             ["Title", link.title],
             ["Length", link.length],
             ["Total Views", link.views],
             ["Rating", link.rating],
             ["Author", link.author],
             ["Publish Date", link.publish_date],
             ["Age Restricted", link.age_restricted],
             ["Available", link.check_availability()],
             ["Video ID", link.video_id],
             ["Channel ID", link.channel_id],
             ["Channel URL", link.channel_url],
             ["Thumbnail URL", link.thumbnail_url]
             ]
    print(divider)
    print(tabulate(table, headers="firstrow"))
    print(divider)

    advanced = input("Do you wanna see the description, caption and keywords?[y/n]\n")

    if advanced == "y":
        print(divider, "Description", divider)
        print(link.description)

        print(divider, "Captions", divider)
        print(link.captions)

        print(divider, "Keywords", divider)
        print(link.keywords)

    return "**********" + divider*2


if __name__ == '__main__':
    result = pyfiglet.figlet_format("YTDownloader By @Berkanktk", font="slant")
    print(result)

    downloader()
    anotherMedia()
