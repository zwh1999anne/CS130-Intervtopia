from django.test import TestCase, Client
from evaluation.models import *
from django.urls import reverse
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_crud_a_question(self):
        test_dict = {'question_text': "Test Question for interviewee", 'target': 'EE',
                     'question_ranking': 99, 'question_name': 'test_q_for_ee'}

        # create
        question = Question.objects.create(**test_dict)

        self.assertEqual(question.target, 'EE')
        self.assertEqual(question.question_ranking, 99)
        self.assertEqual(question.question_name, 'test_q_for_ee')

        # read
        question_set = Question.objects.filter(**test_dict)

        for question in question_set.all():
            self.assertEqual(question.target, 'EE')
            self.assertEqual(question.question_ranking, 99)
            self.assertEqual(question.question_name, 'test_q_for_ee')

        # update
        update_dict = {'target': 'ER', 'question_ranking': 79}

        test_dict.update(update_dict)

        question_set.update(**update_dict)
        question_set = Question.objects.filter(**test_dict)

        for question in question_set.all():
            self.assertEqual(question.target, 'ER')
            self.assertEqual(question.question_ranking, 79)
            self.assertEqual(question.question_name, 'test_q_for_ee')

        # delete
        question_set.delete()

        question_set = Question.objects.filter(**test_dict)

        self.assertEqual(question_set.count(), 0)


class ChoiceModelTests(TestCase):

    def test_crud_a_chioce(self):
        test_dict_question = {'question_text': "Test Question for interviewee", 'target': 'EE',
                              'question_ranking': 99, 'question_name': 'test_q_for_ee'}
        question = Question.objects.create(**test_dict_question)
        test_dict_choice = {'question': question, 'choice_value': 3,
                            'choice_text': "so so", 'selected': False}

        # create
        choice = Choice.objects.create(**test_dict_choice)

        self.assertEqual(choice.question.question_name, 'test_q_for_ee')
        self.assertEqual(choice.choice_value, 3)
        self.assertEqual(choice.choice_text, "so so")
        self.assertEqual(choice.selected, False)

        # read
        choice_set = Choice.objects.filter(**test_dict_choice)

        for choice in choice_set.all():
            self.assertEqual(choice.question.question_name, 'test_q_for_ee')
            self.assertEqual(choice.choice_value, 3)
            self.assertEqual(choice.choice_text, "so so")
            self.assertEqual(choice.selected, False)

        # update
        update_dict = {'choice_text': "so good", 'selected': True}

        test_dict_choice.update(update_dict)

        choice_set.update(**update_dict)
        choice_set = Choice.objects.filter(**test_dict_choice)

        for choice in choice_set.all():
            self.assertEqual(choice.question.question_name, 'test_q_for_ee')
            self.assertEqual(choice.choice_value, 3)
            self.assertEqual(choice.choice_text, "so good")
            self.assertEqual(choice.selected, True)

        # delete
        choice_set.delete()

        choice_set = Choice.objects.filter(**test_dict_choice)

        self.assertEqual(choice_set.count(), 0)

        question.delete()


class ResponseModelTests(TestCase):

    def test_crud_a_response(self):
        test_dict = {'name': "Test response", 'problem_solving': 2,
                     'communication': 3, 'coding_skill': 4, 'helpful': 1}

        # create
        response = Response.objects.create(**test_dict)

        self.assertEqual(response.name, "Test response")
        self.assertEqual(response.problem_solving, 2)
        self.assertEqual(response.communication, 3)
        self.assertEqual(response.coding_skill, 4)
        self.assertEqual(response.helpful, 1)

        # read
        response_set = Response.objects.filter(**test_dict)

        for response in response_set.all():
            self.assertEqual(response.name, "Test response")
            self.assertEqual(response.problem_solving, 2)
            self.assertEqual(response.communication, 3)
            self.assertEqual(response.coding_skill, 4)
            self.assertEqual(response.helpful, 1)

        # update
        update_dict = {'communication': 5, 'problem_solving': 1}

        test_dict.update(update_dict)

        response_set.update(**update_dict)
        response_set = Response.objects.filter(**test_dict)

        for response in response_set.all():
            self.assertEqual(response.name, "Test response")
            self.assertEqual(response.problem_solving, 1)
            self.assertEqual(response.communication, 5)
            self.assertEqual(response.coding_skill, 4)
            self.assertEqual(response.helpful, 1)

        # delete
        response_set.delete()

        response_set = Response.objects.filter(**test_dict)

        self.assertEqual(response_set.count(), 0)


class EvalFormModelTests(TestCase):

    def test_crud_a_eval_form(self):
        test_dict_response = {'name': "Test response", 'problem_solving': 2,
                              'communication': 3, 'coding_skill': 4, 'helpful': 1}
        test_dict_question1 = {'question_text': "Test Question 1 for interviewee", 'target': 'EE',
                               'question_ranking': 99, 'question_name': 'test_q_for_ee'}
        test_dict_question2 = {'question_text': "Test Question 2 for interviewee", 'target': 'EE',
                               'question_ranking': 99, 'question_name': 'test_q_for_ee'}

        response = Response.objects.create(**test_dict_response)
        question1 = Question.objects.create(**test_dict_question1)
        question2 = Question.objects.create(**test_dict_question2)
        user = CustomUser.objects.create(username='carlo')

        test_dict_eval = {'name': "Test response", 'rating': 2, 'comments': 'no comment', 'response': response,
                          'targer_user': user, 'target_role': 'EE'}

        # create
        evalform = EvalForm.objects.create(**test_dict_eval)

        evalform.questions.set([question1, question2])

        self.assertEqual(evalform.name, "Test response")
        self.assertEqual(evalform.rating, 2)
        self.assertEqual(evalform.comments, 'no comment')
        self.assertEqual(evalform.target_role, 'EE')
        self.assertEqual(evalform.response.coding_skill, 4)
        self.assertEqual(evalform.targer_user.username, 'carlo')

        # read
        eval_set = EvalForm.objects.filter(**test_dict_eval)

        for evalform in eval_set.all():
            self.assertEqual(evalform.name, "Test response")
            self.assertEqual(evalform.rating, 2)
            self.assertEqual(evalform.comments, 'no comment')
            self.assertEqual(evalform.target_role, 'EE')
            self.assertEqual(evalform.response.coding_skill, 4)

        # update
        update_dict = {'rating': 5, 'comments': 'pretty good'}

        test_dict_eval.update(update_dict)

        eval_set.update(**update_dict)
        eval_set = EvalForm.objects.filter(**test_dict_eval)

        for evalform in eval_set.all():
            self.assertEqual(evalform.name, "Test response")
            self.assertEqual(evalform.rating, 5)
            self.assertEqual(evalform.comments, 'pretty good')
            self.assertEqual(evalform.target_role, 'EE')
            self.assertEqual(evalform.response.coding_skill, 4)

        # delete
        response.delete()
        question1.delete()
        question2.delete()
        user.delete()
        eval_set.delete()

        eval_set = EvalForm.objects.filter(**test_dict_eval)

        self.assertEqual(eval_set.count(), 0)
