from pytube import YouTube

url = "https://youtu.be/6GaYbeHYLqA"
my_video = YouTube(url)

# resolving MacOS error: run the following in PyCharm terminal
# open /Applications/Python\ 3.7/Install\ Certificates.command

my_video = my_video.streams.get_highest_resolution()
print("done1")
my_video.download()
print("done2")
