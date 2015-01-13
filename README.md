# SAETornado
SAE+Tornado+sqlalchemy的示例代码

搭建环境
--------

  $ pip install -r requirements.txt

配置MySQL
---------

1. settings.py修改db_*的赋值
2. 完善models.py的模型映射

本地调试
--------

  $ python runserver.py

> 端口8000

部署上线
--------

注意修改config.yaml里的应用名和应用版本
