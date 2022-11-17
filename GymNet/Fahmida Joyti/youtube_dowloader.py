import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from termcolor import colored
from helper import get_selenium_driver
import getpass
import subprocess
import shlex
from urllib.parse import urlparse
import os
from pathlib import Path
import time
import re
exitFlag = 0


class YoutubeDownloader(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_id = thread_id
        self.resolution = 1080
        self.download_folder = "youtube_shorts\\"

    def run(self) -> None:
        print("Starting downloading " + self.name)
        self.download_videos()
        print("Done!!!" + self.name)

    def download_videos(self):
        download_urls = self.scrape_videos(self.name)
        print(download_urls)
        for url in download_urls:
            prefix = "youtube-dl -i -c --rm-cache-dir "
            url_suffix = urlparse(url).path.split('/')[-1]
            output_folder = self.download_folder + self.name + "\\"
            output = f"-o  '{output_folder}" + "%(title)s.%(ext)s'" + " "
            video_sound = f" -f 'bestvideo[height<={self.resolution}]+ bestaudio/best[height<={self.resolution}]'" + " "
            cmd = prefix + output + url_suffix + video_sound
            print(cmd)
            self.execute_terminal_command(cmd)

    def scrape_videos(self, name):
        driver = get_selenium_driver()
        urls = []
        if driver is not None:
            name = name.replace(" ", "+")
            driver.get(f"https://www.youtube.com/results?search_query={name}")
            wait = WebDriverWait(driver, 60)
            visible = EC.visibility_of_element_located
            wait.until(visible((By.ID, "video-title")))
            results_cont = driver.find_element(By.ID, "contents")
            results_elements = results_cont.find_elements(By.CSS_SELECTOR, "*")
            num = 0
            while True:
                for video in results_elements:
                    if str(video.get_attribute('id')).strip() == 'video-title':
                        title = str(video.get_attribute('title'))
                        url = video.get_attribute('href')
                        if not video.get_attribute('aria-label'):
                            continue
                        label = str(video.get_attribute('aria-label'))
                        no_title = label.replace(title, '')
                        if 'Short' in no_title:
                            continue
                        words = no_title.split()
                        views = words[-2]
                        duration_string = no_title[no_title.find('ago') + len('ago'): no_title.find(views)].strip()
                        regex = r"(\d+) (\w+)"
                        match = re.findall(regex, duration_string)
                        if match:
                            first_match = match[0]
                            value = first_match[0]
                            unit = first_match[1]
                            if 'hour' in unit:
                                continue
                            if 'minute' in unit and int(value) > 10:
                                continue
                        if url is not None:
                            urls.append(str(url))
                        num += 1
                    if num > 5:
                        break
                break
        return urls

    def execute_terminal_command(self, cmd):
        process = subprocess.Popen(shlex.split(cmd), shell=True)
        output, error = process.communicate()
        if process.returncode != 0:
            print(colored('Error running cmd!', 'red'))
            return
        else:
            return output