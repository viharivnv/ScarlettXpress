import django_filters
from mysite.myR.models import Course
#here we will create filters in order to search our courses
class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['Title', 'Status', 'courseID', 'Credits']


