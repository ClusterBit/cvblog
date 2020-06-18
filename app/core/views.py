from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from .models import Post, PostImages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm, CustomerSignForm, CompanySignForm, PostCreateForm, ImageForm


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/index.html'  # a list of all posts will be displayed on index.html


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # detail about each blog post will be on post_detail.html


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
