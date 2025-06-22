from django.urls import path

from . import views, views_customers, view_cars, views_carModels, views_bookings

urlpatterns = [
    path("", views.index, name="home"),

]

urlpatterns += [
    path("carModels/", views_carModels.car_models, name="car-models"),
    path('carModel/create/', views_carModels.CarModelCreate.as_view(), name='car-model-create'),
    path('carModel/<int:pk>/update/', views_carModels.CarModelUpdate.as_view(), name='car-model-update'),
    path('carModel/<int:pk>/delete/', views_carModels.CarModelDelete.as_view(), name='car-model-delete'),
    path('carModel/<int:pk>', views_carModels.CarModelDetailView.as_view(), name='car-model-detail'),
    path("carsOfModel/<int:model_id>/", views_carModels.cars_of_model, name="cars-of-model"),
]

urlpatterns += [
    path("cars/", view_cars.cars, name="cars"),
    path('car/create/', view_cars.CarCreate.as_view(), name='car-create'),
    path('car/<int:pk>/update/', view_cars.CarUpdate.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', view_cars.CarDelete.as_view(), name='car-delete'),
    path('car/<int:pk>', view_cars.CarDetailView.as_view(), name='car-detail'),
]

urlpatterns += [
    path("customers/", views_customers.customers, name="customers"),
    path('customer/create/', views_customers.CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', views_customers.CustomerUpdate.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', views_customers.CustomerDelete.as_view(), name='customer-delete'),
    path('customer/<int:pk>', views_customers.CustomerDetailView.as_view(), name='customer-detail'),
]

urlpatterns += [
    path("bookings/", views_bookings.bookings, name="bookings"),
    path('booking/create/', views_bookings.BookingCreate.as_view(), name='booking-create'),
    path('booking/<int:pk>/update/', views_bookings.BookingUpdate.as_view(), name='booking-update'),
    path('booking/<int:pk>/delete/', views_bookings.BookingDelete.as_view(), name='booking-delete'),
    path('booking/<int:pk>', views_bookings.BookingDetailView.as_view(), name='booking-detail'),
    path("bookingsOfCar/<int:car_id>", views_bookings.bookings_of_car, name="bookings-of-car"),
    path("bookingsOfCustomer/<int:customer_id>", views_bookings.bookings_of_customer, name="bookings-of-customer"),
]
