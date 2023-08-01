from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q, UniqueConstraint


class User(AbstractUser):
    """Custom user model."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name', )
    username = models.CharField(
        max_length=settings.LENGTH_OF_FIELDS_USER_1,
        unique=True,
        verbose_name='username'
    )
    first_name = models.CharField(
        max_length=settings.LENGTH_OF_FIELDS_USER_1,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=settings.LENGTH_OF_FIELDS_USER_1,
        verbose_name='Фамилия',
    )
    email = models.EmailField(
        max_length=settings.LENGTH_OF_FIELDS_USER_2,
        unique=True,
        verbose_name='email'
    )
    followers = models.ManyToManyField('self', verbose_name='following',
                                       symmetrical=False)

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Subscriptions model."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Автор'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписчик',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~Q(user=F('author')),
                name='no_self_follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.user} подписан(а) на {self.author}"
