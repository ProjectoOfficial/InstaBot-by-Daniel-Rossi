# Daniel Rossi © 2021
# https://youtube.com/c/ProjectoOfficial

from selenium import webdriver
from time import sleep
from random import randrange
import pickle
import os


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.totlikes = 0

        self.driver.get("https://instagram.com")
        sleep(2)

        if os.path.exists("cookies.pkl"):
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)

        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(4)

        if not os.path.exists("cookies.pkl"):
            code = input("insert code")
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input').send_keys(code)
            sleep(1)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button').click()
            sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
            sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)

        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def work_randomly(self, profile, stop=100, start=0):
        n = start
        number_list = []
        multiplier = 2.8
        while True:

            # barra di ricerca
            self.driver.get("https://instagram.com/{}".format(profile))
            sleep(randrange(3, 12))

            # entra nei follower
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            sleep(randrange(3, 12))

            last_ht, ht = 0, 1
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

            # entra nel profilo di un follower random
            number_list.append(0)
            while True:
                rand_number = 0
                while rand_number in number_list:
                    rand_number = randrange(start, stop * multiplier, 1)  # start,stop,step
                if rand_number not in number_list:
                    number_list.append(rand_number)
                    break

            print("user to find: {}".format(rand_number))
            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(
                            rand_number)).click()
                    print("Found!")
                    break
                except Exception:
                    try:
                        self.driver.find_element_by_xpath(
                            '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a'.format(
                                rand_number)).click()
                        break
                    except Exception:
                        try:
                            sleep(randrange(2, 4))
                            ht = self.driver.execute_script("""
                                            arguments[0].scrollTo({},{});
                                            return arguments[0].scrollHeight""".format(ht, ht + 0.1), scroll_box)
                        except Exception:
                            break

            sleep(randrange(5, 12))

            try:
                # prende la prima foto
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                print("getting the picture")
            except Exception:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a').click()
                    print("getting the picture")
                except Exception:
                    pass

            sleep(randrange(3, 12))

            # mette like
            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                print("pushing like")
                self.totlikes += 1
                print("total likes done until now: {}".format(self.totlikes))
            except Exception:
                pass
            sleep(randrange(3, 12))

            n += 1

            if n == stop:
                print("process finished")
                print("total number of likes done: {}".format(self.totlikes))
                print("Last user number: {}".format(n))
                break

    def work_sequentially(self, profile, stop=100, start=0):
        n = start

        while True:
            # barra di ricerca
            self.driver.get("https://instagram.com/{}".format(profile))
            sleep(randrange(3, 12))

            # entra nei follower
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            sleep(randrange(3, 12))

            ht = 0
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            # entra nel profilo di un follower random

            print("user to find: {}".format(n))
            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(
                            n)).click()
                    print("Found!")
                    break
                except Exception:
                    try:
                        self.driver.find_element_by_xpath(
                            '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a'.format(
                                n)).click()
                        break
                    except Exception:
                        try:
                            sleep(randrange(2, 4))
                            ht = self.driver.execute_script("""
                                        arguments[0].scrollTo({},{});
                                        return arguments[0].scrollHeight""".format(ht, ht + 0.1), scroll_box)
                        except Exception:
                            break

            sleep(randrange(5, 12))

            try:
                # prende la prima foto
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                print("getting the picture")
            except Exception:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a').click()
                    print("getting the picture")
                except Exception:
                    pass
            sleep(randrange(3, 12))

            # mette like
            try:

                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                print("pushing like")
                self.totlikes += 1
                print("total likes done until now: {}".format(self.totlikes))
            except Exception:
                pass
            sleep(randrange(3, 12))

            n += 1

            sleep(randrange(3, 11))

            if n == stop:
                print("process finished")
                print("total number of likes done: {}".format(self.totlikes))
                print("Last user number: {}".format(n))
                break

    def like_on_a_tag(self, tag, stop=100):
        n = 1
        y = 1
        x = 1
        likes = 0
        scroll = 10
        while True:

            # barra di ricerca
            self.driver.get("https://instagram.com/explore/tags/{}".format(tag))
            sleep(2)

            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a'.format(y, x)).click()
                    x += 1
                    if x == 4:
                        x = 1
                        y += 1

                    sleep(1)
                    break
                except Exception:
                    try:
                        self.driver.execute_script("""window.scrollTo({},{})""".format(scroll, scroll+10))
                        sleep(0.5)
                        scroll += 10
                    except Exception:
                        break

            sleep(2)

            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                likes += 1
            except Exception:
                continue
            sleep(2)
            n += 1

            if n > stop:
                print("likes done: {}".format(likes))
                print("process finished")
                break

    def __get_followers(self,):
        # barra di ricerca
        self.driver.get("https://instagram.com/{}".format(self.username))
        sleep(2)

        # entra nei follower
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(5)

        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        sleep(1)
        if os.path.exists("followers.txt"):
            os.remove("followers.txt")

        f = open("followers.txt", "a")

        n_max = int(self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)
        print(n_max)

        n = 1

        while True:
            try:
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a'.format(n)).text
                print(user)
                f.write(user+"\n")
                sleep(0.5)
            except Exception:
                try:
                    ht = self.driver.execute_script("""arguments[0].scrollTo({},{});
                                return arguments[0].scrollHeight""".format(ht, ht + 0.1), scroll_box)
                    sleep(1.5)
                    n += 1
                except Exception:
                    break
            if n > n_max:
                break

        f.close()
        print("done! got followers")

    def update_followers(self):
        self.__get_followers()

        with open("followers.txt", "r") as f:
            for line in f:
                print(line)
