# 构建镜像
```bash
docker build -t flask_demo:v1 .
```
# 运行容器

```bash
docker container run --name my-flask -p 10080:10080 -d flask_demo:v1
docker container ps -l

```
