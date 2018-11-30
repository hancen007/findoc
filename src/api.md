1. 上半年总结
  - 自动化测试小组实施流程
      - 目的系统评估
      - 框架选型
        - pytest + selenium/requests（测试框架）
        - katalon Studion（开源自动化平台）
      - 开发
      - 回归
---
  自动化在项目实施成果：
  - 定期的知识分享培训，提高自动化测试在项目的使用率。
  - ECR系统和票交所系统项目上人员可独立完全项目自动化的需求
  - 建立比较完整自动化测试过程，从文档，脚本开发，脚本执行，报告输出等

---
  目前存在的问题：
  - 上半年各项目开发的进度比较忙，对于测试上功能的测试投入时间更多，自动化测试在项目实施中实用率不高
  - 自动化测试在项目中使用不充足，建议各项目在评估工作量中加入自动化测试的建设，并且要尽早介入测试和开发脚本，争取保持与开发周期同步
  - 实施初期由于测试用例是用代码直接编写，在项目实施过程会对测试人员能力要求偏高，所以在项目使用中进度比预期进度要慢
  - 目前自动化实施是以项目出发，项目成员维护和执行，产出未能形成统一可视化管理
-----
2. 下半年计划：
  测试管理与测试平台：项目接口编辑，文档导出，接口测试，用例记录，自动化测试，团队管理等功能，涵盖文档编辑，在线测试，自动化等各种场景，实现一站式测试
  ![](api.png)
  * 方案一:利用开源的测试管理平台，进行二次开发，定制适合自身需求,目前主流开源项目有：
    - Yapi [链接](http://47.106.115.161:3000/)
    - Doclevel [链接](http://doclever.cn/controller/read/read.html#5a532f98b7731a2ba86093b3)
    - httprunnerManage [链接](https://github.com/HttpRunner/HttpRunnerManager)
    - LuckyFrameWeb [链接](https://gitee.com/seagull1985/LuckyFrameWeb/wikis/pages?title=%E9%A1%B9%E7%9B%AE%E4%BB%8B%E7%BB%8D&parent=%E9%A1%B9%E7%9B%AE%E4%BF%A1%E6%81%AF)

    | 技术   | Yapi                  | Doclevel              | httprunnerManage           | LuckyFrameWeb                                                |
    | ------ | --------------------- | --------------------- | -------------------------- | ------------------------------------------------------------ |
    | 前端   | react redux           | vue+element UI        |                            | Bootstrap                                                |
    | 后端   | koa mongoose          | express+mongodb       | Django  mysql   djcelery | java mysql                                                   |
    | 功能点 | 项目管理              | 项目管理- 团队协作    | 项目管理                   | 接口+Web UI+移动端：支持接口+Web UI+移动端自动化，客户端OS必须为Windows系统，UI、移动端自动化采用WebDriver3.0+appium封装，纯关键字驱动，0编码。 |
    |        | 可视化接口管理        | 可视化接口管理        | 可视化接口管理             | HTTP+Socket接口免编码                                    |
    |        | Mock Server           | Mock Server           | Mock Server                |                                                              |
    |        | swagger, postman, har | postman，rap，swagger | har,YAML,Json              |                                                              |
    |        | 插件机制              |                       |                            |                                                              |
    |        |                       |                       |                            |                                                              |

    

  * 方案二:利用集团的自动化测试平台，进行需求定制:
    - 集团测试平台地址 [链接](http://10.18.38.42:8090/poluton/index.html)
    ```账号：finance，密码：finance ```
---

