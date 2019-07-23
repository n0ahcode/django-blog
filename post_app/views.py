from django.shortcuts import render, redirect
from .models import PostTag, Post, PostComment, PostReComment, ChemicalTag
from .forms import PostSearchForm, PostCommentForm, PostReCommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q


class PostBaseListView(ListView):
    paginate_by = 10
    model = Post
    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tag'] = PostTag.objects.all()
        context['chemical_tag'] = ChemicalTag.objects.all()
        context['post_search_form'] = PostSearchForm()
        try:
            context['profile_img'] = Post.objects.get(id=1)
        except:
            context['profile_img'] = None
        return context



class PostIndexView(PostBaseListView):
    template_name = 'post_app/post_index.html'
    def get_queryset(self):
        try:
            word = self.request.GET['word']
        except:
            word = ''
        if word != '':
            queryset = self.model.objects.filter(Q(title__icontains=word) | Q(text__icontains=word))
        else:
            queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    

class PostTemplateView(PostIndexView):
    #ランキングも最近の投稿も同じクラスで取得する
    template_name = 'post_app/post_template.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset




class PostTagView(PostBaseListView):
    template_name = 'post_app/post_list.html'
    def get_queryset(self):
        tag = self.kwargs['tag']
        queryset = self.model.objects.filter(post_tag__name=tag)
        return queryset




class PostChemicalTagView(PostBaseListView):
    template_neme = 'post_app/post_list.html'
    def get_queryset(self):
        tag = self.kwargs['tag']
        queryset = self.model.objects.filter(chemical_tag__name=tag)
        return queryset





class PostDetailView(DetailView):
    model = Post
    template_name = 'post_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['post'] = Post.objects.get(id=id)
        view_counter_add(context['post'])
        context = super().get_context_data(**kwargs)
        context['post_tag'] = PostTag.objects.all()
        context['chemical_tag'] = ChemicalTag.objects.all()
        context['post_search_form'] = PostSearchForm()
        try:
            context['comment'] = context['post'].comment_set.all()
        except:
             context['comment'] = None
        try:
            context['recomment'] = context['comment'].recomment_set.all()
        except:
             context['recomment'] = None       
        context['recomment'] = PostReComment.objects.all()
        return context


class PostCommentCreateView(CreateView):
    model = PostComment
    template_name = 'post_app/comment.html'
    form_class = PostCommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment.target = Post.objects.get(pk=post_pk)
        comment.save()
        return redirect('post_app:post_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tag'] = PostTag.objects.all()
        context['chemical_tag'] = ChemicalTag.objects.all()
        context['post_search_form'] = PostSearchForm()
        return context    

        
class PostReCommentCreateView(CreateView):
    model = PostReComment
    template_name = 'post_app/comment.html'
    form_class = PostReCommentForm
    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment_pk = self.kwargs['comment_pk']
        comment.target = PostComment.objects.get(pk=comment_pk)
        comment.save()
        return redirect('post_app:post_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tag'] = PostTag.objects.all()
        context['chemical_tag'] = ChemicalTag.objects.all()
        context['post_search_form'] = PostSearchForm()
        return context    






def view_counter_add(view_counter_class):
    view_counter_class.view_counter += 1
    view_counter_class.save()
    return view_counter_class
