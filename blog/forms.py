from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'comment_author', 'email', 'comment_body'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_author'].widget.attrs.update({'class': 'form-control',
                                                           'placeholder': 'Your name',
                                                           'id': 'name',
                                                           })
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Your email address here',
                                                  })
        self.fields['comment_body'].widget.attrs.update({'class': 'form-control',
                                                         'placeholder': 'Write message here',
                                                         'id': 'email',
                                                         })
