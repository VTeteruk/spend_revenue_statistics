from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from spend.models import SpendStatistic


@api_view(["GET"])
def spend_statistics(request) -> Response:
    """Display full information about spent money and amount of impressions, clicks, ect."""
    queryset = SpendStatistic.objects.values("name", "date").annotate(
        spent=Sum("spend"),
        impressions=Sum("impressions"),
        clicks=Sum("clicks"),
        conversion=Sum("conversion"),
        revenue=Sum("revenue__revenue"),
    )

    return Response(queryset)
