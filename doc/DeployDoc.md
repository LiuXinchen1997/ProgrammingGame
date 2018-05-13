# 项目部署文档

## 1 前端部署

1. 将根目录中的**package.json**文件放到**CodeGame/frontend**目录下。
1. 在**CodeGame/frontend**目录下使用`cnpm install`安装JS依赖包。额外需要安装的JS包包括：
    1. **vue-router**
    1. **element-ui**
    1. **axios**
    1. 后期开发还引入了很多其他包，这里并不一一列出了，具体见**package.json**。
1. 在**CodeGame/frontend**目录下添加**build**目录用于存放若干build配置文件。
1. 使用`npm run build`生成发布目录dist。
1. 使用`npm run dev`运行Vue服务器，进入开发者模式。

## 2 后端部署

1. 使用`pip install django`或`conda install django`安装Django。
1. 使用`pip install django-cors-headers`安装django-cors-headers包实现跨域访问。
1. 使用`mysql -uroot -p<密码> jisuanke < jisuanke.sql`运行项目sql文件创建数据库与数据库对象。
1. 在**/HFUT_Group3/CodeGame/CodeGame/settings.py**文件内修改以下内容，并将其添加到CodeGame/CodeGame目录下。

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'jisuanke',
            'USER': 'root',
            'PASSWORD': '<你的密码>',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

1. 在**/HFUT_Group3/CodeGame/CodeGame/__init__.py**文件内添加以下内容：

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

1. 使用`python manage.py inspectdb > <APP名称>/models.py`将数据库导入models文件。
1. 使用`python manage.py runserver`运行项目。

## 3 访问项目

1. 打开浏览器，输入`http://localhost:8080/`即可正常访问项目。
