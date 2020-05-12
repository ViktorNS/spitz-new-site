# generated: caf6b92b4a15171aea865651d28cb392


from modeltranslation.translator import translator, TranslationOptions
from dog.models import Puppy, Content, BreedDescription, New


class PuppyTranslationOptions(TranslationOptions):
    """
    Puppy TranslationOptions
    """

    fields = ['status']


translator.register(Puppy, PuppyTranslationOptions)


class ContentTranslationOptions(TranslationOptions):
    """
    Content TranslationOptions
    """

    fields = ['home_text']


translator.register(Content, ContentTranslationOptions)


class BreedDescriptionTranslationOptions(TranslationOptions):
    """
    BreedDescription TranslationOptions
    """

    fields = ['br_descript']


translator.register(BreedDescription, BreedDescriptionTranslationOptions)


class NewTranslationOptions(TranslationOptions):
    """
    New TranslationOptions
    """

    fields = ['title', 'news_text']


translator.register(New, NewTranslationOptions)
