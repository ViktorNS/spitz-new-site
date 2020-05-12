# generated: 2e3a3d91ed5b1052a107ce451ca64f71


from django.db import models
from polymorphic.models import PolymorphicModel
from ckeditor.fields import RichTextField


from django.utils.translation import gettext_lazy as _


class Dog(PolymorphicModel):
    """
    Dog
    """

    home_name = models.CharField(verbose_name=_(
        'Home name'), null=True, blank=True, max_length=100)
    full_name = models.CharField(verbose_name=_(
        'Full name'), null=True, blank=True, max_length=100)
    dog_sex = models.CharField(verbose_name=_(
        'Dog sex'), null=True, blank=True, max_length=100)
    date_of_birth = models.DateField(verbose_name=_(
        'Date of birth'), null=True, blank=True)
    pedigree = RichTextField(verbose_name=_('Pedigree'), null=True, blank=True)
    foto = models.ImageField(
        upload_to='image_upload/dog_foto', null=True, blank=True)
    our_dog = models.BooleanField(verbose_name=_(
        'Our dog'), blank=True, default=True)

    def __str__(self):
        return str(self.home_name) or "Dog {}".format(self.id)

    @classmethod
    def get_ref(cls):
        return 'dog'

    class Meta:
        verbose_name = _("Dog")


class Boy(Dog):
    """
    Boy
    """

    @classmethod
    def get_ref(cls):
        return 'boy'

    class Meta:
        verbose_name = _("Boy")


class Girl(Dog):
    """
    Girl
    """

    @classmethod
    def get_ref(cls):
        return 'girl'

    class Meta:
        verbose_name = _("Girl")


class ShowResult(models.Model):
    """
    ShowResult
    """

    dog = models.ForeignKey("dog.Dog", verbose_name=_(
        'Dog'), null=True, blank=True, related_name='show_results', on_delete=models.PROTECT)
    show_date = models.DateField(verbose_name=_(
        'Show date'), null=True, blank=True)
    show_id = models.CharField(verbose_name=_(
        'Show id'), null=True, blank=True, max_length=100)
    show_locale = models.CharField(verbose_name=_(
        'Show locale'), null=True, blank=True, max_length=100)
    show_judge = models.CharField(verbose_name=_(
        'Show judge'), null=True, blank=True, max_length=100)
    show_result = models.CharField(verbose_name=_(
        'Show result'), null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = _("Show result")


class DogPicture(models.Model):
    """
    DogPicture
    """

    dog = models.ForeignKey("dog.Dog", verbose_name=_(
        'Dog'), null=True, blank=True, related_name='dog_pictures', on_delete=models.PROTECT)
    picture = models.ImageField(
        upload_to='image_upload/dog_picture', null=True, blank=True)

    class Meta:
        verbose_name = _("Dog picture")


class PuppieParent(models.Model):
    """
    PuppieParent
    """

    dad = models.ForeignKey("dog.Boy", verbose_name=_(
        'Dad'), null=True, blank=True, related_name='+', on_delete=models.PROTECT)
    mom = models.ForeignKey("dog.Girl", verbose_name=_(
        'Mom'), null=True, blank=True, related_name='+', on_delete=models.PROTECT)
    date_of_birth = models.DateField(verbose_name=_(
        'Date of birth'), null=True, blank=True)

    def __str__(self):
        return _("Щенки {me.dad} и {me.mom}, {me.date_of_birth:%d.%m.%Y}").format(me=self)

    class Meta:
        verbose_name = _("Puppie parent")


class Puppy(models.Model):
    """
    Puppy
    """

    parents = models.ForeignKey("dog.PuppieParent", verbose_name=_(
        'Parents'), null=True, blank=True, related_name='puppies', on_delete=models.PROTECT)
    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100)
    p_sex = models.CharField(verbose_name=_(
        'P sex'), null=True, blank=True, max_length=4, choices=(('Boy', 'Boy'), ('Girl', 'Girl')))
    status = models.CharField(verbose_name=_('Status'), null=True, blank=True, max_length=9, choices=(
        ('Available', 'Available'), ('Reserved', 'Reserved'), ('Sold', 'Sold')))

    def __str__(self):
        return str(self.name) or "Puppy {}".format(self.id)

    class Meta:
        verbose_name = _("Puppy")


class PuppyPicture(models.Model):
    """
    PuppyPicture
    """

    puppy = models.ForeignKey("dog.Puppy", verbose_name=_(
        'Puppy'), null=True, blank=True, related_name='puppy_pictures', on_delete=models.PROTECT)
    picture = models.ImageField(
        upload_to='image_upload/puppies_foto', null=True, blank=True)

    class Meta:
        verbose_name = _("Puppy picture")


class Content(models.Model):
    """
    Content
    """

    title = models.CharField(verbose_name=_(
        'Title'), null=True, blank=True, max_length=100)
    home_text = RichTextField(verbose_name=_(
        'Home text'), null=True, blank=True)

    def __str__(self):
        return str(self.title) or "Content {}".format(self.id)

    class Meta:
        verbose_name = _("Content")


class BreedDescription(models.Model):
    """
    BreedDescription
    """

    br_descript = RichTextField(verbose_name=_(
        'Br descript'), null=True, blank=True)

    def __str__(self):
        return _("Breed Description").format(me=self)

    class Meta:
        verbose_name = _("Breed description")


class New(models.Model):
    """
    New
    """

    title = models.CharField(verbose_name=_(
        'Title'), null=True, blank=True, max_length=100)
    date_created = models.DateField(verbose_name=_(
        'Date created'), null=True, blank=True)
    news_text = RichTextField(verbose_name=_(
        'News text'), null=True, blank=True)

    def __str__(self):
        return str(self.title) or "New {}".format(self.id)

    class Meta:
        verbose_name = _("New")


class PhotoGallery(models.Model):
    """
    PhotoGallery
    """

    gallery = models.ImageField(
        upload_to='image_upload/gallery_foto', null=True, blank=True)

    class Meta:
        verbose_name = _("Photo gallery")


class Contact(models.Model):
    """
    Contact
    """

    kennel = models.CharField(verbose_name=_(
        'Kennel'), null=True, blank=True, max_length=100)
    owner1 = models.CharField(verbose_name=_(
        'Owner1'), null=True, blank=True, max_length=100)
    owner2 = models.CharField(verbose_name=_(
        'Owner2'), null=True, blank=True, max_length=100)
    adress = models.CharField(verbose_name=_(
        'Adress'), null=True, blank=True, max_length=100)
    country = models.CharField(verbose_name=_(
        'Country'), null=True, blank=True, max_length=100)
    phone = models.CharField(verbose_name=_(
        'Phone'), null=True, blank=True, max_length=100)
    e_mail = models.CharField(verbose_name=_(
        'E mail'), null=True, blank=True, max_length=100)

    def __str__(self):
        return str(self.kennel) or "Contact {}".format(self.id)

    class Meta:
        verbose_name = _("Contact")


class Link(models.Model):
    """
    Link
    """

    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100)
    banner = models.TextField(verbose_name=_('Banner'), null=True, blank=True)

    def __str__(self):
        return str(self.name) or "Link {}".format(self.id)

    class Meta:
        verbose_name = _("Link")


class MyBanner(models.Model):
    """
    MyBanner
    """

    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100)
    html_text = models.TextField(verbose_name=_(
        'Html text'), null=True, blank=True)

    def __str__(self):
        return str(self.name) or "My banner {}".format(self.id)

    class Meta:
        verbose_name = _("My banner")
