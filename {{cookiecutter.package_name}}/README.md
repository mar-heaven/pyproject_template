{{ cookiecutter.project_name }}
====

Features
--------
* package.sh ������Ӧ�÷ŵ�jenkins��ʵ��

Build image:
----
1. ����sh package.sh ����whl��
2. ���� docker build -t {{ cookiecutter.project_name }}:0.1 . �����ɾ��񣬰汾��Ӧ����versioneer����
