#_*_ encoding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from .models import ArticleList,Articles,Contact,Label,Notice,Top,Banner
from forms import CommentForm,SearchForm,StudySearchForm,RssSearchForm
from .models import StudyList,Study_label,Study
from django.db.models import Q
from django.http import HttpResponse
from .models import Resources
# Create your views here.



class IndexView(View):
    def get(self,request):
        article_list = ArticleList.objects.all().order_by('-add_time')[:5]
        new_article = ArticleList.objects.all().order_by('-add_time')[:8]
        article = Articles.objects.all()
        label = Label.objects.all()
        top = Top.objects.all()
        notice = Notice.objects.all()
        banner = Banner.objects.all()
        return render(request,'index.html',{
            'article_list':article_list,
            'new_article': new_article,
            'article': article,
            'label': label,
            'banner': banner,
            'top': top,
            'notice': notice,
        })
class TitleDetailView(View):
    def get(self,request,article_id):
        article = Articles.objects.get(id=int(article_id))
        new_article = ArticleList.objects.all().order_by('-add_time')[:8]
        articles = Articles.objects.all()
        article.click_nums += 1
        article.save()
        label = Label.objects.all()
        top = Top.objects.all()
        notice = Notice.objects.all()
        comments = Contact.objects.all().order_by('-add_time')[:3]
        return render(request,'show.html',{
            'article':article,
            'new_article': new_article,
            'articles': articles,
            'label': label,
            'top': top,
            'notice': notice,
            'comments': comments,
        })
    def post(self, request,article_id):
        article = Articles.objects.get(id=int(article_id))

        contact_form = CommentForm(request.POST)
        if contact_form.is_valid():
            nick_name = request.POST.get('nickname', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            contact = Contact()
            contact.nick_name = nick_name
            contact.email = email
            contact.message = message
            if Contact.objects.filter(nick_name=nick_name, email=email, message=message):
                return render(request,'show.html',{'msg':'不要重复评论'})
            contact.save()
            article.comment += 1
            article.save()
        return HttpResponse('{"status":"success", "msg":"评论成功,刷新页面返回"}', content_type='application/json')




class ArticleListView(View):
    def get(self,request):
        article_list = ArticleList.objects.all()
        new_article = ArticleList.objects.all().order_by('-add_time')[:8]
        search_keywords = request.GET.get('keywords', '')
        label = Label.objects.all()
        if search_keywords:
            article_list = article_list.filter(Q(article__author__icontains=search_keywords)|Q(article__desc__icontains=search_keywords)|Q(article__title__icontains=search_keywords))
        return render(request,'list.html',{
            'article_list':article_list,
            'new_article': new_article,
            'label': label,
        })




class SearchView(View):
    def post(self,request):
        new_article = ArticleList.objects.all().order_by('-add_time')[:8]
        label = Label.objects.all()
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            article_list = ArticleList.objects.all()
            study_list = StudyList.objects.all()
            search_keywords = request.POST.get('keyword', '')
            if search_keywords:
                article_list = article_list.filter(Q(article__title__icontains=search_keywords) | Q(article__title__icontains=search_keywords))
                study_list = study_list.filter(Q(study__desc__icontains=search_keywords)|Q(study__title__icontains=search_keywords))
        return render(request,'search.html',{
            'article_list': article_list,
            'label':label,
            'new_article':new_article,
            'study_list' :study_list,
        })

class StudyListView(View):
    def get(self,request):
        study_list = StudyList.objects.all()
        study_label = Study_label.objects.all()
        new_study = StudyList.objects.all().order_by('-add_time')[:8]
        return render(request,'study-list.html',{
            'study_list': study_list,
            'new_study': new_study,
            'study_label': study_label,
        })
class StudyDetailView(View):
    def get(self,request,study_id):
        study = Study.objects.get(id=int(study_id))
        studys = Study.objects.all()
        study.click_nums += 1
        study.save()
        top = Top.objects.all()
        notice = Notice.objects.all()
        study_label = Study_label.objects.all()

        new_study = StudyList.objects.all().order_by('-add_time')[:8]
        comments = Contact.objects.all().order_by('-add_time')[:3]
        return render(request, 'study-detail.html', {
            'study': study,
            'top': top,
            'notice': notice,
            'new_study': new_study,
            'studys': studys,
            'study_label':study_label,
            'comments':comments,
        })
    def post(self, request,study_id):
        study = Articles.objects.get(id=int(study_id))
        contact_form = CommentForm(request.POST)
        if contact_form.is_valid():
            nick_name = request.POST.get('nickname', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            contact = Contact()
            contact.nick_name = nick_name
            contact.email = email
            contact.message = message
            if Contact.objects.filter(nick_name=nick_name, email=email, message=message):
                return render(request,'show.html',{'msg':'不要重复评论'})
            contact.save()
            study.comment += 1
            study.save()
        return HttpResponse('{"status":"success", "msg":"评论成功,刷新页面返回"}', content_type='application/json')

class StudySearchView(View):
    def post(self,request):
        search_form = StudySearchForm(request.POST)
        new_study = StudyList.objects.all().order_by('-add_time')[:8]
        stduy_label = Study_label.objects.all()
        if search_form.is_valid():
            study_list = StudyList.objects.all()
            search_keywords = request.POST.get('keyword', '')
            if search_keywords:
                study_list = study_list.filter(Q(study__desc__icontains=search_keywords)|Q(study__title__icontains=search_keywords))
        return render(request, 'search-study.html', {
            'stduy_label': stduy_label,
            'new_study': new_study,
            'study_list': study_list,
        })

def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html',)
    response.status_code = 404
    return response

class ResourcesView(View):
    def get(self,request):
        all_resources = Resources.objects.all()
        new_rss = Resources.objects.all().order_by('-add_time')[:8]
        return render(request,'resources.html',{
            'all_resources':all_resources,
            'new_rss':new_rss,
        })
class ResourceSearchView(View):
    def post(self,request):
        rss_search = RssSearchForm(request.POST)
        new_rss = Resources.objects.all().order_by('-add_time')[:8]
        if rss_search.is_valid():
            all_rss = Resources.objects.all()
            search_keywords = request.POST.get('keyword', '')
            if search_keywords:
                all_rss = all_rss.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))
        return render(request, 'resources-search.html', {
            'new_rss': new_rss,
            'all_rss': all_rss,
        })