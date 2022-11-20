from urllib.request import Request, urlopen
import json
import random


class interviewQuestion():

    def __init__(self):
        self._q_title = None
        self._q_difficulty = None
        self._q_url = None
        self._q_front_end_id = None

    def setTitle(self, title):
        self._q_title = title

    def setDifficulty(self, difficulty):
        if isinstance(difficulty, int):
            if difficulty == 1:
                self._q_difficulty = 'E'
            elif difficulty == 2:
                self._q_difficulty = 'M'
            elif difficulty == 3:
                self._q_difficulty = 'H'
        elif isinstance(difficulty, str):
            self._q_difficulty = difficulty

    def setURL(self, url):
        self._q_url = url

    def setFrontendID(self, id):
        self._q_front_end_id = id

    def getTitle(self):
        return self._q_title

    def getDifficulty(self):
        return self._q_difficulty

    def getURL(self):
        return self._q_url

    def getFrontendID(self):
        return self._q_front_end_id


class leetCodeQuestionQuery():

    def __init__(self):
        self._meta_link = "https://leetcode.com/api/problems/algorithms/"
        self._question_link_prefix = "https://leetcode.com/problems/"
        self._free_q_metas = []
        self._free_q_easy = []
        self._free_q_medi = []
        self._free_q_hard = []
        self._updateMeta()
        self._filterQuestions()
        self._sortQuestions()

    def _updateMeta(self):
        req = Request(url=self._meta_link, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as url:
            self._meta = json.load(url)

    def _filterQuestions(self):
        q_status_list = self._meta["stat_status_pairs"]
        for q in q_status_list:
            if q["paid_only"] == False:
                self._free_q_metas.append(q)

    def _sortQuestions(self):
        # sort questions based on difficulty then id
        for q_meta in self._free_q_metas:
            q_title = q_meta["stat"]["question__title"]
            q_title_slug = q_meta["stat"]["question__title_slug"]
            q_difficulty = q_meta["difficulty"]["level"]
            frontend_q_id = q_meta["stat"]["frontend_question_id"]
            q_url = self._question_link_prefix + q_title_slug
            # wrap question class
            q_wrapper = interviewQuestion()
            q_wrapper.setTitle(q_title)
            q_wrapper.setDifficulty(q_difficulty)
            q_wrapper.setURL(q_url)
            q_wrapper.setFrontendID(frontend_q_id)
            # push into containers
            if q_difficulty == 1:
                self._free_q_easy.append(q_wrapper)
            elif q_difficulty == 2:
                self._free_q_medi.append(q_wrapper)
            elif q_difficulty == 3:
                self._free_q_hard.append(q_wrapper)
            # sort for each difficulty
            self._free_q_easy = sorted(self._free_q_easy, key=lambda x: x.getFrontendID())
            self._free_q_medi = sorted(self._free_q_medi, key=lambda x: x.getFrontendID())
            self._free_q_hard = sorted(self._free_q_hard, key=lambda x: x.getFrontendID())

    def length(self, difficulty):
        if difficulty == 'E' or difficulty == 1:
            L = len(self._free_q_easy)
        elif difficulty == 'M' or difficulty == 2:
            L = len(self._free_q_medi)
        elif difficulty == 'H' or difficulty == 3:
            L = len(self._free_q_hard)

        return L

    def getQuestion(self, i: int, difficulty: str):
        if difficulty == 'E' or difficulty == 1:
            return self._free_q_easy[i]
        elif difficulty == 'M' or difficulty == 2:
            return self._free_q_medi[i]
        elif difficulty == 'H' or difficulty == 3:
            return self._free_q_hard[i]

    def getRandomQuestion(self, difficulty):
        rand_q_id = random.randrange(self.length(difficulty))
        return self.getQuestion(rand_q_id, difficulty)


if __name__ == '__main__':
    query = leetCodeQuestionQuery()
    for difficulty in range(1, 4):
        q = query.getRandomQuestion(difficulty)
        print(q.getDifficulty())
        print(q.getTitle())
        print(q.getURL())
