from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Post, PostImages, PostComment, Company
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm, CustomerSignForm, CompanySignForm, PostCreateForm, ImageForm, CommentCreateForm


class index(TemplateView):
    template_name = 'blog/index.html'


def post_list(request):
    post_catalog = Post.objects.order_by('-created_on')
    context = {'post_catalog': post_catalog}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.postcomment_set.order_by('-created_on')
    if request.method == 'POST':
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            new_comm = comment_form.save(commit=False)
            new_comm.user = request.user
            new_comm.post = post
            new_comm.save()
    else:
        comment_form = CommentCreateForm(request.POST)
    context = {'post': post, 'comment_form': comment_form, 'comments': comments}
    return render(request, 'blog/post_detail.html', context)


def news_list(request):
    post_catalog = Post.objects.order_by('-created_on')
    context = {'post_catalog': post_catalog}
    return render(request, 'blog/news_index.html', context)


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


class signup(TemplateView):
    template_name = 'registration/signup.html'


class about(TemplateView):
    template_name = 'blog/about.html'


def create_post(request):
    ImageFormSet = modelformset_factory(PostImages,
                                        form=ImageForm, extra=3)
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


def catalog_list(request):
    catalog = Company.objects.all
    context = {'catalog': catalog}
    return render(request, 'blog/catalog_list.html', context)


def catalog_detail(request, pk):
    catalog_post = get_object_or_404(Post, pk=pk)
    comments = post.postcomment_set.order_by('-created_on')
    if request.method == 'POST':
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            new_comm = comment_form.save(commit=False)
            new_comm.user = request.user
            new_comm.post = post
            new_comm.save()
    else:
        comment_form = CommentCreateForm(request.POST)
    context = {'catalog_post': catalog_post, 'comment_form': comment_form, 'comments': comments}
    return render(request, 'blog/catalog_detail.html', context)