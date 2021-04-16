from django.urls import path
from .views import AudioTypeCreate,AudioTypeEdit,AudioTypeList,AudioTypeDelete,SongCreateView,SongEditView,SongDeleteView,SongDetailView,SongListView,SongEditListView,SongDeleteListView
from .views import AudioBookDeleteView,AudioBookDetailView,AudioBookEditListView,AudioBookEditView,AudioBookListView,AudioBookCreateView,AudioBookDeleteListView
from .views import PodcastCreateView,PodcastEditView,PodcastDetailView,PodcastDeleteView,PodcastListView,PodcastEditListView,PodcastDeleteListView
urlpatterns = [
    path('',AudioTypeCreate.as_view(),name='typecreate'),
    path('audiotypelist',AudioTypeList.as_view(),name='typelist'),
    path('audiotypeedit',AudioTypeEdit.as_view(),name='typeedit'),
    path('audiotypedelete',AudioTypeDelete.as_view(),name='typedelete'),
    path('song',SongCreateView.as_view(),name="songcreate"),
    path('songedit/<int:pk>',SongEditView.as_view(),name="song_edit"),
    path('songdelete/<int:pk>',SongDeleteView.as_view(),name="song_delete"),
    path('songdetail/<int:pk>',SongDetailView.as_view(),name="song_detail"),
    path('songlist',SongListView.as_view(),name="songlist"),
    path('songeditlist',SongEditListView.as_view(),name="songeditlist"),
    path('songdeletelist',SongDeleteListView.as_view(),name="songdeletelist"),
    path('audiobook',AudioBookCreateView.as_view(),name="audiocreate"),
    path('audioedit/<int:pk>',AudioBookEditView.as_view(),name="audio_edit"),
    path('audiodelete/<int:pk>',AudioBookDeleteView.as_view(),name="audio_delete"),
    path('audiodetail/<int:pk>',AudioBookDetailView.as_view(),name="audio_detail"),
    path('audiolist',AudioBookListView.as_view(),name="audiolist"),
    path('audioeditlist',AudioBookEditListView.as_view(),name="audioeditlist"),
    path('audiodeletelist',AudioBookDeleteListView.as_view(),name="audiodeletelist"),
    path('podcast',PodcastCreateView.as_view(),name="podcastcreate"),
    path('podcastedit/<int:pk>',PodcastEditView.as_view(),name="podcast_edit"),
    path('podcastdelete/<int:pk>',PodcastDeleteView.as_view(),name="podcast_delete"),
    path('podcastdetail/<int:pk>',PodcastDetailView.as_view(),name="podcast_detail"),
    path('podcastlist',PodcastListView.as_view(),name="podcastlist"),
    path('podcasteditlist',PodcastEditListView.as_view(),name="podcasteditlist"),
    path('podcastdeletelist',PodcastDeleteListView.as_view(),name="podcastdeletelist"),
]