from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment


def index(request):
    latest = Comment.objects.order_by('-pub_date')[:10]
    return render(request, 'index.html', {'comments': latest})


def new_comment(request):
    form = CommentForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        comment = form.save()
        comment.save()
        return redirect('index')
    return render(request, 'new_comment.html', {'form': form})
