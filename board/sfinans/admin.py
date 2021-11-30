from django.contrib import admin

from sfinans import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(models.Subchapter)
class SubchapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(models.DocumentStatus)
class DocumentStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


@admin.register(models.GroupChapter)
class GroupChapterAdmin(admin.ModelAdmin):
    list_display = ['group', 'chapter']


@admin.register(models.ChapterSubchapter)
class ChapterSubchapterAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'subchapter']


@admin.register(models.ChapterSubchapterDocument)
class ChapterSubchapterDocumentAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'subchapter', 'document']