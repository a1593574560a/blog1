#_*_ encoding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Notice(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=100)
    body = UEditorField(u'正文',filePath='body/ueditor/',imagePath='body/ueditor/',width=600, height=300,default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    class Meta:
        verbose_name = u'公告'
        verbose_name_plural = verbose_name

class Top(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=100)
    body = UEditorField(u'正文', filePath='body/ueditor/', imagePath='body/ueditor/', width=600, height=300,default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    class Meta:
        verbose_name = u'置顶'
        verbose_name_plural = verbose_name


class Label(models.Model):

    label = models.CharField(verbose_name=u'标签',max_length=10,default='')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.label
    def get_label_nums(self):
        return self.articles_set.count()
    def get_article_nums(self):

        return self.articles_set.count() + 2



class Articles(models.Model):
    label_one = models.ForeignKey(Label,verbose_name=u'标签', default='')
    desc = models.CharField(verbose_name=u'文章简介',max_length=300)
    title = models.CharField(verbose_name=u'标题',max_length=30)
    author = models.CharField(verbose_name=u'作者',max_length=10)
    click_nums = models.IntegerField(default=0,verbose_name=u'点击量')
    comment = models.IntegerField(default=0,verbose_name=u'评论数')
    body = UEditorField(u'内容	',width=600, height=300, imagePath="article/ueditor/", filePath="article/ueditor/",default='')
    image = models.ImageField(upload_to='illustration/%Y/%m',default='',null=True,blank=True,verbose_name=u'插图',max_length=200)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')
    class Meta:
        verbose_name = u'文章信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class ArticleList(models.Model):
    article = models.ForeignKey(Articles,verbose_name=u'文章')
    label = models.ForeignKey(Label,verbose_name=u'标签',default='')

    image = models.ImageField(upload_to='image/%Y/%m',verbose_name=u'封面图',max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    class Meta:
        verbose_name = u'文章列表'
        verbose_name_plural = verbose_name



class Contact(models.Model):
    nick_name = models.CharField(verbose_name=u'昵称',max_length=20)
    email = models.EmailField(verbose_name=u'邮箱')
    message = models.CharField(verbose_name=u'地址',max_length=500)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = verbose_name



class Talk(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=100)
    body = models.TextField(verbose_name=u'正文')
    image = models.ImageField(verbose_name=u'封面图',max_length=200,upload_to='talk/%Y/%m')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'说说'
        verbose_name_plural = verbose_name
class Banner(models.Model):
    image1 = models.ImageField(verbose_name=u'轮播图',max_length=200)
    image2 = models.ImageField(verbose_name=u'轮播图', max_length=200,default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name


class Study_label(models.Model):
    label = models.CharField(verbose_name=u'笔记标签',max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'笔记标签'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.label
    def get_study_nums(self):
        return self.study_set.count()

class Study(models.Model):
    study_label = models.ForeignKey(Study_label,verbose_name=u'学习标签')
    desc = models.CharField(verbose_name=u'文章简介', max_length=300)
    title = models.CharField(verbose_name=u'标题', max_length=30)
    author = models.CharField(verbose_name=u'作者', max_length=10)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')
    comment = models.IntegerField(default=0, verbose_name=u'评论数')
    body = UEditorField(u'内容	', width=600, height=300, imagePath="article/ueditor/", filePath="article/ueditor/",
                        default='')
    image = models.ImageField(upload_to='illustration/%Y/%m', default='', null=True, blank=True, verbose_name=u'插图',
                              max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'笔记信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title
    def get_studylist_nums(self):
        return self.studylist_set.count() + 2

class StudyList(models.Model):
    study_label = models.ForeignKey(Study_label,verbose_name=u'学习标签')
    study = models.ForeignKey(Study,verbose_name=u'笔记信息')
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name=u'封面图', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'笔记列表'
        verbose_name_plural = verbose_name

class Resources(models.Model):
    name = models.CharField(verbose_name=u'资源名',max_length=20)
    image = models.ImageField(upload_to='image/%Y/%m',verbose_name=u'封面图',max_length=200)
    download = models.FileField(upload_to='resources/%Y/%m',default='',max_length=200,verbose_name='下载链接')
    desc = models.CharField(verbose_name=u'简介',max_length=300,default='')
    add_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)
    class Meta:
        verbose_name = u'资源列表'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name
