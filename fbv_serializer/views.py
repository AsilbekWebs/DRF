from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from products.models import Product
from rest_framework.exceptions import ValidationError
from .serializer import TestsSerializer



@api_view(['POST', "GET"])
def create_list_product(request):
    if request.method == 'POST':
        serializer = TestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'msg': 'Created',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })

        raise ValidationError({
            'error': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        })
    elif request.method == 'GET':
        products = Product.objects.all()
        serializer = TestsSerializer(products, many=True)

        return Response({
            'count': products.count(),
            'msg': 'list',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })


@api_view(['PUT', 'PATCH', "DELETE", 'GET'])
def detail_delete_update(request, pk):
    def get_object():
        product = Product.objects.filter(pk=pk).first()
        if not product:
            raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})
        return product

    if request.method == 'GET':
        product = get_object()
        serialzier = TestsSerializer(product)
        return Response({
            'msg': 'detail',
            'status': status.HTTP_200_OK,
            'data': serialzier.data
        })

    elif request.method == 'DELETE':
        product = get_object()
        product.delete()
        return Response({
            'msg': 'deleted',
            'status': status.HTTP_204_NO_CONTENT,
        })

    elif request.method == 'PUT':
        product = get_object()
        if not product:
            raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})
        serializer = TestsSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': 'Updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    elif request.method == 'PATCH':
        product = get_object()
        if not product:
            raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})
        serializer = TestsSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': 'Updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })




@api_view(['GET'])
def list_product(request):
    products = Product.objects.all()
    serializer = TestsSerializer(products, many=True)

    return Response({
        'count': products.count(),
        'msg': 'list',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })


@api_view(['GET'])
def detail_product(request, pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})

    serialzier = TestsSerializer(product)

    return Response({
        'msg': 'detail',
        'status': status.HTTP_200_OK,
        'data': serialzier.data
    })


@api_view(['POST'])
def create_product(request):
    serializer = TestsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            'msg': 'Created',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })

    raise ValidationError({
        'error': serializer.errors,
        'status': status.HTTP_400_BAD_REQUEST
    })


@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})

    serializer = TestsSerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({
        'msg': 'Updated',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })


@api_view(['PATCH'])
def update_partial_product(request, pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})

    serializer = TestsSerializer(instance=product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({
        'msg': 'Updated',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })


@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise ValidationError({'msg': 'Product not found', 'status': status.HTTP_400_BAD_REQUEST})

    product.delete()

    return Response({
        'msg': 'deleted',
        'status': status.HTTP_204_NO_CONTENT,
    })

