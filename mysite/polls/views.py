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
        #with transaction.atomic():
        q1 = Question(question_text=question, pub_date=timezone.now())
        q1.save()
        
        #time.sleep(120)

        #q1.question_text="testMod"
        #q1.save()
        

        #id = 192564208089712602
        #q11 = Question.objects.filter(id=id).order_by("-id").first()
        
        
        #Question.objects.filter(id=id).update(question_text='modified')
        #q11.question_text = 'modifiedAgain'
        #q11.save()

        q2_text = str(question) + 'q2'
        q2 = Question(question_text=q2_text, pub_date=timezone.now())
        q2.save()

        transaction.commit()
    except:
        transaction.rollback()
        raise
    finally:
        transaction.set_autocommit(True)
        pass

    return HttpResponse("You're question %s." % question)
