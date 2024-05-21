from setuptools import setup, find_packages

setup(
    name='qianfan',
    version='0.3.12',
    description='qianfan sdk  package',
    author='zhangning',
    author_email='zhangning@lenovo.com',
    packages=find_packages(),  # 自动发现和包含项目中的所有Python包
    install_requires=[
        # 这里放置需要安装的依赖包
        'requests',
    ],
    python_requires='>=3.8',  # 指定支持的Python版本
)