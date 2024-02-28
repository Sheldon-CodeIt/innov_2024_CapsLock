from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Course, Video
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})


def course(request):
    return render(request, 'course/course.html')



@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    videos = Video.objects.filter(course=course)
    return render(request, 'course/course_detail.html', {'course': course, 'videos': videos})

@login_required
def video_detail(request, course_id, vid_id):
    course = get_object_or_404(Course, pk=course_id)
    video = get_object_or_404(Video, pk=vid_id, course_id=course_id)
    
    # Check if the video is added to watch later by the current user
    is_added_to_watch_later = WatchLaterVideo.objects.filter(user=request.user, video=video).exists()
    
    # Check if the video is liked by the current user
    is_added_to_liked_videos = LikedVideo.objects.filter(user=request.user, video=video).exists()
    
    return render(request, 'course/video_detail.html', {
        'course': course,
        'video': video,
        'is_added_to_watch_later': is_added_to_watch_later,
        'is_added_to_liked_videos': is_added_to_liked_videos  
    })

from django.http import HttpResponseBadRequest

@login_required
def save_video_notes(request, course_id, vid_id):
    # Retrieve the video object
    video = get_object_or_404(Video, pk=vid_id, course_id=course_id)
    
    if request.method == 'POST':
        # Update or create the notes for the video
        video.notes = request.POST.get('notes', '')
        video.save()
        # Redirect back to the video detail page
        return redirect('video_detail', course_id=course_id, vid_id=vid_id)
    else:
        # If request method is not POST, return some error response or handle as needed
        return HttpResponseBadRequest("Invalid request method")


@login_required
def add_to_watch_later(request, course_id, vid_id):
    # Retrieve the video object
    video = get_object_or_404(Video, pk=vid_id, course_id=course_id)
    
    # Check if the video is already added to watch later by the current user
    if WatchLaterVideo.objects.filter(user=request.user, video=video).exists():
        # If already added, remove it from watch later
        WatchLaterVideo.objects.filter(user=request.user, video=video).delete()
    else:
        # If not added, add it to watch later
        WatchLaterVideo.objects.create(user=request.user, video=video)
    
    # Redirect back to the video detail page
    return redirect('video_detail', course_id=course_id, vid_id=vid_id)

@login_required
def add_to_liked_videos(request, course_id, vid_id):
    # Retrieve the video object
    video = get_object_or_404(Video, pk=vid_id, course_id=course_id)
    
    # Check if the video is already liked by the current user
    if LikedVideo.objects.filter(user=request.user, video=video).exists():
        # If already liked, remove it from liked videos
        LikedVideo.objects.filter(user=request.user, video=video).delete()
        is_added_to_liked_videos = False  # Set the flag to indicate removal
    else:
        # If not liked, add it to liked videos
        LikedVideo.objects.create(user=request.user, video=video)
        is_added_to_liked_videos = True  # Set the flag to indicate addition
    
    # Redirect back to the video detail page
    return redirect('video_detail', course_id=course_id, vid_id=vid_id)


@login_required
def liked_videos(request):
    """
    Display all videos liked by the current user.
    """
    # Get the videos liked by the current user
    liked_videos = LikedVideo.objects.filter(user=request.user)
    return render(request, 'liked_videos.html', {'liked_videos': liked_videos})


@login_required
def watch_later_videos(request):
    watch_later_videos = WatchLaterVideo.objects.filter(user=request.user)
    return render(request, 'watch_later_videos.html', {'watch_later_videos': watch_later_videos})

def all_videos(request):
    videos = Video.objects.all()
    return render(request, 'all_videos.html', {'videos': videos})
