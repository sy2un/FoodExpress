# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class FERestaurantItem(scrapy.Item):
    id = scrapy.Field()
    restaurant_name = scrapy.Field()         #饭店名
    address = scrapy.Field()                 #饭店地址
    open_time = scrapy.Field()               #营业时间
    description = scrapy.Field()             #说明
    deliver_fee = scrapy.Field()             #送餐费用
    deliver_min_money = scrapy.Field()       #最少起送餐费
    platform_id = scrapy.Field()             #平台ID
    platform_restaurant_id = scrapy.Field()  #平台饭店ID
    latitude = scrapy.Field()                #经度
    longitude = scrapy.Field()               #纬度
    search_place_id = scrapy.Field()         #搜索
    distance = scrapy.Field()                #距离地点

    def get_insert_sql(self):
        insert_sql = """insert into fe_restaurant(restaurant_name,description,address,deliver_fee,deliver_min_money,platform_id,platform_restaurant_id,latitude,longitude)
         value ('%s','%s','%s','%f','%f','%d','%d','%f','%f')"""
        params = (self["restaurant_name"],  self["description"],self["address"], self["deliver_fee"], self["deliver_min_money"],
                  self["platform_id"],self["platform_restaurant_id"], self["latitude"], self["longitude"])
        return insert_sql, params



class FEPlaceRestaurant(scrapy.Item):
    search_place_id = scrapy.Field()         #查询地点
    restaurant_id = scrapy.Field()           #饭店ID
    distance = scrapy.Field                  #饭店距离查询点距离


class FEFoodCategoryItem(scrapy.Item):
    id = scrapy.Field()
    platform_category_id = scrapy.Field()
    platform_id = scrapy.Field()
    category_name = scrapy.Field()
    restaurant_id = scrapy.Field()

    def get_insert_sql(self):

        insert_sql = """insert into fe_food_category(platform_category_id,platform_id,category_name,restaurant_id)
         value ('%d','%d','%s','%d')"""
        params = (self["platform_category_id"],  self["platform_id"],self["category_name"],self["restaurant_id"])
        return insert_sql, params

class FEFoodItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()                  #价钱
    platform_category_id = scrapy.Field()   #平台类别ID
    platform_food_id = scrapy.Field()
    category_name = scrapy.Field()          #平台类别名称
    description = scrapy.Field()            #备注
    month_sales = scrapy.Field()            #月销售
    rating_count = scrapy.Field()           #评论数量
    rating = scrapy.Field()                 #评价星
    restaurant_id = scrapy.Field()          #饭店ID
    platform_id = scrapy.Field()            #平台ID

    def get_insert_sql(self):
        insert_sql = """insert into fe_food(name,price,platform_category_id,platform_food_id,description,month_sales,rating_count,rating,restaurant_id,platform_id)
         value ('%s','%f','%d','%d','%s','%d','%d','%f','%d','%d')"""
        params = (self["name"],  self["price"],self["platform_category_id"], self["platform_food_id"],self["description"], self["month_sales"],
                  self["rating_count"],self["rating"], self["restaurant_id"], self["platform_id"])
        return insert_sql, params

class FERestaurantOrder(scrapy.Item):
    id = scrapy.Field()
    restaurant_id = scrapy.Field()                  #饭店ID
    order_time = scrapy.Field()                     #评价时间，饿了么这里是用评价接口获取的订单信息，将评价时间作为订单时间
    rating = scrapy.Field()                         #评价星数
    time_spent = scrapy.Field()                     #订单送达花费时间

    def get_insert_sql(self):
        insert_sql = """insert into fe_restaurant_order(restaurant_id,order_time,rating,time_spent)
         value ('%d','%s','%d','%d')"""
        params = (self["restaurant_id"],  self["order_time"],self["rating"], self["time_spent"])
        return insert_sql, params

class FEOrderFood(scrapy.Item):
    id = scrapy.Field()
    food_id = scrapy.Field()                  #商品ID
    order_id = scrapy.Field()                     #订单ID


    def get_insert_sql(self):
        insert_sql = """insert into fe_order_food(food_id,order_id)
         value ('%d','%d')"""
        params = (self["food_id"],  self["order_id"])
        return insert_sql, params


class FEPlatform(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()                   #平台名
    description = scrapy.Field()            #说明

    def get_insert_sql(self):
        insert_sql = """insert into fe_food(name,price,description,category_id,month_sales,rating_count,rating,restaurant_id,platform_id)
         value ('%s','%f','%s','%d','%d','%d','%f','%d','%d')"""
        params = (self["name"],  self["price"],self["description"], self["category_id"], self["month_sales"],
                  self["rating_count"],self["rating"], self["restaurant_id"], self["platform_id"])
        return insert_sql, params

class FESearchPlace(scrapy.Item):
    id = scrapy.Field()
    city = scrapy.Field()                   #城市
    place = scrapy.Field()                  #搜索地名
    latitude = scrapy.Field()               #经度
    longitude = scrapy.Field()              #纬度
    platform_id = scrapy.Field()            #平台ID


class TestItem(scrapy.Item):
    a = scrapy.Field()
    b = list()#{}

    def get_insert_sql(self):
        insert_sql = """insert into fe_order(name)
                 value ('%d')"""
        params = (self["a"])
        return insert_sql, params

    def get_insertChild_sql(self,):
        insert_sql = """insert into fe_food(foodid,orderid)
                 value ('%d','%d')"""
        return insert_sql