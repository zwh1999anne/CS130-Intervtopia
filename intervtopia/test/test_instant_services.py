import unittest
from external.meeting import meetingRoom
from external.IDE import IDE


class randomTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # TODO wait for user class done for information hiding (no longer pass inside uids)
        cls.meeting_room = meetingRoom(123, 456)
        cls.ide = IDE(123, 456)

    @classmethod
    def tearDownClass(cls):
        del cls.meeting_room
        del cls.ide

    def test_link_correctness(self):
        # TODO try to find a way of calling the same unique function, so no need to check with a hard-coded res
        self.assertEqual(self.meeting_room.getRoom(), 'https://meet.jit.si/3361307c5b48ef4f')
        self.assertEqual(self.ide.getRoom(), 'https://codeshare.io/3361307c5b48ef4f')
