from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.utils import timezone
import time

# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#@transaction.atomic
def vote(request, question):
    transaction.set_autocommit(False)
    try:
        q1 = Question(question_text=question, pub_date=timezone.now())
        q1.save()
        print(f"id is {q1.id}")
        
        #Question.objects.filter(id=id).update(question_text='modified')
        
        q1.id = None 
        q1.question_text = 'modified'
        q1.save()

        transaction.commit()
    except:
        transaction.rollback()
        raise
    finally:
        transaction.set_autocommit(True)
        pass

    return HttpResponse("You're question %s." % question)
