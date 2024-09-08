travel_route_prompt = """请根据以下说明从文本中抽取旅行相关的实体，并以JSON格式返回结果。请确保所有实体类别都符合下列定义和格式要求。

对【文本】进行实体抽取，实体类别包括：【城市】、【景点】、【住宿】、【餐厅】、【必备APP】、【旅行路线】。实体类别的定义参考【key映射及定义】。

抽取结果用JSON格式返回，JSON中的list允许为空，参考【示例格式】。

【key映射及定义】
【城市】：city，列表，文本中的城市名称，用于行程的目的地推荐。限定为城市级别，如果文本中没有提到城市，可提取相应的地理单位（如国家、省份或地区名称）。
【景点】：location，字典，城市名为键，值为文本中提到的该城市景点名称。
【住宿】：accommodation，字典，城市名为键，值为文本中提到的该城市酒店或民宿名称。
【餐厅】：restaurant，字典，城市名为键，值为文本中提到的该城市餐厅名称或推荐菜名称。
【必备APP】：app_recommend，列表，文本中的APP名称，用于出行APP推荐。
【旅行路线】：itinerary，列表，文本中明确的旅行路线。列表应包含多个行程安排的子列表，每个子列表代表一天的行程安排或一个完整路线的行程安排。每个子列表中的元素是一个字典，字典的键是城市名，字典的值是该城市中具体的景点、餐厅、酒店名称。若文本中无明确的行程路线，可返回空列表。

【示例格式】
```json
{
    "city": [],
    "location": {
        "city_name1": [],
        "city_name2": []
    },
    "accommodation": {
        "city_name1": [],
        "city_name2": []
    },
    "restaurant": {
        "city_name1": [],
        "city_name2": []
    },
    "app_recommend": [],
    "itinerary": [
        [
            {"city_name": "location_name"},
            {"city_name": "restaurant_name"},
            {"city_name": "accommodation_name"}
        ],
        [
            {"city_name": "location_name"},
            {"city_name": "restaurant_name"},
            {"city_name": "accommodation_name"}
        ]
    ]
}
```

如果【文本】不是旅游相关的内容，例如讨论的是日常生活或科技新闻，请返回空json。空json格式如下：
```json
{}
```

【文本】
"""