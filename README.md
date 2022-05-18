# YoutubeDownloader
A simple command line program for downloading and analyzing videoes files from YouTube. 

Made for educational purposes only and not for commercial use.

## Usage
### With Executable
Download the executable and locate it on your terminal.

Then run `./Downloads.exe` enter the link, select the options and done!

> Downloads can be found under 'Downloads' folder on your computer.

### Cloned
Run the code, enter the link, select the format and done!

> Downloads can be found under 'Downloads' folder on your computer.

## Scraping audio
The following code is needed in order to get your downloads in MP3 format. This is due to the pytube package that is being used, which only saves the downloaded files in MP4 format. So, the only thing this does is renaming the newly downloaded file into a '.mp3' format.
```python
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
```
