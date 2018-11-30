





# 项目汇总表

|                        |              |        |
| ---------------------- | ------------ | ------ |
| id                     | 编号     | string |
| pro_id       | 任务编号 | string |
| product_name           | 项目名称     | string |
| project_name           |              | string |
| suite_name             | 套件名称     | string |
| status                 | 状态         | string |
| total_testcase_number  | 总共用例数   | int    |
| passed_testcase_number | 成功用例数   | int    |
| failed_testcase_number | 失败用例数   | int    |
| run_starttime          | 执行开始时间 | data   |
| run_endtime            | 执行结束时间 | data   |
| duration               | 持续时间     | data   |
| createdtimestamp       | 创建时间     | data   |
| createdby              | 创建人       | string |
|                        |              |        |





```
id
job_number
product_name
project_name
record_type
suite_name
testcase_name
testcase_desc
status
total_testcase_number
passed_testcase_number
failed_testcase_number
run_starttime
run_endtime
duration
comment
createdtimestamp
createdby

demo
'20180612053212',--当次执行的任务编号,--字符串类型，格式可以考虑yyyymmddhhmmss,
'GOMS产品',--产品名称,--字符串类型,
'GOMS_配合版本测试',--项目名称,--字符串类型,
'overall',--记录类型,--类型有overall、suite、testcase三种
'suiteName',--suite套件名,当记录类型位overall时，这里值为空
'2018-6-12 4:31:12',--:执行开始时间,--yyyy-mm-dd hh:mm:ss格式,
'2018-6-12 4:33:04',--:执行结束时间,--yyyy-mm-dd hh:mm:ss格式,
'2 Min 52 Sec',--:执行持续时间,--字符串类型,可以不填
20,--:总共用例数,int类型
18,--:成功的用例数,int类型
2,--:失败的用例数,int类型
'',--:测试用例描述,字符串类型,当记录类型位overall时，这里值为空
'',--:测试用例名,字符串类型,当记录类型位overall时，这里值为空
'',--:执行状态,值可以为'Notrun','Skipped','Fail','Pass'的一种,当记录类型位overall时，这里值为空

'''

```





项目报表明细表

|                        |              |        |
| ---------------------- | ------------ | ------ |
| pro_id                     | 任务编号     | string |
| testcase_name          | 用例名称     | string |
| testcase_desc          | 用例描述     | string |
| status                 | 状态         | string |
| comment_log          | 执行日志 | string |
| createdtimestamp       | 创建时间     | data   |
| createdby              | 创建人       | string |
|                        |              |        |

