"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),
    path('studentreg/',views.studentreg),
    path('parentreg/',views.studentreg),
    path('login/',views.login),
    path('adminhome/',views.adminhome),
    path('studenthome/',views.studenthome),
    path('parenthome/',views.studenthome),
    path('tutorhome/',views.tutorhome),
    path('addtutor/',views.addtutor),
    path('viewtutorad/',views.viewtutor_ad),
    path('deletetutor/',views.deletetutor),
    path('viewstudent_ad/',views.viewstudent_ad),
    path('viewparentad/',views.viewstudent_ad),
    path('Approve_student/',views.Approve_student),
    path('Approve_parent/',views.Approve_student),
    path('deletestudent_ad/',views.deletestudent_ad),
    path('deleteparentad/',views.deletestudent_ad),
    path('addbook/',views.addbook),
    path('viewbookad/',views.viewbook_ad),
    path('viewbookstu/',views.viewbook_stu),
    path('viewbookpa/',views.viewbook_stu),
    path('book_delete/',views.book_delete),
    path('edit_book/',views.edit_book),
    path('actionstudent/',views.actionstudent),
    path('actionparent/',views.actionstudent),
    path('deletestudent/',views.deletestudent),
    path('deleteparent/',views.deletestudent),
    path('viewtutorstu/',views.viewtutor_pa),
    path('viewtutorpa/',views.viewtutor_pa),
    path('selecttutor/',views.select_tutor),
    path('bookingtutor/',views.addbooking_tutor),
    path('bookingtutorst/',views.booking_tutor_st),
    path('viewbooking/',views.viewbooking_tutor),
    path('viewbookingst/',views.viewbooking_stu),
    path('viewbooking_stu/',views.viewbooking_student),
    path('viewbooking_pa/',views.viewbooking_student),
    path('actionbooking/',views.actionbooking),
    path('deletebooking/',views.deletebooking),
    path('actionbookingst/',views.actionbooking_st),
    path('deletebookingst/',views.deletebooking_st),
    path('addrequestdemo/',views.addrequest_demo),
    path('viewrequestdemo/',views.viewrequest_demo),
    path('viewrequestdemost/',views.viewrequest_demo_st),
    path('request_demo/',views.request_democlass),
    path('request_demost/',views.request_democlass_st),
    path('add_notes/',views.add_notes),
    path('view_notes_stu/',views.view_notes_stu),
    path('view_notes_tutor/',views.view_notes_tutor),
    path('edit_note/',views.edit_note),
    path('delete_note/',views.delete_note),
    path('viewprofile/',views.viewprofile),
    path('studentchat/',views.studentchat),
    path('parentchat/',views.studentchat),
    path('teacherchat/',views.teacherchat),
    path('addreview/',views.addreview),
    path('viewreview/',views.viewreview_tutor),
    path('deletereview/',views.deletereview),
    path('calculaterating/',views.calculate_average_rating),
    path('addreview_student/',views.addreview_student),
    path('addreview_parent/',views.addreview_student),
    path('viewreview_stu/',views.view_review_student),
    path('viewreview_pa/',views.view_review_student),
    path('editreview_stu/',views.edit_review_student),
    path('deletereview_stu/',views.delete_review_student),
    path('addpayment_student/',views.addpayment_student),
    path('addpaymentpa/',views.addpayment_student),
    path('addpaymentst/',views.addpayment_student),
    path('viewpayment_ad/',views.viewpayment_ad),
    path('viewpaymentpa/',views.viewpayment_ad),
    path('viewpaymentst/',views.viewpayment_ad),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
