### 功能描述

更新混合版本信息

### 请求参数

{{ common_args_desc }}

#### 接口参数

| 字段             |  类型     | 必选   |  描述   |
|------------------|-----------|--------|---------|
| biz_id           |  string   | 是     | 业务ID  |
| app_id           |  string   | 是     | 应用ID     |
| multi_release_id |  string   | 是     | 混合版本ID |
| memo             |  string   | 是     | 备注 (max_length: 256) |

### 请求参数示例

```json
{
    "bk_app_code": "xxx",
    "bk_app_secret": "xxx",
    "bk_token": "xxx",
    "biz_id": "xxx",
    "app_id": "A-0b67a798-e9c1-11e9-8c23-525400f99278",
    "multi_release_id": "MR-0b67a798-e9c1-11e9-8c23-525400f99278",
    "name": "release-01",
    "memo": "update my release"
}
```

### 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "message": "OK"
}
```
