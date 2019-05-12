## 说明
12306_ticket_inquiry
django+selenium 实现12306车票查询接口,后面会实现web可视化页面,登陆抢票接口

## 注意
运行前先要获取城市,城市对应编号
手动运行下get_12306_city.py文件，生成对应的城市编号字典


## 项目主要结构
```
├── app01
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── selenium
│   │   ├── city_number.txt
│   │   ├── get_12306_city.py
│   │   ├── query_tick_12306.py
│   │   └── resource.py
│   ├── tests.py
│   ├── utils
│   │   └── throttle.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── object_12306
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── templates


```

## 运行环境WIN
| Project | version | Description |
|---------|--------|-------------|
| python  | 3.6.8 | 无 |



## 需要用到的第三方库
selenium   pip3 install selenium   
selenium的使用需要安装谷歌驱动chromedriver.exe，要与本地浏览器的版本一致
下载地址: https://npm.taobao.org/mirrors/chromedriver/


```
	Django==2.2.1
	djangorestframework==3.9.4
	
```





## 模块说明
```
	1. selenium
	   基于JS渲染的页面爬取
	   
	
	2. django rest framework
		提供接口
	
```


## 备注
python3技术交流群198447500


Copyright (c) 2019-present, Run