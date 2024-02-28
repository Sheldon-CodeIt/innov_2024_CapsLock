from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('/<int/', views.all_videos, name='all_videos'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('/<int:course_id>/<int:vid_id>/', views.video_detail, name='video_detail'),
    path('/<int:course_id>/<int:vid_id>/add_to_watch_later/', views.add_to_watch_later, name='add_to_watch_later'),
    path('liked_videos/', views.liked_videos, name='liked_videos'),
    path('watch_later_videos/', views.watch_later_videos, name='watch_later_videos'),
    path('courses/<int:course_id>/<int:vid_id>/add_to_liked_videos/', views.add_to_liked_videos, name='add_to_liked_videos'),
    # path('all_videosourse_id>/<int:vid_id>/save-notes/', views.save_video_notes, name='save_video_notes'),
    path('notes/', views.notes, name='notes'),

    path('course/', views.course, name='courseDetail'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('quiz/', views.quiz, name='quiz'),

    # Add more URLs as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
