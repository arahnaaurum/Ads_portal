from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import *
from .forms import *
from .filters import CommentFilter

from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст

from random import randint

class AdsList(ListView):
    model  = Post
    template_name = 'flatpages/ads.html'
    context_object_name = 'adslist'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5


class AdsDetail(DetailView):
    model = Post
    template_name = 'flatpages/adsdetail.html'
    context_object_name = 'ads'


class AdsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'flatpages/ads_add.html'
    form_class = AdsForm


class AdsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'flatpages/ads_edit.html'
    form_class = AdsForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Post.objects.get(pk=pk)



class AdsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'flatpages/ads_delete.html'
    queryset = Post.objects.all()
    success_url = '/ads/'


# class AuthorCreateView(PermissionRequiredMixin, CreateView): #можно создавать автора через готовую форму
#     template_name = 'flatpages/author_add.html'
#     form_class = AuthorForm
#     success_url = '/personal/'
#     permission_required = ('advert_table.add_author',)
#

class AuthorCreateView (LoginRequiredMixin, View):  #но я сделала специальную
    def get(self, request, *args, **kwargs):
        return render(request, 'flatpages/author_add.html')

    def post(self, request, *args, **kwargs):
        identity = request.user
        name = request.POST['name']
        if not Author.objects.filter(name=name): #проверка уникальности имени
            newauthor = Author(name=name, identity=identity)
            newauthor.save()
        else:
            raise ValueError('Name already used')
        return redirect('/personal/')


class CommentList(LoginRequiredMixin, ListView):
    model  = Comments
    template_name = 'flatpages/personal.html'
    context_object_name = 'commentslist'
    queryset = Comments.objects.order_by('-id')
    paginate_by = 10

    def get_filter(self):
        return CommentFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs),
                'filter': self.get_filter(),
                }


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'flatpages/comment_add.html'
    form_class = CommentForm
    success_url = '/ads/'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'flatpages/comment_delete.html'
    queryset = Comments.objects.all()
    success_url = '/ads/'


class CommentAcceptView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = Comments.objects.get(pk=pk)
        comment.accept_comment()
        return render(request, 'flatpages/comment_accept.html', {})

