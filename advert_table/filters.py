from django_filters import FilterSet, CharFilter, DateFilter
from django.forms import DateInput
from .models import Comments

class CommentFilter(FilterSet):
# добавлю виджет для ввода даты
    time_creation = DateFilter(
        lookup_expr='gt',
        widget = DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Comments
        fields = {
            'from_user': ['exact'],
            'to_post': ['exact'],
        }
