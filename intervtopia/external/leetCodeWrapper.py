from urllib.request import Request, urlopen
import json


class interviewQuestion():

    def __init__(self):
        self._q_title = None
        self._q_difficulty = None
        self._q_url = None
        self._q_content = None

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

    def setContent(self, content):
        self._q_content = content

    def getTitle(self):
        return self._q_title

    def getDifficulty(self):
        return self._q_difficulty

    def getURL(self):
        return self._q_url

    def getContent(self):
        return self._q_content


class leetCodeQuestionQuery():

    def __init__(self):
        self._meta_link = "https://leetcode.com/api/problems/algorithms/"
        self._question_link_prefix = "https://leetcode.com/problems/"
        self._free_q_metas = []
        self._updateMeta()
        self._filterQuestions()

    def _updateMeta(self):
        req = Request(url=self._meta_link, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as url:
            self._meta = json.load(url)

    def _filterQuestions(self):
        q_status_list = self._meta["stat_status_pairs"]
        for q in q_status_list:
            if q["paid_only"] == False:
                self._free_q_metas.append(q)

    def length(self):
        return len(self._free_q_metas)

    def getQuestion(self, i: int):
        q_meta = self._free_q_metas[i]
        q_title = q_meta["stat"]["question__title"]
        q_title_slug = q_meta["stat"]["question__title_slug"]
        q_difficulty = q_meta["difficulty"]["level"]
        q_url = self._question_link_prefix + q_title_slug
        # open the link by the question into html
        req = Request(url=q_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as url:
            html_bytes = url.read()
            html_str = html_bytes.decode("utf8")
        # parse html and grab only the question content
        q_content_html = html_str  # TODO

        # wrap question class
        question_wrapper = interviewQuestion()
        question_wrapper.setTitle(q_title)
        question_wrapper.setDifficulty(q_difficulty)
        question_wrapper.setURL(q_url)
        question_wrapper.setContent(q_content_html)
        return question_wrapper


if __name__ == '__main__':
    query = leetCodeQuestionQuery()
    q = query.getQuestion(1)
    print(query.length())
    print(q.getTitle())
    print(q.getDifficulty())
    print(q.getURL())
    # print(q.getContent())
