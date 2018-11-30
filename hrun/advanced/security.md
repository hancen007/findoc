# 信息安全
## 背景
很多时候项目代码在运行时需要使用到账号、密码、key等敏感数据信息，但是从信息安全的角度考虑，我们是不能将这些敏感数据提交到代码仓库的，主要原因有两个：

加强权限管控：参与项目的开发人员可能会有很多，大家都有读取代码仓库的权限，但是像 key 这类极度敏感的信息不应该所有人都有权限获取；
减少代码泄漏的危害性：假如代码出现泄漏，敏感数据信息不应该也同时泄漏。
## 解决方案
那代码部署到服务器或 Jenkins 执行机后，运行时要使用到这些敏感数据信息，该怎么操作呢？

推荐的操作方式为：

对服务器进行权限管控，只有运维人员（或者核心开发人员）才有登录服务器的权限；
运维人员（或者核心开发人员）：在运行的机器上将敏感数据设置到系统的环境变量中；
普通开发人员：只需要知道敏感信息的变量名称，在代码中通过读取环境变量的方式获取敏感数据。
## 存储敏感数据
将敏感数据设置到系统的环境变量中，传统的方式为使用 export 命令：

```
$ export UserName=admin
$ echo $UserName
admin
$ export Password=123456
$ echo $Password
123456

$ python
>>> import os
>>> os.environ["UserName"]
'admin'
```
除了这种方式，HttpRunner 还借鉴了 pipenv 加载.env的方式。

在项目中，创建.env文件，将敏感数据信息放置到其中，存储采用name=value的格式：

```
$ cat .env
UserName=admin
Password=123456
PROJECT_KEY=ABCDEFGH
```
同时，.env文件不应该添加到代码仓库中，建议将.env加入到.gitignore中。

默认情况下，.env文件应该位于运行hrun命令的同级目录下，在此情况下，运行hrun命令时就会自动将.env文件中的内容加载到运行时的环境变量中。

假如.env文件位于其它位置，或者采用了不同的文件名称，那么就需要采用--dot-env-path参数指定文件路径：

```
$ hrun /path/to/testset.yml --dot-env-path /path/to/.env --log-level debug
INFO     Loading environment variables from /path/to/.env
DEBUG    Loaded variable: UserName
DEBUG    Loaded variable: Password
DEBUG    Loaded variable: PROJECT_KEY
...
```
## 使用敏感数据
在 debugtalk.py 文件中，通过 os.environ 获取指定的环境变量数据。

```
import os

UserName = os.environ["UserName"]           # admin
Password = os.environ["Password"]           # 123456
PROJECT_KEY = os.environ["PROJECT_KEY"])    # ABCDEFGH
```
然后，在 YAML/JSON 格式的测试用例中，就可以通过$var的方式获取到敏感数据了。

```
- test:
    name: login
    request:
        url: http://host/api/login
        method: POST
        headers:
            Content-Type: application/json
        json:
            username: $UserName
            password: $Password
        validate:
            - eq: [status_code, 200]
```
