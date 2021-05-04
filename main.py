# Import modules
from pytube import YouTube
from pytube.cli import on_progress
import os


# This is the video class
class Video:
    # This initialize function will take the video name and url
    def __init__(self, name, url):
        self.name = name
        self.url = url

    # This function will print the name of video to check if that the video which user want to install
    def print_video(self):
        print("Video name: {} \n".format(self.name))

    # This function will download the video
    def downloading(self, url):
        self.url = url
        # We will store the video streams in this variable
        stream = url.streams

        # This loop will print the qualities for the video
        for i in stream:
            print("--------------------------------------------- Quality ---------------------------------------------")
            print(i)
            print("---------------------------------------------------------------------------------------------------")

        # This will take the itag for the stream that the user want
        wanted_stream = int(input("Put the iTag for the quality you want: "))

        # This will store the video with the quality user want
        install = url.streams.get_by_itag(wanted_stream)

        # This will store the path you want to store the video in
        path = input("Put the path you want to install the video in: ")

        # This will check if the path is exists or no
        exist = os.path.exists(path)

        # This will stop the program if the path is not exist
        if not exist:
            print("\nInvalid path")
            return False

        # This will try to install the video in the path the user choose
        try:
            # This will install the video in the path
            install.download(path)

            # This will print done if the video is installed
            print("Done!")

        # This will notify the user that the video isn't downloaded
        except:
            print("Sorry, The video didn't install you can try again later or check if the itag or path is wrong")


# This function will take the url from the user and run the video methods
def ready():
    # This will store the link of the video
    link = input("Put video URL: ")

    # This will find the video on the youtube and make a progress bar
    try:
        video = YouTube(link, on_progress_callback=on_progress)

    except:
        print("\nThis is not video URL")
        return False

    # This will store the title of the video
    title = video.title

    # This will run the print_video() method
    Video(title, video).print_video()

    # This will check if the video is that the user want or no
    is_vid = input("""
is this the video is the video you want to download [Y,n]
""")

    # This will run the downloading() method if this video is the right video
    if is_vid.upper() == "Y":
        Video(title, video).downloading(video)

    # This will repeat the function to take the right video
    elif is_vid.upper() == "N":
        ready()

    # This will exit the program if the user give an invalid input
    else:
        print("invalid input")


# This will run the script if the you try to run it from the main file
if __name__ == "__main__":
    # This will try to run the script
    try:
        ready()

    # This will handle the Keyboard Interruption errors
    except KeyboardInterrupt:
        print("\nGood Bye")

    except ValueError:
        print("\ninvalid input")
