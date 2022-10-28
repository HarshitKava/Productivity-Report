from django.urls import path
from . import views
urlpatterns = [
    path('HomeMang/', views.HomeMangProRepo,name="HomeMangProRepo"),

    path('HomeAdmin/', views.HomeAdminProRepo,name="HomeAdminProRepo"),
    path('Activity/', views.Activity,name="AddActivity"),
    path('Structure/', views.AddStructure,name="AddStructure"),
    path('ajax-load-ProRepo-Labour/', views.load_ProRepo_labour,name="ajax_load_ProRepo_labour"),
    path('ajax-load-Category/', views.load_category,name="ajax_load_category"),

    path('HomeSE/', views.HomeSEProRepo,name="HomeSEProRepo"),
    path('SEAddProRepo/', views.SEAddProRepo,name="SEAddProRepo"),
    path('SEViewDayProRepo/', views.SEViewDayProRepo,name="SEViewDayProRepo"),
    path('SEDelDayProRepo/<int:i>/', views.SEDelDayProRepo,name="SEDelDayProRepo"),
    path('SEAddNightProRepo/', views.SEAddNightProRepo,name="SEAddNightProRepo"),
    path('SEViewNightProRepo/', views.SEViewNightProRepo,name="SEViewNightProRepo"),
    path('SEDelNightProRepo/<int:i>/', views.SEDelNightProRepo,name="SEDelNightProRepo"),
]