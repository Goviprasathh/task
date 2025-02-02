from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import FAQ
from .utils import translate_text

@receiver(pre_save, sender=FAQ)
def translate_question(sender, instance, **kwargs):
    """Automatically translate the question before saving."""
    if not instance.question_hi or instance.question_hi == instance.question:
        instance.question_hi = translate_text(instance.question, 'hi')

    if not instance.question_bn or instance.question_bn == instance.question:
        instance.question_bn = translate_text(instance.question, 'bn')
