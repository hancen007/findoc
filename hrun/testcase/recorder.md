# 录制生成用例
为了简化测试用例的编写工作，HttpRunner 实现了测试用例生成的功能，对应的转换工具为一个独立的项目：har2case。

简单来说，就是当前主流的抓包工具和浏览器都支持将抓取得到的数据包导出为标准通用的 HAR 格式（HTTP Archive），然后 HttpRunner 实现了将 HAR 格式的数据包转换为YAML/JSON格式的测试用例文件的功能。

## 获取 HAR 数据包
在转换生成测试用例之前，需要先将抓取得到的数据包导出为 HAR 格式的文件。在Charles Proxy中的操作方式为，选中需要转换的接口（可多选或全选），点击右键，在悬浮的菜单目录中点击【Export...】，格式选择HTTP Archive(.har)后保存即可；假设我们保存的文件名称为 demo.har。
![demo](/img/charles-export.jpg)

## 转换生成测试用例
然后，在命令行终端中运行 har2case 命令，即可将 demo.har 转换为 HttpRunner 的测试用例文件。

这里需要说明的是，har2case 可将 HAR 文件转换为 YAML 或 JSON 格式的测试用例，具体转换为什么形式取决于第二个参数（testset_path）。
```
$ har2case /path/to/demo.har testset_path
```
若第二个参数为空，则默认转换为 JSON 格式的测试用例，文件名称和路径与 HAR 源文件相同。

```
$ har2case docs/data/demo-quickstart.har
INFO:root:Generate JSON testset successfully: docs/data/demo-quickstart.json
```
若文件后缀为.yml/.yaml，则转换生成 YAML 格式的测试用例。

```
$ har2case docs/data/demo-quickstart.har demo.yml
INFO:root:Generate YAML testset successfully: demo.yml
```
若文件后缀为.json，则转换生成 JSON 格式的测试用例。

```
$ har2case docs/data/demo-quickstart.har demo.json
INFO:root:Generate JSON testset successfully: demo.json
```
