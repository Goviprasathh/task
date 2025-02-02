from googletrans import Translator

def translate_text(text, target_lang='en'):
    """Translate text using Google Translate API."""
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Return the original text if translation fails
