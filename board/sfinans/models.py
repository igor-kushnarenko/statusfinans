from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Разделы'
        verbose_name = 'Подразделы'


class Subchapter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Подразделы'
        verbose_name = 'Подраздел'


class DocumentStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Статусы документа'
        verbose_name = 'Статус документа'


class Document(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey(
        DocumentStatus,
        on_delete=models.PROTECT,
        default='',
        related_name='document',
        verbose_name='Статус',
    )


class GroupChapter(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        default='',
        related_name='group_chapter',
        verbose_name='Группа',
    )
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        default='',
        related_name='group_chapter',
        verbose_name='Раздел',
    )

    def __str__(self):
        return f'{self.group} - {self.chapter}'


class ChapterSubchapter(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        default='',
        related_name='chapter_subchapter',
        verbose_name='Раздел',
    )
    subchapter = models.ForeignKey(
        Subchapter,
        on_delete=models.CASCADE,
        default='',
        related_name='chapter_subchapter',
        verbose_name='Подгруппа',
    )

    def __str__(self):
        return f'{self.chapter} - {self.subchapter}'


class ChapterSubchapterDocument(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        default='',
        related_name='chapter_subchapter_document',
        verbose_name='Раздел',
    )
    subchapter = models.ForeignKey(
        Subchapter,
        on_delete=models.CASCADE,
        default='',
        related_name='chapter_subchapter_document',
        verbose_name='Подгруппа',
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        default='',
        related_name='chapter_subchapter_document',
        verbose_name='Документ',
    )

    def __str__(self):
        return f'{self.chapter} - {self.subchapter} - {self.document}'