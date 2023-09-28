from django.db.models import Sum, F
from rest_framework.decorators import api_view
from rest_framework.response import Response

from revenue.models import RevenueStatistic


@api_view(["GET"])
def revenue_statistics(request) -> Response:
    """Display full information about spent money, profit and amount of impressions, clicks, ect."""
    queryset = RevenueStatistic.objects.values("name", "date").annotate(
        revenue=Sum("revenue"),
        spent=Sum("spend__spend"),
        impressions=Sum("spend__impressions"),
        clicks=Sum("spend__clicks"),
        conversion=Sum("spend__conversion"),
        profit=F("revenue") - F("spent")
    )

    return Response(queryset)
