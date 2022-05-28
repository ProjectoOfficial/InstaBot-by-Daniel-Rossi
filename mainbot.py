# Dott. Daniel Rossi © 2021
# https://youtube.com/c/ProjectoOfficial
# seguici anche su Instagram come @OfficialProjecto e Facebook come @MiniProjectsOfficial

from instabot import bot
from selenium import webdriver
from instabot.utils import init
import os

'''
Please consider that the bot may not work because it could be necessary to update xpaths
'''

TEST = False

if __name__ == '__main__':
    if TEST:
        pass
    else:
        path, (username, password) = init(reset=False)

        # start must be >=1
        stop = 300
        start = 3

        bot = bot.InstaBot(username, password)
        mode = 5
        # MODE
        # 1) likes first picture of profile's followers sequentially
        # 2) likes first picture of profile's followers randomly
        # 3) likes pictures found by a tag
        # 4) prints all your followers
        # 5) prints people who don't follow you back

        print(bot.get_banner())

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        if os.path.exists("chromedriver.exe"):
            driver = webdriver.Chrome("chromedriver.exe", options=option)
            print("Your current Chromedriver version is: {}".format(driver.capabilities['chrome']['chromedriverVersion'].split(" ")[0]))
        else:
            driver = webdriver.Chrome(options=option)
            print("You do NOT have chromedriver.exe in the current folder")
            print("You must download the correct Chromedriver.exe version from https://chromedriver.chromium.org/downloads")
            print("then add it to the current folder: {} \n".format(os.getcwd()))

        print("Your current browser version is: {} \n".format(driver.capabilities['browserVersion']))

        if mode == 1:
            profile = input("insert profile: ")
            bot.work_sequentially(profile, stop, start)
        elif mode == 2:
            profile = input("insert profile: ")
            bot.work_randomly(profile, stop, start)
        elif mode == 3:
            tag = input("insert tag: ")
            bot.like_on_a_tag(tag, stop)
        elif mode == 4:
            bot.update_followers()
        elif mode == 5:
            bot.i_am_not_a_fan_of_anyone(updatefollowers=True, updatefollowing=True, verbose=True)

