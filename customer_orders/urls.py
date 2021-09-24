from django.urls import path, include
from .api import CustomerOrderViewSet


urlpatterns = [
    path('api/order', CustomerOrderViewSet.as_view()),
    # path('api/table_reservations/arrival', TableReservationArrivalViewSet.as_view()),
    # path('api/table_reservations/today_reservations', GetTodayTableReservationsViewSet.as_view()),
]