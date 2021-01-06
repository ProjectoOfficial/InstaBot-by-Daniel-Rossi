from instagram_private_api import Client, ClientCompatPatch, ClientLoginError, ClientError


class Bot:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__api = None

        try:
            self.__api = Client(auto_patch=True, authenticate=True, username=self.__username, password=self.__password)
            print("login effettuato con successo!\n")
        except ClientLoginError:
            print("La password che hai inserito non è corretta\n")
            return
        except ClientError:
            print("Se hai l'autenticazione a due fattori attiva, il bot non può funzionare\n")
            print("Puoi disattivarla per usare il bot, e al termine riattivarla\n")
            return

        user_feed_info =  self.__api.user_feed('329452045', count=10)
        for post in user_feed_info:
            print('%s from %s' % (post['link'], post['user']['username']))
