
### 运行工程步骤  2021.09.24

### 快速 进入py366
```
$ source  /Users/wuchunlong/local/py366/env/bin/activate
$ cd /Users/wuchunlong/local/github/sync-mysql
```

### 运行工程
```
初次运行
1、$ ./create_mysql.sh  创建mysql-studb数据库和表; 只能在Python 3.6.6环境工作！
2、$ python mysite/init_mysql.py  给mysql-studb数据库account_student表，初始化100条记录；
3、$ ./start.sh -i  运行
运行
$ ./start.sh
```

### 主要功能
```
本例使用了mysql、db.sqlite3两个数据库。
运行$ python mysite/init_mysql.py，mysql获得初始化数据；
通过数据更新，本例用三种方法，将mysql数据库数据，写入到db.sqlite3数据库；
 
1、前台实现-不用定时任务。按‘更新数据库按钮’-正在更新(动画)...-更新完成-显示‘更新数据库按钮’（更新的记录数）。   
2、前台实现-用定时任务-前台每分钟刷新一次页面。按‘更新数据库按钮’-正在更新...-更新完成-出现‘更新数据库按钮’，不能返回更新的记录数。
3、admin 添加一个按钮-不用定时任务。按‘更新数据库按钮’-正在更新...-更新完成-显示‘更新数据库按钮’（更新的记录数）。 

```

### 使用到的技术
```
1、定时执行任务、数据库数据更新
2、每隔60秒刷新一次页面
3、程序运行过程显示动画
4、mysql数据库
5、脚本操作mysql   https://www.cnblogs.com/study-learning/p/10800820.html
```

### 验证步骤详情  
```
1、$ ./create_mysql.sh  创建mysql-studb数据库;
...
Applying auth.0008_alter_user_username_max_length... OK
Applying sessions.0001_initial... OK

2、$ python mysite/init_mysql.py  给mysql-studb数据库的account_student表，初始化100条记录；
...
django版本: 1.11.5。

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
(env375) $ python mysite/manage.py crontab add
### 删除所有定时任务
```  
(env375) $ python mysite/manage.py crontab remove
removing cronjob: (b173a63adf4d670247b6b63dd93bc07b) -> ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')
```

