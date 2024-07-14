from django.contrib import admin
from .models import Certificate, Member
from import_export.admin import ImportExportModelAdmin


class AdminCertificate(ImportExportModelAdmin):
    list_display = ['cert_id','name','event','year']
    search_fields = ['name','cert_id',]
    list_filter = ('year', 'event',)
class MemberCertificateAdmin(ImportExportModelAdmin):
    list_display = ['certificate_num','name','father_name','email','year']
    search_fields = ['name','father_name','certificate_num',]
    list_filter = ('year',)


# Register your models here.
admin.site.register(Certificate, AdminCertificate)
admin.site.register(Member, MemberCertificateAdmin)

admin.site.site_header = 'Navprayas Certifications'
