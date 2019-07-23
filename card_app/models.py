from django.db import models

class CardPostTag(models.Model):
    name = models.CharField(verbose_name='カード記事タグ', max_length=64)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'カード記事タグ'
        verbose_name_plural = 'カード記事タグ'


class CardChemicalTag(models.Model):
    name = models.CharField(verbose_name='カード化学タグ', max_length=256)        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'カード化学タグ'
        verbose_name_plural = 'カード化学タグ'    


class Card(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=256)
    text = models.TextField(verbose_name='本文')
    post_tag = models.ManyToManyField(CardPostTag, verbose_name='記事カードタグ', blank=True)
    chemical_tag = models.ManyToManyField(CardChemicalTag, verbose_name='化学カードタグ', blank=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    thumnail = models.ImageField(upload_to='card_thumnail/', blank=True, null=True)
    view_counter = models.IntegerField(verbose_name='閲覧数', default=0)
    friend_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)
    detail = models.TextField(verbose_name='記事の説明', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'カード'
        verbose_name_plural = 'カード'    
        ordering = ('-created_at',)

class CardComment(models.Model):
    name = models.CharField(verbose_name='名前', max_length=256)
    text = models.TextField(verbose_name='コメント')
    thumnail = models.ImageField(upload_to='comment_thumnail/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    target = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='対象記事')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'カードコメント'
        verbose_name_plural = 'カードコメント'    
        ordering = ('-created_at',)
    


class CardReComment(models.Model):
    name = models.CharField(verbose_name='名前', max_length=256)
    text  = models.TextField(verbose_name='コメント')
    thumnail = models.ImageField(upload_to='recomment_thumnail/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    target = models.ForeignKey(CardComment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'カードコメントの返信'
        verbose_name_plural = 'カードコメントの返信'    
        ordering = ('-created_at',)
    





