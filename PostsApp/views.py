from django.shortcuts import render, redirect
from . models import Post, Comment, Category, Like

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(post=post, author=request.user, content=content)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'posts/edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/delete_post.html', {'post': post})

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', post_id=comment.post.id)
    return render(request, 'posts/delete_comment.html', {'comment': comment})

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.content = request.POST['content']
        comment.save()
        return redirect('post_detail', post_id=comment.post.id)
    return render(request, 'posts/edit_comment.html', {'comment': comment}) 


# Create your views here.
