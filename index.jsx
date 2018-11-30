---
banner:
  name: '更懂你的学习文档站'
  desc: '基于软件自动化测试'
  btns:
    - { name: '开 始', href: './webdriver/README.html', primary: true }
    - { name: '金融测试网', href: 'http://fintest.midea.com/fintest/',primary: true}
features:
  - { name: 'WebUI自动化', desc: '在上线新功能的时候都需要对网站的主要流程做一遍回归测试，已确保新改动不会对旧功能造成影响。引入UI的自动化，可以有效减少重复人力劳动，节约时间，提高效率' }
  - { name: 'API接口自动化', desc: '接口测试提前介入，加强系统的逻辑测试' }
  - { name: '性能自动化', desc: '性能测试是通过自动化的测试工具模拟多种正常、峰值以及异常负载条件来对系统的各项性能指标进行测试' }

footer:
  copyRight:
    name: '金融测试网'
    href: 'http://fintest.midea.com/fintest/'
  links:
    团队网址:
      - { name: 'Fintest', href: 'http://fintest.midea.com/fintest/' }
---
<Homepage banner={banner} features={features} />
<Footer distPath={props.page.distPath} copyRight={props.footer.copyRight} links={props.footer.links} />
