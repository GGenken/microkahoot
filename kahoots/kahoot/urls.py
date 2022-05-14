from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes, name='index'),
    path('<int:quiz_id>/', views.detail, name='detail'),
    path('<int:quiz_id>/edit_question/<int:question_id>/', views.edit_question, name='editquestion'),
    path('<int:quiz_id>/delete_question/<int:question_id>/', views.delete_question, name='deletequestion'),
    path('<int:quiz_id>/add_question/', views.quiz_add_question, name='addquestion'),

    path('<int:quiz_id>/start_quiz/', views.initialize, name='start-game'),
    path('join/', views.join_page, name='join-page'),
    path('play/', views.join, name='join'),
    path('resolve/<int:game_id>/', views.resolve, name='resolve'),
    path('monitor/<int:game_id>/', views.monitor, name='monitor'),
    path('monitor_question/<int:game_id>/', views.monitor_question, name='monitor-question'),
    path('switch_question/<int:game_id>/', views.switch_question, name='switch-question'),

    # path('<int:game_id>/play', views.question_answering_page, name='play'),
    # path('<int:game_id>/answer', views.accept_answer, name='accept-answer'),

    path('question/<int:question_id>/', views.question_detail, name='question-detail'),
    path('question/<int:question_id>/add_option/', views.question_add_option, name='question-addoption'),
    path('question/<int:question_id>/edit_option/<int:choice_id>/', views.question_edit_option, name='question-editoption'),
    path('question/<int:question_id>/delete_option/<int:choice_id>/', views.question_delete_option, name='question-deloption'),
]
