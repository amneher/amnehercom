from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


# Create your models here.
class Post(models.Model):
	""" docstring for Post
		models.Model
	"""
	
	title = models.CharField(max_length=200)
	author = models.ForeignKey(to='User', on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	content = MarkdownField(rendered_field='content_rendered', validator=VALIDATOR_STANDARD, use_editor=False, use_admin_editor=True)
	content_rendered = RenderedMarkdownField()

	def __str__(self):
		return self.title

	@property
	def text(self):
		return self.content_rendered

	@property
	def data(self):
		data = {}
		data['title'] = self.title
		data['author'] = self.author
		data['created'] = self.created
		data['updated'] = self.updated

		return data


class UserManager(DjangoUserManager):
    def new_public_user(self, email, first_name=None, last_name=None):
        """Construct and return a new Public user, assigned to the supplied client.

        Arguments:
            email: the email address of the user
            first_name: optional first name
            last_name: optional last name

        Returns:
            A new user instance assigned to the supplied client.
        """
        user = User()
        user.username = email
        user.email = email
        user.first_name = first_name or ''
        user.last_name = last_name or ''
        user.save()
        return user


class User(AbstractUser):
    """A regular Django user with some extras.
    """
    is_employee = models.BooleanField(default=False, help_text='Indicate if this is a Tagg employee')  # noqa: E501

    objects = UserManager()

    class Meta:
        db_table = 'amneher_user'

    @property
    def is_internal_user(self):
        """True when this user is super user, staff, or employee.
        """
        return (
            self.is_superuser or
            self.is_staff or
            self.is_employee
        )