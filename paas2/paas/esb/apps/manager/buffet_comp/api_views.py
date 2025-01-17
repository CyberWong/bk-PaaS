# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS
Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.views.generic import View

from common.decorators import has_apigateway_manage_permission_for_classfunc
from esb.bkcore.models import ESBBuffetMapping
from esb.common.django_utils import JsonResponse, get_error_prompt
from .forms import ESBBuffetMappingForm, EditESBBuffetMappingForm


class APIBuffetMappingView(View):
    """Check All Mappings"""

    @has_apigateway_manage_permission_for_classfunc
    def get(self, request, item_id):
        obj = ESBBuffetMapping.objects.get(pk=item_id)
        return JsonResponse({"error_message": None, "data": obj.get_info()})

    @has_apigateway_manage_permission_for_classfunc
    def post(self, request):
        form = ESBBuffetMappingForm(request.POST)
        if form.is_valid():
            obj = ESBBuffetMapping(**form.cleaned_data)
            obj.save()
            return JsonResponse({"error_message": None, "data": obj.get_info()})

        return JsonResponse(
            {
                "error_message": get_error_prompt(form),
                "data": None,
            }
        )

    @has_apigateway_manage_permission_for_classfunc
    def put(self, request, item_id):
        from django.http import QueryDict

        put = QueryDict(request.body)
        form = EditESBBuffetMappingForm(put)

        if form.is_valid():
            obj = ESBBuffetMapping.objects.get(pk=form.cleaned_data["id"])
            obj.__dict__.update(form.cleaned_data)
            obj.save()
            return JsonResponse({"error_message": None, "data": obj.get_info()})

        return JsonResponse(
            {
                "error_message": get_error_prompt(form),
                "data": None,
            }
        )

    @has_apigateway_manage_permission_for_classfunc
    def delete(self, request, item_id):
        obj = ESBBuffetMapping.objects.get(pk=item_id)
        obj.delete()
        return JsonResponse({"error_message": None, "data": None})
