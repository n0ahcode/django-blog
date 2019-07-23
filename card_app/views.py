from django.shortcuts import render, redirect
from .models import Card, CardPostTag, CardChemicalTag, CardComment, CardReComment
from .forms import CardSearchForm, CardCommentForm, CardReCommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q
from post_app.models import Post


class CardBaseListView(ListView):
    paginate_by = 10
    model = Card

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_post_tag'] = CardPostTag.objects.all()
        context['card_chemical_tag'] = CardChemicalTag.objects.all()
        context['card_search_form'] = CardSearchForm()
        try:
            context['profile_img'] = Post.objects.get(id=1)
        except:
            context['profile_img'] = None
        return context

class CardIndexView(CardBaseListView):
    template_name = 'card_app/card_index.html'

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


class CardTemplateView(CardIndexView):
    template_name = 'card_app/card_template.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context   


class CardPostTagView(CardBaseListView):
    template_name = 'card_app/card_list.html'
    def get_queryset(self):
        tag = self.kwargs['tag']
        queryset = self.model.objects.filter(post_tag__name=tag)
        return queryset

class CardChemicalTagView(CardBaseListView):
    template_neme = 'card_app/card_list.html'
    def get_queryset(self):
        tag = self.kwargs['tag']
        queryset = self.model.objects.filter(chemical_tag__name=tag)
        return queryset

class CardDetailView(DetailView):
    model = Card
    template_name = 'card_app/card_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['card'] = Card.objects.get(id=id)
        view_counter_add(context['card'])
        context = super().get_context_data(**kwargs)
        context['card_tag'] = CardPostTag.objects.all()
        context['card_chemical_tag'] = CardChemicalTag.objects.all()
        context['card_search_form'] = CardSearchForm()
        try:
            context['comment'] = context['card'].comment_set.all()
        except:
             context['comment'] = None
        try:
            context['recomment'] = context['comment'].recomment_set.all()
        except:
             context['recomment'] = None       
        context['recomment'] = CardReComment.objects.all()
        return context

class CardCommentCreateView(CreateView):
    model = CardComment
    template_name = 'card_app/comment.html'
    form_class = CardCommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment.target = Card.objects.get(pk=post_pk)
        comment.save()
        return redirect('card_app:card_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_tag'] = CardPostTag.objects.all()
        context['card_chemical_tag'] = CardChemicalTag.objects.all()
        context['card_search_form'] = CardSearchForm()
        return context    

        
class CardReCommentCreateView(CreateView):
    model = CardReComment
    template_name = 'card_app/comment.html'
    form_class = CardReCommentForm
    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['pk']
        comment_pk = self.kwargs['comment_pk']
        comment.target = CardComment.objects.get(pk=comment_pk)
        comment.save()
        return redirect('card_app:card_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_tag'] = CardPostTag.objects.all()
        context['card_chemical_tag'] = CardChemicalTag.objects.all()
        context['card_search_form'] = CardSearchForm()
        return context   




def view_counter_add(view_counter_class):
    view_counter_class.view_counter += 1
    view_counter_class.save()
    return view_counter_class
