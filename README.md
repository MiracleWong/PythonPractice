# PythonPractice
学习Python时，练手的例程！
目前的练手的例程是[菜鸟教程](https://www.runoob.com/)提供的[Python 100例](https://www.runoob.com/python/python-100-examples.html)

# Windows 10 安装pip
```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip -V
```

# Windows 10 设置pip源
在c:\user(或者用户)\电脑的用户名\，目录下创建一个命名为“pip”的文件夹（如：C:\Users\Administrator\pip），在该文件夹下创建一个命名为“pip.ini”的文件，在该文件中写入以下内容：
```shell
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple 
[install]  
trusted-host=pypi.tuna.tsinghua.edu.cn
disable-pip-version-check = true  
timeout = 6000
```

若是想在安装package的时候再设置源，可以以这种方式来进行：

```shell
pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Todo
- [Python 练习册，每天一个小程序](https://github.com/Yixiaohan/show-me-the-code)
- [Python 的练手项目有哪些值得推荐？](https://www.zhihu.com/question/29372574)
- [python小练习：一日一练](http://bbs.fishc.com/forum.php?mod=collection&action=view&ctid=503)