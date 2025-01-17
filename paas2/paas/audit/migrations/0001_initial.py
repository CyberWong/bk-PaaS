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

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditEventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('system', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('op_time', models.DateTimeField(auto_now_add=True)),
                ('op_type', models.CharField(max_length=32, choices=[(1, '\u67e5\u8be2'), (2, '\u521b\u5efa'), (3, '\u5220\u9664'), (4, '\u4fee\u6539')])),
                ('op_object_type', models.CharField(max_length=32)),
                ('op_object_id', models.CharField(max_length=64, null=True, blank=True)),
                ('op_object_name', models.CharField(max_length=64, null=True, blank=True)),
                ('data_before', models.TextField(null=True, blank=True)),
                ('data_after', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'audit_event_log',
                'verbose_name': '\u64cd\u4f5c\u5ba1\u8ba1\u65e5\u5fd7',
                'verbose_name_plural': '\u64cd\u4f5c\u5ba1\u8ba1\u65e5\u5fd7',
            },
        ),
    ]
