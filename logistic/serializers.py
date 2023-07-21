from rest_framework import serializers

from .models import Product, Stock, StockProduct


# 1. Сериалайзер: ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


# 2. Сериалайзер (Дополнительный - для вывода): ProductPositionSerializer
class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


# 3. Сериалайзер: StockSerializer
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    positions = ProductPositionSerializer(many=True)

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for pos in positions:
            StockProduct.objects.create(stock=stock, **pos)
        return stock


    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        stock.positions.all().delete()
        for pos in positions:
            StockProduct.objects.create(stock=stock, **pos)
        return stock

