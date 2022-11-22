from rest_framework import serializers
from .models import Question, Choice, Response, EvalForm


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ['question_name', 'question_text', 'target', 'question_ranking']


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Choice
        fields = ['question', 'choice_value', 'choice_text', 'selected']


class ResponseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Response
        fields = ['name', 'problem_solving', 'communication', 'coding_skill', 'helpful']


class EvalFormSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    response = serializers.StringRelatedField()
    targer_user = serializers.StringRelatedField()

    class Meta:
        model = EvalForm
        fields = ['name', 'questions', 'rating', 'comments', 'response', 'targer_user', 'target_role']
