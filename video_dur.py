#! /usr/bin/python

import os
import subprocess
from datetime import timedelta

video_extensions = ["mp4", "avi"]


def get_videos():
    videos = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split(".")[-1] in video_extensions:
                videos.append(os.path.join(root, file))
    return videos


def get_ffprobe_output(filename):
    filename = filename.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(
        filename
    )
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    stdout, stderr = p.communicate()
    return int(float(stdout))


def seconds_to_str(s):
    return str(timedelta(seconds=s))


def main():
    videos = get_videos()
    total_duration = 0

    for video in videos:
        duration = get_ffprobe_output(video)

        print(video.split("/")[-1], "Duration:", seconds_to_str(duration))
        total_duration += duration

    print("Total: ", seconds_to_str(total_duration))


if __name__ == "__main__":
    main()
