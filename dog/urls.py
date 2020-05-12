# generated: b032dc6c45f7459d81351b673136b478

from django.conf.urls import url
from .views import DogHomeView, DogOurDogsView, DogPedigreeView, DogBreedDescriptionView, DogPhotoGalleryView, DogPuppiesView, DogContactView, DogLinksView, DogNewsView

urlpatterns = (
    url(r'^$', DogHomeView.as_view(), name='dog.home'),

    url(r'^dogs/(?P<name>[^\/]+)$',
        DogOurDogsView.as_view(), name='dog.our_dogs'),

    url(r'^dogs/(?P<name>[^\/]+)/pedigree/$',
        DogPedigreeView.as_view(), name='dog.pedigree'),

    url(r'^breed_description/$', DogBreedDescriptionView.as_view(),
        name='dog.breed_description'),

    url(r'^photo_gallery/$', DogPhotoGalleryView.as_view(), name='dog.photo_gallery'),

    url(r'^puppies/$', DogPuppiesView.as_view(), name='dog.puppies'),

    url(r'^contact/$', DogContactView.as_view(), name='dog.contact'),

    url(r'^links/$', DogLinksView.as_view(), name='dog.links'),

    url(r'^news/$', DogNewsView.as_view(), name='dog.news'),
)
