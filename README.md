
### sync-mysql  
### django crontab定时执行任务。将mysql数据库的数据同步到db.sqlite3

###python3.6.6   django版本: 2.2.6。
### 快速 进入py366
```
$ source  /Users/wuchunlong/local/py366/env/bin/activate
$ cd /Users/wuchunlong/local/github/sync-mysql
```
### 运行工程
```
初次运行
1、$ ./create_mysql.sh  创建mysql-studb数据库和表; 只能在Python 3.6.6环境工作！
2、$ python mysite/init_mysql.py  给mysql-studb数据库account_student表，初始化1000条记录；
3、$ ./start.sh -i  运行
运行
$ ./start.sh
```
### 主要功能
```
1、前台实现-不用定时任务。按‘更新数据库按钮’-正在更新(动画)...-更新完成-显示‘更新数据库按钮’（更新的记录数）。   
2、前台实现-用定时任务-前台每分钟刷新一次页面。按‘更新数据库按钮’-数据库更新中，请稍等....-更新完成-出现‘更新数据库按钮’。
3、admin 添加一个按钮-用定时任务。按‘更新数据库按钮’-数据库更新中，请稍等...-更新完成-显示‘更新数据库按钮’）。 

```
### 使用到的技术
```
本例使用了mysql、db.sqlite3两个数据库。
运行$ python mysite/init_mysql.py， mysql获得初始化1000条记录；
通过数据更新，本例用三种方法，将mysql数据库数据，写入到db.sqlite3数据库；
 
1、定时执行任务、数据库数据更新
2、每隔60秒刷新一次页面
3、程序运行过程显示动画
4、mysql数据库
5、shell脚本写mysql语句 脚本操作mysql   https://www.cnblogs.com/study-learning/p/10800820.html
```
### 创建mysql-studb数据库,初始化1000条记录
```
1、$ ./create_mysql.sh  创建mysql-studb数据库;
...
Applying auth.0008_alter_user_username_max_length... OK
Applying sessions.0001_initial... OK

2、$ python mysite/init_mysql.py  给mysql-studb数据库的account_student表，初始化1000条记录；
...

### 验证步骤详 
$ mysql -u root -p
mysql> show databases;  # 显示数据库
mysql> use studb;   # 使用数据库studb   必须！！！
mysql> show tables;  # 显示表
mysql>select * from account_student;  # 显示表数据
+-----+--------+---------+------------+
| id  | sid    | name    | address    |
+-----+--------+---------+------------+
|   1 | sid-0  | name-0  | address-0  |
|   2 | sid-1  | name-1  | address-1  |
|   3 | sid-2  | name-2  | address-2  |
mysql> drop database studb; # 删除数据库studb
mysql> quit   
3、$ ./start.sh -i
###本机运行时，出现【终端.APP对话框】，选择【好】
...
removing cronjob: (aae4bd6b5a8e7449f14322a064c567a2) -> ('*/1 * * * *', 'account.cron.work')
  adding cronjob: (aae4bd6b5a8e7449f14322a064c567a2) -> ('*/1 * * * *', 'account.cron.work')
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 24, 2021 - 07:53:04
Django version 2.2.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 启动定时任务
(env) $ python mysite/manage.py crontab add
### 删除所有定时任务
```  
(env) $ python mysite/manage.py crontab remove
removing cronjob: (b173a63adf4d670247b6b63dd93bc07b) -> ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')
```

### 下拉
```
$ git clone https://github.com
```

### 推送
```
$ rm  -rf env
$ git add .
$ git ci -a -m 'add data'
$ git push   必须T用OKEN！
```

# 定时器  跑同步脚本
# 前端：
# 1. 没有此状态文件时，对登陆用户就正常显示同步按钮。
# 2. 有此文件时，对登陆用户就显示一个 <Span> ，不是 button，写 “同步中，请等待””
# 3. 用户点击按钮后，在后台create一个文件，里面写0，表示待同步
# 后端：
# 1. 加一条crontab，每分钟跑一次脚本
# 2. 脚本判断逻辑：
# 2.1 状态文件存在+内容是0  -- 待同步
#     状态文件内容改成1
#     跑同步脚本
# 2.2 状态文件存在+内容是1  -- 同步中
#     跑同步脚本
# 2.3 状态文件存在+内容是1  -- 同步完成
#     同步脚本跑完，删除状态文件    
# 2.4 状态文件不存在
#     空跑、啥也不做
更新时间： 2022.08.26