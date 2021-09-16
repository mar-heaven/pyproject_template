{{ cookiecutter.project_name }}
====

Features
--------
* package.sh 的内容应该放到jenkins中实现

Build image:
----
1. 运行sh package.sh 生成whl包
2. 运行 docker build -t {{ cookiecutter.project_name }}:0.1 . 来生成镜像，版本号应该由versioneer生成
