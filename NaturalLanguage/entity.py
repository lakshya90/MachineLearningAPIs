from google.cloud import language
import six

def entities_text(text):
    """Detects entities in the text."""
    language_client = language.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = language_client.document_from_text(text)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.doc_type == language.Document.HTML
    entities = document.analyze_entities().entities

    for entity in entities:
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity.entity_type))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))

if __name__ == '__main__':
	text='Prime Minister Narendra Modi is speaking in Madison Square and Lakshya Sivaramakrishnan is speaking in Solve for India'
	print ('Text entered is : {}'.format(text))
	entities_text(text)
