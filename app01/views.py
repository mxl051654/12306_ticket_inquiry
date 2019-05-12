from django.shortcuts import render
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from app01.selenium import query_tick_12306
import json, time, os
# Create your views here.


class RestApiView(APIView):
    versioning_class = QueryParameterVersioning

    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": 200})

    def post(self, request, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, 'selenium', 'city_number.txt')
        start_city = request.data.get('start_city').strip()
        end_city = request.data.get('end_city').strip()
        start_time = request.data.get('start_time').strip()
        now_time = self.now_time()
        # 判断时间是否过期
        if now_time > start_time:
            return JsonResponse({"status": "error", "message": "过期时间"})

        with open(file_path, encoding='utf-8', mode='r') as f:
            city_number_dict = json.loads(f.read())
            # print(city_number_dict)
            # 判断城市是否在对应字典里面
            if start_city in city_number_dict and end_city in city_number_dict:
                url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={},{}&ts={},{}&date={}&flag=N,N,Y'.\
                    format(start_city, city_number_dict.get(start_city),
                           end_city, city_number_dict.get(end_city),
                           start_time)
                st = query_tick_12306.QueryTicket()
                ret = st.main(url)
                return JsonResponse(ret)
            else:
                return JsonResponse({"status": "error", "message": "城市错误"})

    def now_time(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))
