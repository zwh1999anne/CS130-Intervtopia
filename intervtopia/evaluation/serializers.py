from rest_framework import serializers
from evaluation.models import Question, EvalForm
from users.models import CustomUser

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    evalform = serializers.ReadOnlyField(source='evalform.name')
    
    class Meta:
        model = Question
        fields = ['url', 'evalform', 'question_text', 'target', 'question_ranking', 'score']


# class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
#     # question = serializers.StringRelatedField()

#     class Meta:
#         model = Choice
#         # fields = ['question', 'choice_value', 'choice_text', 'selected']


# class ResponseSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Response
        # fields = ['name', 'problem_solving', 'communication', 'coding_skill', 'helpful']


class EvalFormSerializer(serializers.HyperlinkedModelSerializer):
    # questions = serializers.StringRelatedField(many=True)
    # response = serializers.StringRelatedField()
    targer_user = serializers.HyperlinkedRelatedField(many = False, view_name='customuser-detail', queryset = CustomUser.objects.all())
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only = True)
    class Meta:
        model = EvalForm
        fields = ['url', 'id', 'name', 'targer_user', 'target_role', 'time', 'questions', 'comments']
