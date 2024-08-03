from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


# NOTE: pk: takes in primary key of the article and the request

# load ups the main blog on index
class Index(ListView): # what does ListView does?
    model = Article
    queryset = Article.objects.all()
    template_name = 'blog/index.html'


class Featured(ListView):
	model = Article
	queryset = Article.objects.filter(featured=True).order_by('-date') # checks for if featured is checked in admin
	template_name = 'blog/featured.html'
	paginate_by = 1 # assigns page number


class DetailArticleView(DetailView):
	model = Article
	template_name = 'blog/blog_post.html'
    
    #still have to understand what are kwargs and args
	def get_context_data(self, *args, **kwargs):
		context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
		context['liked_by_user'] = False
		article = Article.objects.get(id=self.kwargs.get('pk')) # what does kwargs do?
		if article.likes.filter(pk=self.request.user.id).exists():
			context['liked_by_user'] = True
		return context
	
class LikeArticle(View):
	def post(self, request, pk):
		article = Article.objects.get(id=pk)
		if article.likes.filter(pk=self.request.user.id).exists():
			article.likes.remove(request.user.id)
		else:
			article.likes.add(request.user.id)

		article.save()
		return redirect('detail_article', pk)

class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Article
	template_name = 'blog/blog_delete.html'
	success_url = reverse_lazy('index')

	def test_func(self):
		article = Article.objects.get(id=self.kwargs.get('pk'))
		return self.request.user.id == article.author.id