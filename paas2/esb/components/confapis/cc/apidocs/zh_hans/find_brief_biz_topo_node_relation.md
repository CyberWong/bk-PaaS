### 功能描述

该接口用于根据业务拓扑中的某一个层级(模型)的实例，查询与其直接相关联的上、下层级(模型)的简明关系信息。(v3.10.1+)


若业务拓扑层级自上而下分别为业务、部门(自定义业务层级)、集群、模块。则：


1. 向上可查询某集群所属的直接上级**部门**的关系信息；


2. 向下可查询该集群所直接关联的模块关系信息。


反过来，不可通过部门直接查询自定义层级实例**某部门**下所包含的模块关系，因为部门与模块不是直接关联关系。


### 请求参数

{{ common_args_desc }}

#### 接口参数

| 字段      |  类型      | 必选   |  描述      |
|-----------|------------|--------|------------|
| src_biz_obj  | string  | 是     | 业务层级中，源层级的模型ID，可以分别为"biz"、自定义层级模型ID(bk_obj_id)、"set"、"module"。 |
| src_ids  | array  | 是     |  src_biz_obj 所代表的实例ID列表，列表长度范围为[1,200]|
| dest_biz_obj  | string  | 是     | 与src_biz_obj**直接(紧临)**相关联的业务层级模型。其中业务("biz")
为例外，任意的src_biz_obj的dest_biz_obj都可以是"biz"。但二者不允许相同。|
| page  | object  | 是     |  查询到的数据返回的分页配置信息|

#### page 字段说明

| 字段  | 类型   | 必选 | 描述                  |
| ----- | ------ | ---- | --------------------- |
| start | int    | 是   | 记录开始位置，从0开始         |
| limit | int    | 是   | 每页限制条数,最大500 |
| sort | string    | 不可用   | 该字段，在接口内默认按被关联(dest_biz_obj)的身份ID进行排序，请勿设置此字段 |



### 请求参数示例

```json
{
    "bk_app_code": "xxx",
    "bk_app_secret": "xxx",
    "bk_username": "xxx",
    "bk_token": "xxx",
    "src_biz_obj": "biz",
    "src_ids":[3,302],
    "dest_biz_obj":"nation",
    "page":{
        "start": 0,
        "limit": 2
    }
}
```

### 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "message": "success",
    "permission": null,
    "request_id": "e43da4ef221746868dc4c837d36f3807",
    "data":
    [
        {
            "bk_biz_id": 3,
            "src_id": 3,
            "dest_id": 3812
        },
        {
            "bk_biz_id": 302,
            "src_id": 302,
            "dest_id": 3813
        }
    ]
}
```

### 返回结果参数说明

#### response

| 名称    | 类型   | 描述                                    |
| ------- | ------ | ------------------------------------- |
| result  | bool   | 请求成功与否。true:请求成功；false请求失败 |
| code    | int    | 错误编码。 0表示success，>0表示失败错误    |
| message | string | 请求失败返回的错误信息                    |
| permission    | object | 权限信息    |
| request_id    | string | 请求链id    |
| data    | object | 请求返回的数据                           |

#### data说明
| 字段      |  类型      |  描述      |
|-----------|------------|------------|
| bk_biz_id | int   | 该实例所属的业务ID     |
| src_id | int   | 与入参中的src_ids输入的ID列表一致。代表的是入参查询模型的实例ID |
| dest_id | int| 与入参中的dest_biz_obj对应的模型且与src_ids对应的实例直接关联的实例ID |

注：

1. 若是向下查询（由向层级向低层级查询）判断分页拉取完数据的方式为返回的data数组列表为空。


2. 若是向上查询（由低层级向高层级查询），该接口可一次返回所有查询结果，条件为page.limit的值要>=src_ids的长度。
