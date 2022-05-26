# Dott. Daniel Rossi © 2021
# https://youtube.com/c/ProjectoOfficial
# seguici anche su Instagram come @OfficialProjecto e Facebook come @MiniProjectsOfficial

from selenium import webdriver
from time import sleep
from random import randrange
import pickle
import os


class InstaBot:
    def __init__(self, username, password):
        self.driver = None
        self.username = username
        self.totlikes = 0

        self.username = username
        self.password = password

        self._followers_PATH = "followers.txt"
        self._following_PATH = "following.txt"
        self._people_to_unfollow_PATH = "to_unfollow.txt"

    def _login(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get("https://instagram.com")
        sleep(2)

        if os.path.exists("cookies.pkl"):
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)

        # cookies button
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/button[1]').click()

        sleep(1)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        # access button
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(4)

        if not os.path.exists("cookies.pkl"):
            code = input("insert code")

            # insert 2FA code
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input').send_keys(code)
            sleep(1)

            # click code confirmation button
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button').click()
            sleep(5)

            # save login info --> not now
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/section/main/div/div/div/div/button').click()
            sleep(5)
        #self.driver.find_element_by_xpath(
            #'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        #sleep(2)

        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def get_banner(self):
        return """ 
            ██╗███╗   ██╗███████╗████████╗ █████╗ ██████╗  ██████╗ ████████╗                                          
            ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝                                          
            ██║██╔██╗ ██║███████╗   ██║   ███████║██████╔╝██║   ██║   ██║                                             
            ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║                                             
            ██║██║ ╚████║███████║   ██║   ██║  ██║██████╔╝╚██████╔╝   ██║                                             
            ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝                                             
                                                                                                                      
            ██████╗ ██╗   ██╗    ██████╗  █████╗ ███╗   ██╗██╗███████╗██╗         ██████╗  ██████╗ ███████╗███████╗██╗
            ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗████╗  ██║██║██╔════╝██║         ██╔══██╗██╔═══██╗██╔════╝██╔════╝██║
            ██████╔╝ ╚████╔╝     ██║  ██║███████║██╔██╗ ██║██║█████╗  ██║         ██████╔╝██║   ██║███████╗███████╗██║
            ██╔══██╗  ╚██╔╝      ██║  ██║██╔══██║██║╚██╗██║██║██╔══╝  ██║         ██╔══██╗██║   ██║╚════██║╚════██║██║
            ██████╔╝   ██║       ██████╔╝██║  ██║██║ ╚████║██║███████╗███████╗    ██║  ██║╚██████╔╝███████║███████║██║
            ╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝                                                                                                                                            
            """

    def work_randomly(self, profile, stop=100, start=0):
        self._login()

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
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")

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
        self._login()

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
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            # entra nel profilo di un follower random

            print("user to find: {}".format(n))
            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div/div/a'.format(
                            n)).click()
                    print("Found!")
                    break
                except Exception:
                    try:
                        self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(
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
                        '/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a').click()
                    print("getting the picture")
                except Exception:
                    pass
            sleep(randrange(3, 12))

            # mette like
            try:

                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
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
        self._login()

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
        self._login()

        # gets to the user profile
        self.driver.get("https://instagram.com/{}".format(self.username))
        sleep(2)

        # clicks on followers
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a').click()
        sleep(5)

        # gets the scrollbar
        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
        sleep(1)
        if os.path.exists(self._followers_PATH):
            os.remove(self._followers_PATH)

        f = open(self._followers_PATH, "a")

        if f == None:
            print("couldn't create or open {}".format(self._following_PATH))

        # get the total number of followers
        n_max = int(self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/div/span').text)

        print(n_max)
        n = 1

        while True:
            user = None

            try:
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a/span'.format(n)).text
            except Exception:
                pass

            try:
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a/span'.format(n)).text
            except Exception:
                pass

            if user == None:
                try:
                    print("********* SCROLLING **********")
                    ht = self.driver.execute_script("""arguments[0].scrollTo({},{});
                                return arguments[0].scrollHeight""".format(ht, ht + 0.1), scroll_box)
                    sleep(1.5)
                    continue
                except Exception:
                    print("cannot scroll")
                    break

            print("{} - {}".format(n, user))
            f.write(user+"\n")
            sleep(0.1)
            n += 1

            if n > n_max:
                break

        f.close()
        print("done! got followers")


    def __get_following(self,):
        self._login()

        # gets to the profile page
        self.driver.get("https://instagram.com/{}".format(self.username))
        sleep(2)

        # clicks on the following link
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[3]/a').click()
        sleep(5)

        # gets the scrollbar
        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]")
        sleep(1)
        if os.path.exists(self._following_PATH):
            os.remove(self._following_PATH)

        f = open(self._following_PATH, "a")

        if f == None:
            print("couldn't create or open {}".format(self._following_PATH))

        # gets the number of following
        n_max = int(self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[3]/a/div/span').text)
        print(n_max)
        n = 1
        while True:
            user = None

            try:
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a/span'.format(n)).text
            except Exception:
                pass

            try:
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a/span'.format(n)).text
            except Exception:
                pass

            if user == None:
                try:
                    print("********* SCROLLING **********")
                    ht = self.driver.execute_script("""arguments[0].scrollTo({},{});
                                return arguments[0].scrollHeight""".format(ht, ht + 0.1), scroll_box)
                    sleep(1.5)
                    continue
                except Exception:
                    print("cannot scroll")
                    break

            print("{} - {}".format(n, user))
            f.write(user + "\n")
            sleep(0.1)
            n += 1

            if n > n_max:
                break

        f.close()
        print("done! got following")

    def update_followers(self):
        self.__get_followers()

        with open(self._followers_PATH, "r") as f:
            for line in f:
                print(line)

    def i_am_not_a_fan_of_anyone(self, updatefollowers:bool=True, updatefollowing:bool=True):
        if updatefollowers:
            self.__get_followers()
        if updatefollowing:
            self.__get_following()

        try:
            assert os.path.exists(self._followers_PATH)
            assert os.path.exists(self._following_PATH)
        except AssertionError:
            print("{} or {} or both files do not exist".format(self._followers_PATH, self._following_PATH))

        followers = []
        followings = []

        with open(self._followers_PATH) as f:
            followers = [line.strip() for line in f]

        with open(self._following_PATH) as f:
            followings = [line.strip() for line in f]

        if os.path.exists(self._people_to_unfollow_PATH):
            os.remove(self._people_to_unfollow_PATH)

        print("people who are not following you:")
        with open(self._people_to_unfollow_PATH, "a") as f:
            for following in followings:
                if not following in followers:
                    print(following)
                    f.write(following)



