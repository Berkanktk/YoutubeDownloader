# YoutubeDownloader
A simple command line program for downloading MP3 and MP4 files from YouTube .

## Usage
Run the code, enter the link, select the format and done!

> Downloads can be found under 'Downloads' folder on your computer.

## Scraping audio
The following code is needed in order to get your downloads in MP3 format. This is due to the pytube package that is being used, which only saves the downloaded files in MP4 format. So, the only thing this does is renaming the newly downloaded file into a '.mp3' format.
```python
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
```
