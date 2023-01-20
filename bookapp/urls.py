from django.urls import path
from .views import * 


urlpatterns = [
    path('home/',index,name="home"),
    path('add/',add_books, name="add"),
    path('view/',view_books, name="view"),
    path('delete/',delete_books, name="del"),
    path('search/',search_book, name="search"),
    path('upd/<int:id>',upd_books, name="upd"),
]

# class UserEditView(generic.UpdateView):
#     model = Profile
#     form_class = EditProfileForm
#     template_name = "editP.html"
#     success_url = reverse_lazy('home')
    
#     def get_object(self):
#         return self.request.user