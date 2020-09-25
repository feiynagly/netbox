
二、安装
1、数据库安装

#安装
yum install postgresql10-contrib postgresql10-server -y
#默认数据目录   /var/lib/pgsql/10/data/
#默认安装目录  /usr/pgsql-10/

#初始化
/usr/pgsql-10/bin/postgresql-10-setup initdb
#启动数据库并设置为开机自启动
sudo systemctl start postgresql-10
sudo systemctl enable postgresql-10.service

#创建数据库
# sudo -u postgres psql
postgres=# CREATE DATABASE netbox;
postgres=# CREATE USER netbox WITH PASSWORD 'J5brHrAXFLQSif0K';
postgres=# GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox;
postgres=# \q

#测试数据库
# psql --username netbox --password --host 127.0.0.1 netbox
Password for user netbox: 
psql (10.12 (Ubuntu 10.12-0ubuntu0.18.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.
netbox=> \q

2、安装Netbox
#下载netbox （在开源版本上的定制版，修改了数据库，不能直接下载开源版本）
wget https://github.com/feiynagly/netbox/archive/master.zip
#解压下载后的文件至/home/netbox/下
unzip netbox-master.zip

#  安装相关组件
yum install -y gcc python36 python36-devel python36-setuptools libxml2-devel libxslt-devel libffi-devel openssl-devel redhat-rpm-config 
yum install -y esay_install-3.6 pip
pip3 install --upgrade pip --proxy=http://10.61.2.214:800

#安装Netbox依赖（在/home/netbox/目录下执行，该目录下有requirements.txt文件）
pip3 install -r requirements.txt --proxy=http://10.61.2.214:800


#修改netbox配置文件
/home/netbox/netbox/netbox/configuration.py

#定义监听地址
ALLOWED_HOSTS = ['netbox.example.com', '10.0.10.4']
#定义postgresql数据库
DATABASE = {
    'NAME': 'netbox',               # Database name
    'USER': 'netbox',               # PostgreSQL username
    'PASSWORD': 'J5brHrAXFLQSif0K', # PostgreSQL password
    'HOST': 'localhost',            # Database server
    'PORT': '',                     # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,            # Max database connection age (seconds)
}
#定义秘钥   
#使用netbox自带工具generate_secret_key.py生成秘钥并写在配置文件中（在/home/netbox/netbox/下执行命令phthon3  ./generate_secret_key.py）
SECRET_KEY = 'XF4*=k&8n+0_c@v1WjAU2zdDhHQT3N%mP6JEwl#fSKOgCB^Go5'
PREFER_IPV4 = True
#如果不用webhook，可以不需要redis数据库

#初始化数据库（netbox解压后，在/home/netbox/netbox下有个自带的manage.py文件）
python3 manage.py migrate
python3 manage.py createsuperuser

#测试netbox
python3 manage.py runserver 0.0.0.0:8000 --insecure
之后可以通过网页打开netbox


3、部署https服务器
1 部署WSGI容器
#gunicorn处理动态页面，静态资源无法加载，也无法负载均衡以及启用https
#部署WSGI容器gunicorn
pip3 install gunicorn --proxy=http://10.61.2.214:800

#启动gunicorn容器（gunicorn配置文件在/home/netbox/目录下，可参照/home/netbox/contrib/gunicorn_config.py中的范例设置）
gunicorn -D -c gunicorn_config.py netbox.wsgi 

2、生成证书用于https
#生成一个key
openssl genrsa -des3 -out ssl.key 1024

#生成key必须输入密码，可以生成后删除该密码，否则nginx启动加载该证书时需要输入密码。这一步是可以选操作。
mv ssl.key ssl_enc.key

openssl rsa -in ssl_enc.key -out ssl.key

rm ssl_enc.key



#生成证书请求文件（弹出的提示信息可以任意输入）

openssl req -new -key ssl.key -out ssl.csr


#生成证书文件(有效期3650天）

openssl x509 -req -days 3650 -in ssl.csr -signkey ssl.key -out ssl.crt

#把证书复制至指定目录，用于nginx https调用
mv ssl.crt    /home/netbox
mv ssl.key   /home/netbox



3、配置nginx

# 安装nginx
yum install nginx

#默认路径
配置文件：/etc/nginx/nginx.conf
安装文件：/usr/sbin/nginx

参照/home/netbox/contrib/nginx.conf配置nginx

#停止防火墙
systemctl stop firewalld.servie
systemctl disable firewalld.servie

#启动nginx
/usr/sbin/nginx -t   (测试配置文件是否正确）
/usr/sbin/nginx -s reload  (重启）
./usr/sbin/nginx    （启动）



三、数据备份与恢复

1、备份
# 单次备份
pg_dump -U postgres -p 6060 -h 10.0.10.4 -F c -d netbox -f /home/backup/netbox.$(date "+%Y-%m-%d").bat

#自动备份
修改/home/netbox/contrib/backup.sh

#加入到定时任务
crontab -u root -e （打开编辑窗口）
10 1 * * * /home/backup.sh（写入一行）

crontab -u root -l  （查看定时任务）

2、恢复

pg_restore -c -d netbox -h 10.0.10.4 -U netbox  netbox.2020-09-12.bak

-c 创建前清除数据数据
-d 数据库名称
-h 要恢复的数据库地址
-U 用户名
netbox.2020-09-12.bak 数据库备份文件
