from django.db import models  # 장고에서 제공하는 모델(model)


# DB와 연결해주는 인터페이스, 클래스 형태로 데이터 객체 모델링
class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록시간',
    )

    def __str__(self):
        return self.username

    class Meta:  # DB 메타정보
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
