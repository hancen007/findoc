#dubbo服务测试方案

>建议准入场景为以性能测试为基础，只做些高频，或者需要性能测试的接口

>需要开发进行编写符合jmeter格式的测试用例

- 工程依赖ApacheJMeter_core.jar、ApacheJMeter_java.jar这两个包，请从本地jmeter的安装目录下的lib\ext中获取
- 工程自身编译后的jar包，以及依赖的jar包，需放入jmeter的安装目录下的lib\ext
- com.midea.jr.jmeter.TestSampler即为自定义的java采样器
- 用jmeter打开jmeterExample.jmx，demo工程参考里面的配置

---

1. 模拟一个dubbo的服务，代码如下：
```
    #DemoService.java
    package com.midea.jr.dubbo.interfaces;

    public interface DemoService {
    	public String sayHello(String text);
    }
```
1. 初始化DubboLoader (代码如下：)
```
    ### DubboLoader.Java

    package com.midea.jr.jmeter;

    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    import org.springframework.context.ApplicationContext;
    import org.springframework.context.support.ClassPathXmlApplicationContext;

    import com.midea.jr.dubbo.interfaces.DemoService;
    import com.midea.jr.gfp.gbm.api.service.VoucherHandleFacadeService;

    public class DubboLoader {
    	private static final Logger LOGGER = LoggerFactory.getLogger(DubboLoader.class);
    	private static ApplicationContext context;

    	static {
    		LOGGER.info("load applicationContext.xml......");
    		try {
    			context = new ClassPathXmlApplicationContext("classpath:/applicationContext.xml");
    		} catch (Exception ex) {
    			LOGGER.error("context init fail", ex);
    		}
    	}

    	public static void main(String[] args) {
    		VoucherHandleFacadeService demoService = (VoucherHandleFacadeService) context.getBean("demoService");
    		String result = "OK";

    		LOGGER.info(result);
    	}

    	public static ApplicationContext getContext() {
    		return context;
    	}
    }
```

1. 开发测试jmeter工具用例类 (代码如下:)
```
    # TestSampler.Java
    package com.midea.jr.jmeter;

    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.util.ArrayList;
    import java.util.List;

    import org.apache.commons.lang3.exception.ExceptionUtils;
    import org.apache.http.HttpResponse;
    import org.apache.http.NameValuePair;
    import org.apache.http.client.entity.UrlEncodedFormEntity;
    import org.apache.http.client.methods.HttpPost;
    import org.apache.http.impl.client.CloseableHttpClient;
    import org.apache.http.impl.client.HttpClients;
    import org.apache.http.message.BasicNameValuePair;
    import org.apache.http.util.EntityUtils;
    import org.apache.jmeter.config.Arguments;
    import org.apache.jmeter.protocol.java.sampler.AbstractJavaSamplerClient;
    import org.apache.jmeter.protocol.java.sampler.JavaSamplerContext;
    import org.apache.jmeter.samplers.SampleResult;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    import org.springframework.context.ApplicationContext;

    import com.midea.jr.dubbo.interfaces.DemoService;
    import com.midea.jr.gfp.gbm.api.bo.ReceiveApplyReqBO;
    import com.midea.jr.gfp.gbm.api.bo.ReceiveApplyRespBO;
    import com.midea.jr.gfp.gbm.api.constant.GBMConstant;
    import com.midea.jr.gfp.gbm.api.service.VoucherHandleFacadeService;

    public class TestSampler extends AbstractJavaSamplerClient {

    	private static final Logger LOGGER = LoggerFactory.getLogger(TestSampler.class);
    	private ApplicationContext context;

    	private static void postForm(String url) throws IOException {
    		CloseableHttpClient httpclient = HttpClients.createDefault();
    		try {
    			HttpPost httppost = new HttpPost(url);
    			List<NameValuePair> nvps = new ArrayList<NameValuePair>();
    			nvps.add(new BasicNameValuePair("type", "10000"));
    			nvps.add(new BasicNameValuePair("content", new String(new char[4000]).replace("\0", "测")));
    			httppost.setEntity(new UrlEncodedFormEntity(nvps, StandardCharsets.UTF_8.name()));
    			httppost.setHeader("Content-type", "application/x-www-form-urlencoded; charset=utf-8");
    			HttpResponse response = httpclient.execute(httppost);
    			System.out.println(EntityUtils.toString(response.getEntity()));

    		} finally {
    			httpclient.close();

    		}
    	}

    	@Override
    	public void setupTest(JavaSamplerContext samplerContext) {
    		LOGGER.info("setupTest......");
    		// 初始化spring context
    		context = DubboLoader.getContext();
    	}

    	@Override
    	public Arguments getDefaultParameters() {

    		Arguments defaultParameters = new Arguments();
    		// 初始化参数，此参数的值在jmeter UI上可进行修改
    		defaultParameters.addArgument("url", "http://10.16.89.183:32000/dubbo-provider-test/springmvc/post");

    		return defaultParameters;

    	}

    	@Override
    	public SampleResult runTest(JavaSamplerContext samplerContext) {
    		LOGGER.info("runTest......");
    		SampleResult result = new SampleResult();
    		boolean success = true;
    		result.sampleStart();

    		// TODO: Write your test code below.
    		try {
    			// http post调用测试
    			// postForm(samplerContext.getParameter("url"));
    			// result.setResponseMessage("success post url:" +
    			// samplerContext.getParameter("url"));

    			// dubbo调用测试
    			VoucherHandleFacadeService demoService = (VoucherHandleFacadeService) context.getBean("demoService");
    			// TODO: 调用VoucherHandleFacadeService的方法，并判断结果的正确性
    			ReceiveApplyReqBO reqInfo = new ReceiveApplyReqBO();
    			reqInfo.setApplyUserId("monitor4a");
    			reqInfo.setApplyUserName("monitor4a");
    			reqInfo.setBankAccKey("key001");
    			reqInfo.setCurrencyCode("CNY");
    			reqInfo.setVoucherType(GBMConstant.VoucherType.BANK_CHECK);
    			reqInfo.setBizNo("zk001");
    			reqInfo.setOrgCode("1200");
    			reqInfo.setOrgName("发的");
    			reqInfo.setSourceCode(GBMConstant.DataSource.GBM_VOUCHER);
    			ReceiveApplyRespBO respInfo = demoService.sendReceiveApply(reqInfo);
    			if (!"000000".equals(respInfo.getBackCode())) {
    				success = false;
    			}

    			result.setResponseMessage(respInfo.getBackCode());
    		} catch (Exception e) {
    			success = false;
    			result.setResponseMessage(
    					"url:" + samplerContext.getParameter("url") + "\n" + ExceptionUtils.getStackTrace(e));
    		}
    		// TODO: Write your test code above.

    		result.sampleEnd();
    		result.setSuccessful(success);

    		return result;
    	}
    }
```
1. 启动jmeter工具（编译后的jar包，以及依赖的jar包，需放入jmeter的安装目录下的lib\ext），新建java类的请求


2. 运行
