from .models import CustomerOrder
from restaurants.models import Restaurant
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import CustomerOrderSerializer
from datetime import datetime, date
from rest_framework import serializers
from django.db.models import Sum
from middleware.user_group_validation import is_customer, is_staff
from middleware.enums.meal_times_enum import meal_times
import json


# Customer Order ViewSet
class CustomerOrderViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CustomerOrderSerializer

    def get(self, request):
        if not is_customer(request.user):
            raise serializers.ValidationError("Access Denied: You are not a customer")

        orders_objs = CustomerOrder.objects.filter(customer=request.user.id)
        orders = []

        for obj in orders_objs:
            order = obj.__dict__
            order.pop('_state')
            order['total_price'] = float(str(order['total_price']))
            orders.append(order)

        return Response({"orders": orders})

    def post(self, request, *args, **kwargs):
        if not is_staff(request.user, 4):
            raise serializers.ValidationError("Access Denied: You are not a virtual waiter")

        data = request.data
        data['customer'] = User.objects.filter(username=data['customer'])[0].id

        data['id'] = CustomerOrder.objects.order_by('-id')[0].id + 1

        data['menu_items'] = json.dumps(data['menu_items'])
        data['special_offers'] = json.dumps(data['special_offers'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        return Response({
            "order": CustomerOrderSerializer(order, context=self.get_serializer_context()).data
        })


# View Set to get the available reservations for today
# class GetTodayTableReservationsViewSet(generics.GenericAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = TableReservationSerializer
#
#     def get(self, request):
#         if not is_staff(request.user, 3):
#             raise serializers.ValidationError("Access Denied: You are not a waiter")
#
#         today = datetime.now().date()
#         time_now = datetime.now().time()
#
#         breakfast_begin = time_now.replace(hour=6, minute=0, second=0, microsecond=0)
#         breakfast_end = time_now.replace(hour=10, minute=30, second=0, microsecond=0)
#         lunch_begin = time_now.replace(hour=12, minute=0, second=0, microsecond=0)
#         lunch_end = time_now.replace(hour=15, minute=30, second=0, microsecond=0)
#         dinner_begin = time_now.replace(hour=19, minute=30, second=0, microsecond=0)
#         dinner_end = time_now.replace(hour=22, minute=30, second=0, microsecond=0)
#
#         if breakfast_begin <= time_now <= breakfast_end:
#             table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=meal_times[0][0])
#         elif lunch_begin <= time_now <= lunch_end:
#             table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=meal_times[1][0])
#         elif dinner_begin <= time_now <= dinner_end:
#             table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=meal_times[2][0])
#         else:
#             raise serializers.ValidationError("No Meal Provided at this Time.")
#         table_reservations = []
#
#         for obj in table_reservations_objs:
#             reservation = obj.__dict__
#             reservation.pop('_state')
#             table_reservations.append(reservation)
#
#         return Response({"table_reservations": table_reservations})
#
#
# # View Set to get update customer arrival
# class TableReservationArrivalViewSet(generics.GenericAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = TableReservationSerializer
#
#     def post(self, request, *args, **kwargs):
#         if not is_staff(request.user, 3):
#             raise serializers.ValidationError("Access Denied: You are not a waiter")
#
#         data = request.data
#         reservation_id = data['reservation_id']
#
#         try:
#             reservation = TableReservation.objects.get(id=reservation_id, customer=request.user.id)
#         except TableReservation.DoesNotExist:
#             raise serializers.ValidationError("Invalid Access")
#
#         if datetime.now().date() == reservation.reserved_date:
#             reservation.customer_arrival = True
#             reservation.save()
#         else:
#             raise serializers.ValidationError("Today is not the Reserved Date.")
#
#         return Response({
#             "room_reservation": TableReservationSerializer(reservation, context=self.get_serializer_context()).data
#         })
#
#
# def is_fully_booked(restaurant, reserved_date, meal_time, num_of_people):
#     try:
#         restaurant_max_people = Restaurant.objects.filter(id=restaurant)[0].max_number_of_people_for_reservation
#     except IndexError:
#         raise serializers.ValidationError('Invalid Restaurant')
#
#     prev_reservations = TableReservation.objects.filter(restaurant=restaurant, reserved_date=reserved_date, meal_time=meal_time).aggregate(Sum('num_of_people'))['num_of_people__sum']
#
#     if prev_reservations and restaurant_max_people >= prev_reservations + num_of_people:
#         return False
#     elif restaurant_max_people >= num_of_people:
#         return False
#     return True
#
#
# def is_meal_time_served_by_restaurant(restaurant, meal_time):
#     if meal_time == 'breakfast':
#         return Restaurant.objects.filter(id=restaurant)[0].breakfast
#     elif meal_time == 'lunch':
#         return Restaurant.objects.filter(id=restaurant)[0].lunch
#     elif meal_time == 'dinner':
#         return Restaurant.objects.filter(id=restaurant)[0].dinner
#     else:
#         raise serializers.ValidationError("Invalid Meal Time")