#_*_ encoding: utf-8 _*_
__author__ = "Administrator"
__date__ = "2018/1/30 , 16:32"
from xadmin import views
import xadmin
from .models import Articles,ArticleList,Label,Contact,Notice,Top,Talk,Banner
from .models import Study_label,Study,StudyList
from .models import Resources





class BannerAdmin(object):
    list_display = ['image1', 'image2','add_time']
    search_fields = ['image1','image2']
    list_filter = ['image1','image2', 'add_time']


xadmin.site.register(Banner,BannerAdmin)

class TalkAdmin(object):
    list_display = ['title','body', 'add_time']
    search_fields = ['title','body']
    list_filter = ['title','body', 'add_time']


xadmin.site.register(Talk,TalkAdmin)



class NoticeAdmin(object):
    list_display = ['title','body', 'add_time']
    search_fields = ['title','body']
    list_filter = ['title','body', 'add_time']
    style_fields = {'body':'ueditor'}

xadmin.site.register(Notice,NoticeAdmin)
class TopAdmin(object):
    list_display = ['title', 'body', 'add_time']
    search_fields = ['title', 'body']
    list_filter = ['title', 'body', 'add_time']
    style_fields = {'body':'ueditor'}
xadmin.site.register(Top,TopAdmin)

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobAdminSettings(object):
    site_title = '后台管理系统'
    site_footer = '后台管理'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView,GlobAdminSettings)



class ArticlesAdmin(object):
    list_display = ['desc','title','author','click_nums','comment','body','image','add_time']
    search_fields = ['desc','title','author','click_nums','comment','body','image']
    list_filter = ['desc','title','author','click_nums','comment','body','image','add_time']
    model_icon = 'fa fa-pencil-square'
    relfield_style = 'fk-ajax'
    style_fields = {'body': 'ueditor'}

xadmin.site.register(Articles,ArticlesAdmin)


class ArticleListAdmin(object):
    list_display = ['image','add_time']
    search_fields = ['image']
    list_filter = ['image','add_time']
    model_icon = 'fa fa-file-text'
    relfield_style = 'fk-ajax'

xadmin.site.register(ArticleList,ArticleListAdmin)

class LabelAdmin(object):
    list_display = ['label','add_time']
    search_fields = ['label']
    list_filter = ['label','add_time']
    model_icon = 'fa fa-tag'
    relfield_style = 'fk-ajax'

xadmin.site.register(Label,LabelAdmin)

class ContactAdmin(object):
    list_display = ['nick_name','email','message','add_time']
    search_fields = ['nick_name','email','message']
    list_filter = ['nick_name','email','message','add_time']
    model_icon = 'fa fa-comment'

xadmin.site.register(Contact,ContactAdmin)


class StudyAdmin(object):
    list_display = ['desc','title','author','click_nums','comment','body','image','add_time']
    search_fields = ['desc','title','author','click_nums','comment','body','image']
    list_filter = ['desc','title','author','click_nums','comment','body','image','add_time']
    model_icon = 'fa fa-pencil-square'
    relfield_style = 'fk-ajax'
    style_fields = {'body': 'ueditor'}

xadmin.site.register(Study,StudyAdmin)

class StudyLabelAdmin(object):
    list_display = ['label','add_time']
    search_fields = ['label']
    list_filter = ['label','add_time']
    model_icon = 'fa fa-tag'
    relfield_style = 'fk-ajax'

xadmin.site.register(Study_label,StudyLabelAdmin)

class StudyListAdmin(object):
    list_display = ['image','add_time']
    search_fields = ['image']
    list_filter = ['image','add_time']
    model_icon = 'fa fa-file-text'
    relfield_style = 'fk-ajax'

xadmin.site.register(StudyList,StudyListAdmin)
class ResourcesAdmin(object):
    list_display = ['image', 'name', 'add_time']
    search_fields = ['image1', 'name']
    list_filter = ['image', 'name', 'add_time']


xadmin.site.register(Resources,ResourcesAdmin)