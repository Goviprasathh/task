from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang='en'):
        """Return the translated question based on the requested language."""
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  # Default to English

    def __str__(self):
        return self.question
