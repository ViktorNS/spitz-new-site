# generated: 2a782eeeb7447ff9dc19fabb6da33872


from django.contrib import admin
from django import forms
from dog.models import Dog, Boy, Girl, ShowResult, DogPicture, PuppieParent, Puppy, PuppyPicture, Content, BreedDescription, New, PhotoGallery, Contact, Link, MyBanner
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from django.contrib.admin import TabularInline, ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin


class DogModelForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ()
        widgets = {

        }


class DogAdmin(PolymorphicParentModelAdmin):
    """
    #dog
    Dog Admin
    """

    base_model = Dog

    child_models = (Boy, Girl,)


admin.site.register(Dog, DogAdmin)


class BoyModelForm(forms.ModelForm):
    class Meta:
        model = Boy
        exclude = ()
        widgets = {

        }


class BoyShowResultsInline(TabularInline):
    model = ShowResult
    suit_classes = 'suit-tab suit-tab-general'

    extension = 0
    fk_name = 'dog'
    fields = ['show_date', 'show_id',
              'show_locale', 'show_judge', 'show_result']


class BoyDogPicturesInline(TabularInline):
    model = DogPicture
    suit_classes = 'suit-tab suit-tab-general'

    extension = 0
    fk_name = 'dog'
    fields = ['picture']


class BoyAdmin(PolymorphicChildModelAdmin):
    """
    #boy
    Boy Admin
    """

    base_model = Boy

    form = BoyModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['home_name', 'full_name', 'dog_sex', 'date_of_birth', 'pedigree', 'foto', 'our_dog']
        }),)

    inlines = [BoyShowResultsInline, BoyDogPicturesInline]


admin.site.register(Boy, BoyAdmin)


class GirlModelForm(forms.ModelForm):
    class Meta:
        model = Girl
        exclude = ()
        widgets = {

        }


class GirlShowResultsInline(TabularInline):
    model = ShowResult
    suit_classes = 'suit-tab suit-tab-general'

    extension = 0
    fk_name = 'dog'
    fields = ['show_date', 'show_id',
              'show_locale', 'show_judge', 'show_result']


class GirlDogPicturesInline(TabularInline):
    model = DogPicture
    suit_classes = 'suit-tab suit-tab-general'

    extension = 0
    fk_name = 'dog'
    fields = ['picture']


class GirlAdmin(PolymorphicChildModelAdmin):
    """
    #girl
    Girl Admin
    """

    base_model = Girl

    form = GirlModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['home_name', 'full_name', 'dog_sex', 'date_of_birth', 'pedigree', 'foto', 'our_dog']
        }),)

    inlines = [GirlShowResultsInline, GirlDogPicturesInline]


admin.site.register(Girl, GirlAdmin)


class PuppieParentModelForm(forms.ModelForm):
    class Meta:
        model = PuppieParent
        exclude = ()
        widgets = {

        }


class PuppieParentAdmin(ModelAdmin):
    """
    #puppie_parent
    PuppieParent Admin
    """

    form = PuppieParentModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['dad', 'mom', 'date_of_birth']
        }),)


admin.site.register(PuppieParent, PuppieParentAdmin)


class PuppyModelForm(forms.ModelForm):
    class Meta:
        model = Puppy
        exclude = ()
        widgets = {

        }


class PuppyPuppyPicturesInline(TabularInline):
    model = PuppyPicture
    suit_classes = 'suit-tab suit-tab-general'

    extension = 0
    fk_name = 'puppy'
    fields = ['picture']


class PuppyAdmin(TabbedTranslationAdmin):
    """
    #puppy
    Puppy Admin
    """

    form = PuppyModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['parents', 'name', 'p_sex', 'status']
        }),)

    inlines = [PuppyPuppyPicturesInline]


admin.site.register(Puppy, PuppyAdmin)


class ContentModelForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ()
        widgets = {

        }


class ContentAdmin(TabbedTranslationAdmin):
    """
    #content
    Content Admin
    """

    form = ContentModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['title', 'home_text']
        }),)


admin.site.register(Content, ContentAdmin)


class BreedDescriptionModelForm(forms.ModelForm):
    class Meta:
        model = BreedDescription
        exclude = ()
        widgets = {

        }


class BreedDescriptionAdmin(TabbedTranslationAdmin):
    """
    #breed_description
    BreedDescription Admin
    """

    form = BreedDescriptionModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['br_descript']
        }),)


admin.site.register(BreedDescription, BreedDescriptionAdmin)


class NewModelForm(forms.ModelForm):
    class Meta:
        model = New
        exclude = ()
        widgets = {

        }


class NewAdmin(TabbedTranslationAdmin):
    """
    #new
    New Admin
    """

    form = NewModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['title', 'date_created', 'news_text']
        }),)


admin.site.register(New, NewAdmin)


class PhotoGalleryModelForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        exclude = ()
        widgets = {

        }


class PhotoGalleryAdmin(ModelAdmin):
    """
    #photo_gallery
    PhotoGallery Admin
    """

    form = PhotoGalleryModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['gallery']
        }),)


admin.site.register(PhotoGallery, PhotoGalleryAdmin)


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()
        widgets = {

        }


class ContactAdmin(ModelAdmin):
    """
    #contact
    Contact Admin
    """

    form = ContactModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['kennel', 'owner1', 'owner2', 'adress', 'country', 'phone', 'e_mail']
        }),)


admin.site.register(Contact, ContactAdmin)


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ()
        widgets = {

        }


class LinkAdmin(ModelAdmin):
    """
    #link
    Link Admin
    """

    form = LinkModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'banner']
        }),)


admin.site.register(Link, LinkAdmin)


class MyBannerModelForm(forms.ModelForm):
    class Meta:
        model = MyBanner
        exclude = ()
        widgets = {

        }


class MyBannerAdmin(ModelAdmin):
    """
    #my_banner
    MyBanner Admin
    """

    form = MyBannerModelForm

    suit_form_tabs = (
        ('general', 'General'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'html_text']
        }),)


admin.site.register(MyBanner, MyBannerAdmin)
