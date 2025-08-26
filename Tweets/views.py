from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from accounts.forms import TweetForm
from .models import Tweet
from History.models import History


# Create your views here.
def home(request):
    return render(request, "home.html")

class TweetDetailView(DetailView):
    model = Tweet
    template_name = "detail_view.html"
    context_object_name = "tweet"

    def get_object(self, queryset=Tweet.objects.all()):
        return Tweet.objects.get(pk=self.kwargs['pk'])

# def tweets_list_view(request):
#     qs = Tweet.objects.all()
#     print(qs)
#     context = {
#         'query': qs,
#     }
#     return render(request, 'list_view.html', context)

class TweetListView(ListView):
    model = Tweet
    template_name = "list_view.html"
    context_object_name = "tweets"
    queryset = Tweet.objects.all()

class TweetCreateView(CreateView):
    model = Tweet
    fields = ['content',]
    template_name = "create_view.html"
    success_url = reverse_lazy('list_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

class HistoryListView(ListView):
    model = History
    template_name = "history.html"
    context_object_name = "all-history"