from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Board, Rubric
from .forms import BoardForm


def index(request):
    bbs = Board.objects.all()
    rubrics = Rubric.objects.all()
    return render(request,"shop/index.html",{"bbs":bbs, "rubrics":rubrics})


def by_rubric(request, rubric_id):
    bbs  = Board.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}

    return render(request, 'shop/by_rubric.html', context)


class BoardCreateView(CreateView):
    template_name = 'shop/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context