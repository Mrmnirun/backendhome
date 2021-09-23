from django.urls import path, include
from .api import TableReservationViewSet, TableReservationArrivalViewSet, GetTodayTableReservationsViewSet


urlpatterns = [
    path('api/table_reservations', TableReservationViewSet.as_view()),
    path('api/table_reservations/arrival', TableReservationArrivalViewSet.as_view()),
    path('api/table_reservations/today_reservations', GetTodayTableReservationsViewSet.as_view()),
]