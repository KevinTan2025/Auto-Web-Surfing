# 自动浏览网页的python脚本
你是否有想过给自己的博客/网页有比较不错的流量呢？以下是用python写的自动运行脚本；它可以自定义网址，运行间隔时间以及重复次数。

        import requests
        import random
        import time
        from bs4 import BeautifulSoup

        # 要访问的网址
        url = 'https://kevintan.pro'

        # 定义 user-agent 列表，模拟不同的客户端浏览器
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        ]

        # 定义访问次数和访问间隔时间
        num_visits = 10
        min_interval = 10
        max_interval = 40

        # 循环访问网页
        for i in range(num_visits):
            # 随机选择一个 user-agent
            headers = {'User-Agent': random.choice(user_agents)}

            # 发起 HTTP 请求
            response = requests.get(url, headers=headers)
            print(f'[{i+1}/{num_visits}] Status code: {response.status_code}')

            # 随机等待指定的时间间隔
            time_interval = random.randint(min_interval, max_interval)
            print(f'Waiting {time_interval} seconds before next visit...')
            time.sleep(time_interval)

            # 获取页面中的链接
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            if len(links) > 0:
                # 随机选择一个链接
                link = random.choice(links)
                href = link.get('href')
                if href:
                    # 发起 HTTP 请求
                    response = requests.get(href, headers=headers)
                    print(f'    Subpage visited: {href}, status code: {response.status_code}')

                    # 随机等待指定的时间间隔
                    time_interval = random.randint(min_interval, max_interval)
                    print(f'    Waiting {time_interval} seconds before returning to main page...')
                    time.sleep(time_interval)
