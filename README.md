# 自动浏览网页的python脚本

你是否有想过给自己的博客/网页有比较不错的流量呢？以下是用python写的自动运行脚本；它可以自定义网址，导入github action进行周期性计划任务。当然，最大的特点是可以自行选择sitemap.xml的url,以保证 Google Analytics的记录分析。
![image](https://user-images.githubusercontent.com/51069261/226630915-88246f15-d60f-4668-b149-036e35d70a79.png)


![image](https://user-images.githubusercontent.com/51069261/226631047-8847899a-aba1-485b-b4b7-81a1b90e9958.png)


请注意！你需要在workflows里面的 main.yml 把

      on: [push]


替换为

      on:
        schedule:
          - cron: '*/10 * * * *'


**必须等待完整运行后才能修改成先前的定期执行任务，否则将不会运行。**


可自定义的部分

![image](https://user-images.githubusercontent.com/51069261/226636145-af01399d-ab56-4c41-a203-caa557b2476d.png)


其中的**website_url**可输入你的url，并且sitelink.xml可以根据你实际的url来填写。

![image](https://user-images.githubusercontent.com/51069261/226636470-185f8a61-17ae-4817-a86d-29f1eaf85ef3.png)

解释

      num_visits = 10 就是打开10个窗口 (Chrome)
      min_interval = 10 最小间隔时间 （秒）     
      max_interval = 30 最大间隔时间 （秒）     
