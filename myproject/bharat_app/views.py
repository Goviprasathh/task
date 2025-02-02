from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils import translate_text
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET', 'POST'])
def faq_list(request):
    if request.method == 'GET':
        # Handle GET request (same as before)
        lang = request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Handle POST request
        serializer = FAQSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new FAQ object to the database
            faq = serializer.save()

            # Automatically translate the question into Hindi and Bengali
            faq.question_hi = translate_text(faq.question, 'hi')
            faq.question_bn = translate_text(faq.question, 'bn')
            faq.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
