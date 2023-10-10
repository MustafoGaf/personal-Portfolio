from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from django.core.paginator import Paginator
from .form import EmailPostForm, CommentForm, BlogForm
import smtplib
from email.mime.text import MIMEText
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth import get_user
from django.utils.timezone import now


def send_email(mail_to, sub ,message):
    sender = "mustafogaforovdev@gmail.com"
    password = "lekwrrraxyfoqfon"
     
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = sub
        server.sendmail(sender, mail_to, msg.as_string())
        
    except:
        return "EROR $)$"

all_blog = Blog.objects.order_by("-date")

def blog(req, tag_slug = None):
    paginator = Paginator(all_blog, 5)
    page_number = req.GET.get("page", 1)
    blogs = paginator.page(page_number)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = all_blog.filter(tags__in=[tag])
    return render(req, 'blogs/blog.html', {"blogs":blogs, "tag":tag})

def detail(req, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.filter(active=True)
    form = CommentForm()
    
    blog_tags_ids = blog.tags.values_list("id", flat=True)
    similar_blogs = all_blog.filter(tags__in=blog_tags_ids).exclude(id = blog_id)
    similar_blogs = similar_blogs.annotate(same_tags=Count("tags")).order_by('-same_tags')[:4]
    
    return render(req, 'blogs/detail.html', {'blog':blog, "comments":comments, 'form':form, 'similar_blogs': similar_blogs})

def blog_share(req, blog_id):
    blog = get_object_or_404(Blog,id = blog_id)
    sent = False
    if req.method == "POST":
        form = EmailPostForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            blog_url = req.build_absolute_uri(blog.get_absolute_url())
            subject = f"{cd['name']} recomend you read" \
                f"{blog.title}"
            message = f"Read {blog.title} at {blog_url}\n\n"\
                f"{cd['name']}\'s comment : {cd['comment']}"
            send_email([cd['to']], subject, message)
            sent = True
    else: 
        form = EmailPostForm()
    
    return render(req, 'blogs/share.html', {"blog":blog, 'form':form, "sent":sent})

@require_POST
def blog_comment(req, blog_id):
     
    blog = get_object_or_404(Blog, id = blog_id)
    comment = None
    form = CommentForm(data=req.POST)
    if form.is_valid():
        
        comment = form.save(commit=False)
        
        comment.blog = blog
        
        comment.save()
        
    return render(req, 'blogs/comment.html', {"blog":blog, 'form': form, 'comment':comment})


