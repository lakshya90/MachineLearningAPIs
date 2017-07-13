#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
from google.cloud import translate

def translate_text_with_model(target, text, model=translate.NMT):
    """Translates text into the target language.

    Make sure your project is whitelisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

if __name__ == '__main__':
	text=u'विश्व के प्रसिद्ध देशों में से एक भारत है। हरेक भारतीय नागरिक को इसके बारे में जानना चाहिये जैसे इसका इतिहास, संघर्ष और दूसरी मुख्य बातें। मुख्य परीक्षा या कक्षा के टेस्ट में सामान्यत: स्कूल या कॉलेज में विद्यार्थियों को इस विषय पर कुछ पैराग्राफ या पूरा निबंध लिखने के लिये दिया जाता है। यहाँ पर हम भारत को समझने के लिये बेहद आसान और विभिन्न शब्द सीमाओं के साथ अलग-अलग कक्षाओं के विद्यार्थियों की मदद के लिये निबंध उपलब्ध करा रहें हैं।'.encode('utf-8').strip()
	target = 'en'
	translate_text_with_model(target, text, model=translate.NMT)
