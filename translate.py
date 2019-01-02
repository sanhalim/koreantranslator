from google.cloud import translate
import sys

translate_client = translate.Client()
target='us'

translated = open(sys.argv[2], 'w+', encoding="utf-16")
with open(sys.argv[1], 'r', encoding="utf-16") as f:
    for line in f:
        text = line.strip('\n')

        result = translate_client.translate(text)
        print('{0},{1}\n'.format(text, result['translatedText']))
        translated.write('{0},{1}\n'.format(text, result['translatedText']))

translated.close()
