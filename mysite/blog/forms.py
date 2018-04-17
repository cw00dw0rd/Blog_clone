from django import forms
from blog.models import Comment, Post, User
from django.contrib.auth.forms import UserCreationForm

# Form for the admin to create new Posts, currently Staff Only
class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text','image')
        image = forms.ImageField(widget=forms.FileInput())

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image':forms.ClearableFileInput(attrs={'type':'file'})
        }

# Form for user to leave a comment and sets commenter name to be first name
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        # user = request.user.pk
        fields = ('text',)

        widgets = {
            # 'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'author': ('request.user.id'),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }

# Sign Up form using the UserCreationForm and sets Email to be auth token instead of username
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Unique Email address required.')
    username = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

# Allows user to sign in with email instead of username
class LoginForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Unique Email address required.')
    username = None

    class Meta:
        model = User
        fields = ('email', 'password')
