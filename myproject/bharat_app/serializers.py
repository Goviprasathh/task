from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn']

    # Dynamically return the translated question based on the language
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        lang = self.context.get('lang', 'en')
        # Translate the question based on the requested language
        translated_question = instance.get_translated_question(lang)
        representation['translated_question'] = translated_question
        return representation
