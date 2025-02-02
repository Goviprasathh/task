from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  
    question_hi = models.TextField(blank=True, null=True)  
    question_bn = models.TextField(blank=True, null=True) 

    def get_translated_question(self, lang='en'):
        """Return the translated question based on the requested language."""
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  

    def __str__(self):
        return self.question
