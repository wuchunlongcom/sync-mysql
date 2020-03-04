### sync-mysql 更新数据库数据 2020.02.25
### 关键词：更新数据库数据 admin 添加按钮 db.sqlite3 mysql django使用定时执行任务 刷新页面 显示动画


### 功能
```
工程使用db.sqlite3数据库，连接mysql从mysql数据库获取数据，再写入db.sqlite3数据库
本例用三种方法，实现更新数据库数据，从mysql数据库获取数据，再写入db.sqlite3数据库; 
1、前台实现-不用定时任务。按‘更新数据库按钮’-正在更新(动画)...-更新完成-显示‘更新数据库按钮’（更新的记录数）。实现的功能很完善。 
   
2、前台实现-用定时任务-前台每分钟刷新一次页面。按‘更新数据库按钮’-正在更新...-更新完成-出现‘更新数据库按钮’，不能返回更新的记录数。
3、admin 添加一个按钮-用定时任务-前台每分钟刷新一次页面。按‘更新数据库按钮’-正在更新... ，此时只有观察数据库记录变化了，说明数据库更新完成。

4、admin 添加一个按钮-不用定时任务。按‘更新数据库按钮’-正在更新...-更新完成-显示‘更新数据库按钮’（更新的记录数）。实现的功能很完善。 

```

### 提交：
```
1、定时执行任务
2、每隔60秒刷新一次页面
3、修改README.md     

```


### 操作步骤  
```
1、./start_mysql.sh  用脚本初始化studb数据库（mysql）;
2、python mysite/initmysql.py  给studb数据库(mysql)的account_student表，初始化1000条记录；   
3、./start_mysql.sh 数据初始化，从studba数据库account_student表中获取数据；此时list db.sqlite3中Student表中是没有数据的;
4、./start.sh -i ;
5、前台实现更新数据库;
6、按更新按钮, 连接mysql 数据库，更新实例中的db.sqlite3数据库数据，list中获得数据;

```
### 删除所有定时任务
```  
(env375) $ python mysite/manage.py crontab remove
removing cronjob: (b173a63adf4d670247b6b63dd93bc07b) -> ('*/1 * * * *', 'account.cron.test', '>>/tmp/test.log')
```

### 使用到的技术
```
1、连接studb(mysql)数据库
2、脚本操作mysql   https://www.cnblogs.com/study-learning/p/10800820.html
3、程序运行过程显示动画
```