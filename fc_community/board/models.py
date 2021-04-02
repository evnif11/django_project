from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(max_length=128,
                                verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser',  # 1:N 한명의 유저와 여러개의 글
                               on_delete=models.CASCADE,
                               max_length=64,
                               verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록시간',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
