from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import AllowAny
from .models import Poll, Question, Recommendation, Category, Choice, Answer, \
    Tip
from .serializers import PollSerializer, QuestionSerializer, \
    RecommendationSerializer, CategorySerializer, ChoiceSerializer, \
    AnswerSerializer, TipSerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    
    def get_queryset(self):
        return self.request.user.profile.get_recommendations()
        

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
        

class TipViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class AnswerUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        try:
            user = request.data.get('user', None)
            question_id = request.data.get('question', None)
            try:
                answerData = Answer.objects.filter(user=user)

                if(question_id == -1):
                    recommendations_filter = []
                    recommendations = Recommendation.objects.all()
                    categories = Category.objects.all()

                    data_recommendation = {}
                    for i in range(len(categories)):
                        data_recommendation[categories[i].id] = {'name': categories[i].name, 'recommendation':[], 
                            'bad_data' : 0, 'regular_data' : 0, 'good_data' : 0}

                    for i in range(len(answerData)):
                        choice_filter = answerData[i].choice
                        recommendation = Recommendation.objects.filter(choice=choice_filter)

                        if choice_filter.value > 3:
                            data_recommendation[choice_filter.question.category_id]['good_data'] += 1
                        elif choice_filter.value == 3:
                            data_recommendation[choice_filter.question.category_id]['regular_data'] += 1
                        else:
                            data_recommendation[choice_filter.question.category_id]['bad_data'] += 1

                        if (len(recommendation) > 0):
                            recommendation = recommendation[0]
                            if (recommendation.text != ""):
                                data_recommendation[recommendation.category_id]['recommendation'].append(recommendation.text)   

                    answerData = {'id': -1,
                              'response': data_recommendation,
                              }

                else:
                    for i in range(len(answerData)):
                        if(answerData[i].id == question_id):
                            answerData = answerData[i]
                            break
                    answerData = {'id': answerData.id,'choice': answerData.choice.id}

            except:
                answerData = {'id': -1,
                              'response': 'Answer does not exist'}

            return Response(answerData, status.HTTP_200_OK)

        except:  # User does not exist
            return Response({request},
                            status.HTTP_412_PRECONDITION_FAILED)
