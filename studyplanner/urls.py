from django.urls import path, re_path
from . import views

app_name = 'studyplanner'

urlpatterns = [
    path('my-plans/', views.my_plans, name='my-plans'),
    path('archived-plans/', views.archived_plans, name='archived-plans'),
    path('create-plan/', views.create_plan, name='create-plan'),
    path('edit-plan/<int:pk>/', views.edit_plan, name='edit-plan'),
    path('plan-detail/<int:pk>/', views.plan_detail, name='plan-detail'),
    path('archive-plan/<int:pk>/', views.archive_plan, name='archive-plan'),
    path('unarchive-plan/<int:pk>/', views.unarchive_plan, name='unarchive-plan'),
    path('complete-plan/<int:pk>/', views.complete_plan, name='complete-plan'),
    path('print-plan/<int:pk>/', views.print_plan, name='print-plan'),
    path('add-subject/<int:pk>/', views.add_subject, name='add-subject'),
    path('edit-subject/<int:pk>/', views.edit_subject, name='edit-subject'),
    path('complete-subject/<int:pk>/', views.complete_subject, name='complete-subject'),
    path('delete-subject/<int:pk>/', views.DeleteSubject.as_view(), name='delete-subject'),
    path('add-subtopic/<int:pk>/', views.add_subtopic, name='add-subtopic'),
    path('edit-subtopic/<int:pk>/', views.edit_subtopic, name='edit-subtopic'),
    path('complete-subtopic/<int:pk>/', views.complete_subtopic, name='complete-subtopic'),
    path('delete-subtopic/<int:pk>/', views.DeleteSubtopic.as_view(), name='delete-subtopic'),
    path('add-path/<int:pk>/', views.add_path, name='add-path'),
    path('edit-path/<int:pk>/', views.edit_path, name='edit-path'),
    path('complete-path/<int:pk>/', views.complete_path, name='complete-path'),
    path('delete-path/<int:pk>/', views.DeletePath.as_view(), name='delete-path'),
    re_path(r'^add-method/(?P<pk>\d+)/(?P<pathpk>\d+)/(?P<flag>[\w-]+)/$', views.add_method, name='add-method'),
    path('edit-method/<int:pk>/', views.edit_method, name='edit-method'),
    re_path(r'^complete-method/(?P<pk>\d+)/(?P<flag>[\w-]+)/$', views.complete_method, name='complete-method'),
    path('delete-method/<int:pk>/', views.DeleteMethod.as_view(), name='delete-method'),
]