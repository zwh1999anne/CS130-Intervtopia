
class instantOnlineService:
    def __init__(self, uid1, uid2): # TODO wait for user class done for information hiding (no longer pass inside uids)
        self.uid1 = uid1
        self.uid2 = uid2
        self.service_link = None
        self._setServiceLink()
        self._setupRoom()

    def _uniqueRoomIDCal(self):
        user_tuple=(self.uid1, self.uid2)
        return str(hex(hash(user_tuple)))[3:]

    def _setServiceLink(self):
        # NOTE implement in child class
        raise NotImplementedError("This needs to be implemented")

    def _setupRoom(self):
        self.roomLink = self.service_link+ self._uniqueRoomIDCal()

    def getRoom(self):
        return self.roomLink

if __name__ == '__main__':
    mr = instantOnlineService(123,456)
    lk = mr.getRoom()
    print(lk)
