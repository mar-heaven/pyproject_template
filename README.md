## 项目生成模板
### 前言
看到前公司同事 **zza** 大佬最近在研究 **cookiecutter** 模板，本着跟随大佬脚本的原则于是乎也新起了一个项目玩玩。
初始化 *Python* 项目的模板

### 引用
主要引用了两个开源项目
* [python-versioneer](https://github.com/python-versioneer/python-versioneer): 用于生成Git版本号的工具
* [cookiecutter](https://github.com/cookiecutter/cookiecutter) 生成项目模板的工具

### 使用
```
(tool) G:\Workspace>cookiecutter https://github.com/mar-heaven/pyproject_template.git
project_name [Python Package]: play
package_name [play]:
project_slug [play]:
project_short_description [Project Short Description]: just play
Select is_service:
1 - y
2 - n
Choose from 1, 2 [1]: 1 
```
### 参数
* project_name: 项目名字
* package_name: 包名
* project_slug: 包名
* 项目描述
* Select is_service: 1 生成Dockerfile 
