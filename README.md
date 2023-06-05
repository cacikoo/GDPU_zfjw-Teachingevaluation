# 新版正方教务系统教学质量评价自动脚本

使用python selenium4在edge浏览器上模拟点击，可绕过正方教务系统的js自动化检测。

``本脚本只在广东药科大学新版正方教务系统上经过测试，其他学校请自行测试修改脚本``

## 1.准备工作

1.下载 ``main.py``

2.使用编辑工具打开``main.py``

3.在``user``和``pwd``中输入自己的学号和密码

4.自己在浏览器登录并打开教学评价页面，复制网址栏中的网址到``url2``中

## 2.安装依赖

方法1（建议）

```sh
pip install -r requirements.txt
```

方法2

```sh
pip install selenium webdriver_manager
```

## 3.启动

直接运行，第一次运行会自动下载自动化程序

```sh
python main.py
```
