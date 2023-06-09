# 基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将项目文件复制到镜像中
COPY . /app

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露项目的运行端口
EXPOSE 8000

# 运行 Django 项目
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]