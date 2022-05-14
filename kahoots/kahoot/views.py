from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from .models import Question, Choice, Quiz, Game, Participant


def latest_questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'questions': latest_question_list
    }
    template = loader.get_template('questions/questions_list.html')
    return HttpResponse(template.render(context, request))


def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)

    template = loader.get_template('questions/question.html')
    return HttpResponse(template.render({'question': question}, request))


@csrf_protect
def question_add_option(request, question_id):
    if request.method == 'POST':
        form = request.POST.dict()

        question = Question.objects.get(pk=question_id)
        new_option = Choice.objects.create(question=question, choice_text=form['option_text'])
        new_option.save()
    return redirect('question-detail', question_id=question_id)


@csrf_protect
def question_edit_option(request, question_id, choice_id):
    if request.method == 'POST':
        form = request.POST.dict()

        choice = Choice.objects.get(pk=choice_id)

        if form['choice_text']:
            choice.choice_text = form['choice_text']
            choice.save()
        else:
            choice.delete()

    return redirect('question-detail', question_id=question_id)


@csrf_protect
def question_delete_option(request, question_id, choice_id):
    if request.method == 'POST':
        choice = Choice.objects.get(pk=choice_id)
        choice.delete()

    return redirect('question-detail', question_id=question_id)


def quizzes(request):
    latest_quizzes_list = Quiz.objects.order_by('-pub_date')[:5]
    context = {
        'quizzes': latest_quizzes_list
    }
    template = loader.get_template('quizzes/quizzes_list.html')
    return HttpResponse(template.render(context, request))


def detail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    template = loader.get_template('quizzes/quiz.html')
    return HttpResponse(template.render({'quiz': quiz}, request))


@csrf_protect
def edit_question(request, quiz_id, question_id):
    if request.method == 'POST':
        form = request.POST.dict()

        question = Question.objects.get(pk=question_id)

        if form['question_text']:
            question.question_text = form['question_text']
            question.save()
        else:
            question.delete()

    return redirect('detail', quiz_id=quiz_id)


@csrf_protect
def delete_question(request, quiz_id, question_id):
    if request.method == 'POST':
        question = Question.objects.get(pk=question_id)
        question.delete()

    return redirect('detail', quiz_id=quiz_id)


@csrf_protect
def quiz_add_question(request, quiz_id):
    if request.method == 'POST':
        form = request.POST.dict()

        quiz = Quiz.objects.get(pk=quiz_id)
        new_question = Question.objects.create(quiz=quiz, question_text=form['question_text'])

        new_question.save()

        return redirect('question-detail', question=new_question)

    return


def initialize(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    new_game = Game.objects.create(quiz=quiz)
    new_game.save()

    request.session['admin'] = True
    return redirect('monitor', game_id=new_game.id)


def join_page(request):
    template = loader.get_template('game/join.html')
    return HttpResponse(template.render({}, request))


@csrf_protect
def join(request):
    if request.method == 'POST':
        form = request.POST.dict()

        game = Game.objects.get(code=form['form_game-id'])
        participant = Participant.objects.create(nickname=form['form_nickname'], game=game)

        request.session['participant_id'] = participant.id
        request.session['admin'] = False

        return redirect('monitor', game_id=game.id)


def monitor(request, game_id):
    game = Game.objects.get(pk=game_id)

    template = loader.get_template('game/monitor_start.html')
    return HttpResponse(template.render({
        'game': game,
        'participant': Participant.objects.get(pk=request.session['participant_id']) if request.session.get('participant_id', -1) != -1 else -1
    }, request))


def monitor_question(request , game_id):
    game = Game.objects.get(pk=game_id)

    template = loader.get_template()
    return HttpResponse(template.render({'game': game}, request))


def resolve(request, game_id):
    game = Game.objects.get(pk=game_id)

    if request.session.get('admin', False):
        if game.status == 0:
            return redirect('switch-question', game_id)
    else:
        if game.status == 0:
            return redirect('monitor', game_id)


def switch_question(request, game_id):
    game = Game.objects.get(pk=game_id)

    if request.session.get('admin', False):
        if game.status == 0:
            game.current_question = game.quiz.question_set.first()
            game.status = 1
            game.save()
        elif game.status == 1:
            try:
                game.current_question = game.current_question.get_next_in_order()
            except Question.DoesNotExist:
                game.status = 2
            finally:
                game.save()
        elif game.status == 2:
            pass

    redirect('resolve', game_id)


