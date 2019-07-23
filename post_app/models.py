from django.db import models


class PostTag(models.Model):
    name = models.CharField(verbose_name='記事タグ名', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '記事タグ'
        verbose_name_plural = '記事タグ'    


class ChemicalTag(models.Model):
    name = models.CharField(verbose_name='化学タグ名', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '化学タグ'
        verbose_name_plural = '化学タグ'    


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=256)
    text = models.TextField(verbose_name='本文')
    post_tag = models.ManyToManyField(PostTag, verbose_name='記事タグ', blank=True)
    chemical_tag = models.ManyToManyField(ChemicalTag, verbose_name='化学タグ', blank=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    thumnail = models.ImageField(upload_to='thumnail/', blank=True, null=True)
    view_counter = models.IntegerField(verbose_name='閲覧数', default=0)
    friend_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)
    detail = models.TextField(verbose_name='記事の説明', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'    
        ordering = ('-created_at',)
    

class PostComment(models.Model):
    name = models.CharField(verbose_name='名前', max_length=256)
    text = models.TextField(verbose_name='コメント')
    thumnail = models.ImageField(upload_to='comment_thumnail/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '記事コメント'
        verbose_name_plural = '記事コメント'    
        ordering = ('-created_at',)
    


class PostReComment(models.Model):
    name = models.CharField(verbose_name='名前', max_length=256)
    text  = models.TextField(verbose_name='コメント')
    thumnail = models.ImageField(upload_to='recomment_thumnail/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    target = models.ForeignKey(PostComment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '記事コメントの返信'
        verbose_name_plural = '記事コメントの返信'    
        ordering = ('-created_at',)
    


