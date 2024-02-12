"""
URL configuration for construction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from constructionapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('userregister/',views.userregister),
    path('workerregister/',views.workerregister),
    path('contractorregister/',views.contractorregister),
    path('login/',views.login),
    path('contractorhome/',views.contractorhome),
    path('userhome/',views.userhome),
    path('workerhome/',views.workerhome),
    path('admin1/',views.admin1),
    path('userviewcontractor/',views.userviewcontractor),
    path('userviewprofile/',views.userviewprofile),
    # path('updateuser/',views.updateuser),
    path('deletecontractor/',views.deletecontractor),
    path('workerviewprofile/',views.workerviewprofile),
    path('contractorviewprofile/',views.contractorviewprofile),
    path('adminviewcontractor/',views.adminviewcontractor),
    path('actioncontractor/',views.actioncontractor),
    path('delete1/',views.delete1),
    path('adminviewworker/',views.adminviewworker),
    path('actionworker/',views.actionworker),
    path('adminviewuser/',views.adminviewuser),
    path('userrequestwork/',views.userrequestwork),
    path('contractorviewuserrequest/',views.contractorviewuserrequest),
    path('userrequestaction/',views.userrequestaction),
    path('userviewstatus/',views.userviewstatus),
    path('contractorviewworker/',views.contractorviewworker),
    # path('allotwork/',views.allotwork),
    path('workerviewassignedwork/',views.workerviewassignedwork),
    path('assignedaction/',views.assignedaction),
    path('contractorviewwork/',views.contractorviewwork),
    path('userfeedback/',views.userfeedback),
    path('workerfeedback/',views.workerfeedback),
    path('workerviewfeedback/',views.workerviewfeedback),
    path('contractorviewfeedback/',views.contractorviewfeedback),
    path('userpayment/',views.userpayment),
    path('userviewpayment/',views.userviewpayment),
    path('contractorpayment/',views.contractorpayment),
    path('contractorviewpayment/',views.contractorviewpayment),
    path('adminviewfeedback/',views.adminviewfeedback),
    path('viewworker/',views.viewworker),
    path('workerviewcontractor/',views.workerviewcontractor),
    path('logout/',views.logout),
]
