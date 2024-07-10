from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.request.query_params.get('city_id')
        if city_id:
            return self.queryset.filter(city_id=city_id)
        return self.queryset

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def filter_shops(self, request):
        street = request.query_params.get('street')
        city = request.query_params.get('city')
        open_param = request.query_params.get('open')

        queryset = self.queryset
        if street:
            queryset = queryset.filter(street__name=street)
        if city:
            queryset = queryset.filter(city__name=city)
        if open_param is not None:
            from datetime import datetime
            current_time = datetime.now().time()
            if open_param == '1':
                queryset = queryset.filter(opening_time__lte=current_time, closing_time__gte=current_time)
            else:
                queryset = queryset.filter(opening_time__gt=current_time) | queryset.filter(closing_time__lt=current_time)
        return Response(self.serializer_class(queryset, many=True).data)
