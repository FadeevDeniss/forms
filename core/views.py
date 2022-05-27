from django.http import JsonResponse
from django.shortcuts import render
from modernrpc.core import rpc_method
from rest_framework.parsers import JSONParser

from core.models import CustomForm, FormFields
from core.serializers import FormSerializer, FieldSerializer


class FormName:
    pass


@rpc_method(entry_point='rpc')
def form_api(request, id=0):
    if request.method == 'POST':
        form_data = JSONParser().parse(request)
        form_serializer = FormSerializer(data=form_data)
        if form_serializer.is_valid():
            form_serializer.save()
            return JsonResponse('Success', safe=False)
        return JsonResponse('Error occured while adding field', safe=False)

    elif request.method == 'PUT':
        form_data = JSONParser().parse(request)
        form = CustomForm.objects.get(form_id=form_data['form_id'])
        form_serializer = FormSerializer(form, data=form_data)
        if form_serializer.is_valid():
            form_serializer.save()
            return JsonResponse('Success', safe=False)
        return JsonResponse('Error occured while updating field', safe=False)

    elif request.method == 'DELETE':
        form = CustomForm.objects.get(form_id=id)
        form.delete()
        return JsonResponse('Success', safe=False)


@rpc_method(entry_point='rpc')
def field_api(request, id=0):
    if request.method == 'POST':
        field_data = JSONParser().parse(request)
        field_serializer = FieldSerializer(data=field_data)
        if field_serializer.is_valid():
            field_serializer.save()
            return JsonResponse('Success', safe=False)
        return JsonResponse('Error occured while adding field', safe=False)

    elif request.method == 'PUT':
        field_data = JSONParser().parse(request)
        fields = FormFields.objects.get(field_id=field_data['field_id'])
        field_serializer = FieldSerializer(fields, data=field_data)
        if field_serializer.is_valid():
            field_serializer.save()
            return JsonResponse('Success', safe=False)
        return JsonResponse('Error occured while updating field', safe=False)

    elif request.method == 'DELETE':
        fields = FormFields.objects.get(field_id=id)
        fields.delete()
        return JsonResponse('Success', safe=False)
