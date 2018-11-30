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

    def test_verify_update_post(self):
        '''验证修改文章接口'''
        '''
        #接口文章的接口地址
        # POST /wp/v2/posts/<id>
        #先获取一个文章的id，两种方法，第一创建一个文章，第二直接查询，下面直接新建一个文章，稳定性高
        '''
        post_id = self.Create_a_Post()['id']
        print(post_id)
        url = self.host + '/wp-json/wp/v2/posts/' +str(post_id)
        title = 'update_title'
        post = {
            'title':'{}'.format(title)
            }
        r = requests.post(url,data=post,auth=HTTPBasicAuth(self.user,self.pwd))
        result = r.json()
        #断言
        self.assertEqual(title,result['title']['raw'])

    def test_Delete_Post(self):
        '''测试删除文章接口'''
        '''
        #接口文章的接口地址 使用 DELETE请求方式
        #DELETE /wp/v2/posts/<id>
        #先获取一个文章的id，两种方法，第一创建一个文章，第二直接查询，下面直接新建一个文章，稳定性高
        '''
        post_id = self.Create_a_Post()['id']
        url = self.host + '/wp-json/wp/v2/posts/85' #+str(post_id)
        r = requests.delete(url,auth=HTTPBasicAuth(self.user,self.pwd))
        result = r.json()
        #预期结果
        code = 'rest_already_trashed'
        #断言
        self.assertEqual(code,result['code'])


if __name__ == '__main__':
    unittest.main()
