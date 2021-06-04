from rest_framework.decorators import api_view
from .serializers import CommentSerializer, PictureSerialiser
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def simple_request(request):
    phone = request.data['phone']
    email = request.data['email']
    comment = request.data['comment']
    # валидация телефона и email происходит в сериализаторе
    if 'http' in comment:
        raise ValidationError(['Комментарий не должен содержать ссылок.'])
    data = {'phone': phone, 'email': email, 'comment': comment}
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # я бы тут использовал статус 201, но по ТЗ нужен 200
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['POST'])
def image_request(request):
    image = request.data['image']
    data = {'image': image}
    serializer = PictureSerialiser(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
