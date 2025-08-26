from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from accounts.forms import TweetForm
from .models import Tweet


# Create your views here.
def home(request):
    return render(request, "home.html")

# def tweets_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         'object': obj,
#     }
#     return render(request, 'detail_view.html', context)

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