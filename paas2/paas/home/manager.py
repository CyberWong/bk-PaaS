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

from __future__ import unicode_literals

from django.db import models

from home.constants import LinkTypeEnum


class UserAppsManager(models.Manager):
    pass


class UsefulLinksManager(models.Manager):
    def get_light_app_or_none(self, code):
        try:
            return self.get(id=int(code[1:]), link_type=LinkTypeEnum.LIGHT_APP.value)
        except Exception:
            return None

    def is_useful_link(self, code):
        try:
            return True, self.get(id=int(code[1:]))
        except Exception:
            return False, None

    def get_common_links(self):
        return self.filter(is_active=True, link_type=LinkTypeEnum.COMMON.value)
