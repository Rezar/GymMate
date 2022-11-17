
import os
from csv import reader

from youtube_dowloader import YoutubeDownloader

download_folder = "youtube_videos\\"

if __name__ == '__main__':

    exercice_names = []
    with open('exercises.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            exercice_name = row[0]
            exercice_names.append(exercice_name)
            directory_path = download_folder + "\\" + exercice_name
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)
    num = 1
    thread_list = []
    for exercice_name in exercice_names[0:10]:
        thread = YoutubeDownloader("Thread-" + str(num), exercice_name)
        thread_list.append(thread)
        thread.start()
        num += 1
    for thread in thread_list:
        thread.join()
