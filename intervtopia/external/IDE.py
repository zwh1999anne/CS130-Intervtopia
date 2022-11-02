from external.instantOnlineService import instantOnlineService

class IDE(instantOnlineService):
    def __init__(self, uid1, uid2): # TODO wait for user class done for information hiding (no longer pass inside uids)
        super().__init__(uid1, uid2)

    def _setServiceLink(self):
        self.service_link = "https://codeshare.io/"

if __name__ == '__main__':
    mr = IDE(123,456)
    lk = mr.getRoom()
    print(lk)
