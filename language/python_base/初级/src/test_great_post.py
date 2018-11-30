import  unittest,json,requests
from requests.auth import HTTPBasicAuth
import time


# 接口的相关地址 https://developer.wordpress.org/rest-api/reference/posts/

class Great_Post(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host = 'http://47.106.115.161:8000'
        cls.user = 'admin'
        cls.pwd = 'admin'

    def test_lists_Post(self):
        '''查询所有文章'''
        url = self.host + '/wp-json/wp/v2/posts'
        r = requests.get(url)
        result = r.json()
        print(result)

    def Create_a_Post(self,nowtime = None):
        '''创建一篇文章'''
        if nowtime == None:
            strtime = str(time.time())
        else:
            strtime = nowtime

        post = {
            'title':'test_title%s' %(strtime),
            'slug': 'rest-api-1',
            'status': 'publish',
            'content': 'this is the content post',
            'author': '1',
            }
        #请求的地址
        url = self.host + '/wp-json/wp/v2/posts/'
        #r = requests.post(url,data=post,auth=HTTPBasicAuth('admin','admin'))
        r = requests.post(url,data=post,auth=HTTPBasicAuth(self.user,self.pwd))
        result = r.json()
        return result

    def test_verify_Create_Post(self):
        '''验证发表文章接口'''
        nowtime = str(time.time())
        #调发文章的方法
        post = self.Create_a_Post(nowtime)
        #构造测试数据 文章的标题
        test_title = 'test_title' + nowtime
        #获取生成后的标题返回的值
        get_title = post['title']['raw']
        self.assertEqual(test_title,get_title)



if __name__ == '__main__':
    unittest.main()
