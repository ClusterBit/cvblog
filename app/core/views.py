from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Post, PostImages, NewsPost, Company
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm, CustomerSignForm, CompanySignForm, \
    PostCreateForm, ImagePostForm, CommentCreatePostForm, CommentCreateNewsPostForm


def index(request):
    catalog = Company.objects.reverse()[:8]
    context = {'catalog': catalog}
    return render(request, 'blog/index.html', context)


class signup(TemplateView):
    template_name = 'registration/signup.html'


def signup_customer(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        customer_profile_form = CustomerSignForm(request.POST, request.FILES)
        if customer_profile_form.is_valid() and user_form.is_valid():
            new_user = user_form.save(commit=False)
            customer_profile = customer_profile_form.save(commit=False)
            new_user.save()
            customer_profile.user = new_user
            customer_profile.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        user_form = UserCreateForm()
        customer_profile_form = CustomerSignForm(request.POST, request.FILES)
    context = {'user_form': user_form, 'customer_profile_form': customer_profile_form}
    return render(request, 'registration/signup_customer.html', context)


def signup_company(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        company_profile_form = CompanySignForm(request.POST, request.FILES)
        if company_profile_form.is_valid() and user_form.is_valid():
            new_user = user_form.save(commit=False)
            company_profile = company_profile_form.save(commit=False)
            new_user.save()
            company_profile.user = new_user
            company_profile.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        user_form = UserCreateForm()
        company_profile_form = CompanySignForm(request.POST, request.FILES)
    context = {'user_form': user_form, 'company_profile_form': company_profile_form}
    return render(request, 'registration/signup_company.html', context)


# ----------------------------------------------------------POST
def create_post(request):
    ImageFormSet = modelformset_factory(PostImages,
                                        form=ImagePostForm, extra=3)
    if request.method == 'POST':
        post_form = PostCreateForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PostImages.objects.none())
        if post_form.is_valid() and formset.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = PostImages(post=new_post, image=image)
                    photo.save()
            return redirect('home')
    else:
        post_form = PostCreateForm()
        formset = ImageFormSet(queryset=PostImages.objects.none())
    context = {'post_form': post_form, 'formset': formset}
    return render(request, 'blog/post_new.html', context)


def post_list(request):
    post_catalog = Post.objects.order_by('-created_on')
    context = {'post_catalog': post_catalog}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_comments = post.postcomment_set.order_by('-created_on')
    if request.method == 'POST':
        post_comment_form = CommentCreatePostForm(request.POST)
        if post_comment_form.is_valid():
            add_post_comment = post_comment_form.save(commit=False)
            add_post_comment.user = request.user
            add_post_comment.post = post
            add_post_comment.save()
    else:
        post_comment_form = CommentCreatePostForm(request.POST)
    context = {'post': post, 'post_comment_form': post_comment_form, 'post_comments': post_comments}
    return render(request, 'blog/post_detail.html', context)


# ----------------------------------------------------------NEWS
def news_list(request):
    news_catalog = NewsPost.objects.order_by('-created_on')
    context = {'news_catalog': news_catalog}
    return render(request, 'blog/news_list.html', context)


def news_detail(request, slug):
    news_post = get_object_or_404(NewsPost, slug=slug)
    news_comments = news_post.newspostcomment_set.order_by('-created_on')
    if request.method == 'POST':
        news_comment_form = CommentCreateNewsPostForm(request.POST)
        if news_comment_form.is_valid():
            add_news_comment = news_comment_form.save(commit=False)
            add_news_comment.user = request.user
            add_news_comment.post = news_post
            add_news_comment.save()
    else:
        news_comment_form = CommentCreateNewsPostForm(request.POST)
    context = {'news_post': news_post, 'news_comment_form': news_comment_form, 'news_comments': news_comments}
    return render(request, 'blog/news_detail.html', context)


# --------------------------------------------------------COMPANY
def catalog_list(request):
    catalog = Company.objects.all
    context = {'catalog': catalog}
    return render(request, 'blog/catalog_list.html', context)


def catalog_detail(request, pk):
    catalog_post = get_object_or_404(Company, pk=pk)
    context = {'catalog_post': catalog_post,}
    return render(request, 'blog/catalog_detail.html', context)


class about(TemplateView):
    template_name = 'blog/about.html'
