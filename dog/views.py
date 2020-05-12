# generated: d0e0768ac2fd22ac148fae0527182473

from dog.models import Dog, Boy, Girl, ShowResult, DogPicture, PuppieParent, Puppy, PuppyPicture, Content, BreedDescription, New, PhotoGallery, Contact, Link, MyBanner
from django.views.generic import TemplateView
from app.utils.views import Data, ZmeiDataViewMixin


from django.utils.translation import gettext_lazy as _


class DogIndexView(ZmeiDataViewMixin, TemplateView):

    template_name = "dog/index.html"

    def get_data(self, url, request, inherited=False):
        data = Data()

        dog_list = Dog.objects.filter(our_dog=True)

        data.update({'url': url, 'dog_list': dog_list})

        return data


class DogHomeView(DogIndexView):

    template_name = "dog/home.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        content = Content.objects.all()[0]
        news_last_article = New.objects.all().order_by('-date_created')[0]
        news_count = New.objects.count()

        data.update({'url': url, 'content': content,
                     'news_last_article': news_last_article, 'news_count': news_count})

        return data


class DogOurDogsView(DogIndexView):

    template_name = "dog/our_dogs.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        dog = Dog.objects.get(home_name=url.name)

        data.update({'url': url, 'dog': dog})

        return data


class DogPedigreeView(DogIndexView):

    template_name = "dog/pedigree.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        dog = Dog.objects.get(home_name=url.name)

        data.update({'url': url, 'dog': dog})

        return data


class DogBreedDescriptionView(DogIndexView):

    template_name = "dog/breed_description.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        breed_descript = BreedDescription.objects.all()[0]

        data.update({'url': url, 'breed_descript': breed_descript})

        return data


class DogPhotoGalleryView(DogIndexView):

    template_name = "dog/photo_gallery.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        foto_gallerys = PhotoGallery.objects.all()

        data.update({'url': url, 'foto_gallerys': foto_gallerys})

        return data


class DogPuppiesView(DogIndexView):

    template_name = "dog/puppies.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        contact = Contact.objects.get()
        puppy_groups = PuppieParent.objects.all().order_by('-date_of_birth')

        data.update({'url': url, 'contact': contact,
                     'puppy_groups': puppy_groups})

        return data


class DogContactView(DogIndexView):

    template_name = "dog/contact.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        contact = Contact.objects.get()

        data.update({'url': url, 'contact': contact})

        return data


class DogLinksView(DogIndexView):

    template_name = "dog/links.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        html_text = MyBanner.objects.get()
        banners = Link.objects.all()

        data.update({'url': url, 'html_text': html_text, 'banners': banners})

        return data


class DogNewsView(DogIndexView):

    template_name = "dog/news.html"

    def get_data(self, url, request, inherited=False):
        data = super().get_data(url, request, inherited)

        news = New.objects.all().order_by('-date_created')

        data.update({'url': url, 'news': news})

        return data
