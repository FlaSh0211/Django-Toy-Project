from django.shortcuts import render, get_object_or_404, redirect
from . models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from . form import BlogPost
# Create your views here.
def home(request):
    blogs = Blog.objects #.all()를 붙이면 home.html 에서 blogs.all -> blogs 로 대체 가능
    blog_list = Blog.objects.all() #모든 글을 대상으로
    paginator = Paginator(blog_list, 3) #3개를 한 페이지로 자른다
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs' : blogs, 'posts' : posts})

def details(request, blog_id): # Blog 객체안의 인스턴스 개수를 id로 가져옴(등록 순서 게시판에서 1 2 3...)
    detail = get_object_or_404(Blog, pk = blog_id) 
    # get_object_or_404(): 객체를 받아 키워드 인수를 get함수를 통해 받아온다. 그리고 객체가 없으면 404를 리턴.
    return render(request, 'blog/details.html', {'detail' : detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()   #블로그 데이터베이스에 접속하여 직접 추가 하지 않고 사용자가 추가하려면 Blog 객체를 생성한다
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs' : blogs})
    #return redirect('/blog/ + str(blod_id))

def blogpost(request): #입력된 내용을 처리하는 form 함수 (post 방식)
    if request.method == 'POST':
        form = BlogPost(request.POST or None) #form.py 의 입력받은 값을 가져옴
        blogs = Blog.objects.all()
        if form.is_valid(): # 가져온 값을 검사
            post = form.save(commit=False) #db에 저장되지 않고 값들을 담은 객체가 반환된다
            inputtitle = form.cleaned_data['title']
            if blogs.filter(title = inputtitle): # 원래 있던 타이틀이면 등록 x
                existtitle = blogs.filter(title = inputtitle)
                return redirect('error')
            if '시발' in form.cleaned_data['body']: # .find()도 있지만 잘 안됨 
                return redirect('error2')
            post.pub_date = timezone.now() # 시간을 아직 처리 안했기 때문에 위와 같이 함
            post.save() # db에 저장
            return redirect('home')
    else:
        form = BlogPost() # form를 띄워 준다 ()안에 비어있으면 get 방식 
        return render(request, 'blog/new2.html', {'form': form})

def error(request):
    return render(request, 'blog/error.html')

def error2(request):
    return render(request, 'blog/error2.html')