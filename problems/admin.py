from django.contrib import admin
from problems.models import Problems, ProblemDetail, Example, BackTestExample


class ExampleAdmin(admin.TabularInline):
    model = Example
    fields = ('inputData', 'outputData')
    extra = 1

class  BackTestExampleAdmin(admin.TabularInline):
    model = BackTestExample
    fields = ('inputData', 'outputData')
    extra = 1

class ProblemDetailAdmin(admin.TabularInline):
    model = ProblemDetail
    fields = ('desc', )

@admin.register(Problems)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty')
    inlines = [ProblemDetailAdmin, ExampleAdmin, BackTestExampleAdmin]
    
