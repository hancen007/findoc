# 编写测试用例
建议以YAML格式编写测试用例。

演示
以下是一个典型场景的测试集示例：token在开始处获取，每个后续请求都应该token在头文件中进行。

```
- config:
    name: "create user testsets."
    variables:
        - user_agent: 'iOS/10.3'
        - device_sn: ${gen_random_string(15)}
        - os_platform: 'ios'
        - app_version: '2.8.6'
    request:
        base_url: "http://127.0.0.1:5000"
        headers:
            Content-Type: application/json
            device_sn: $device_sn

- test:
    name: get token
    request:
        url: /api/get-token
        method: POST
        headers:
            user_agent: $user_agent
            device_sn: $device_sn
            os_platform: $os_platform
            app_version: $app_version
        json:
            sign: ${get_sign($user_agent, $device_sn, $os_platform, $app_version)}
    extract:
        - token: content.token
    validate:
        - eq: ["status_code", 200]
        - len_eq: ["content.token", 16]

- test:
    name: create user which does not exist
    request:
        url: /api/users/1000
        method: POST
        headers:
            token: $token
        json:
            name: "user1"
            password: "123456"
    validate:
        - eq: ["status_code", 201]
        - eq: ["content.success", true]
```
YAML/JSON格式测试用例支持函数调用，例如gen_random_string和get_sign以上。这个机制依赖于debugtak.py热插件，我们可以用它来定义debugtak.py文件中的函数，然后可以在运行时自动发现和调用函数。

有关编写测试用例的详细规定，您可以阅读quickstart文档。

比较
HttpRunner 目前支持以下比较器。

| comparator           | Description                   | A(check), B(expect)     | examples                                     |
| -------------------- | ----------------------------- | ----------------------- | -------------------------------------------- |
| `eq`, `==`           | value is equal                | A == B                  | 9 eq 9                                       |
| `lt`                 | less than                     | A < B                   | 7 lt 8                                       |
| `le`                 | less than or equals           | A <= B                  | 7 le 8, 8 le 8                               |
| `gt`                 | greater than                  | A > B                   | 8 gt 7                                       |
| `ge`                 | greater than or equals        | A >= B                  | 8 ge 7, 8 ge 8                               |
| `ne`                 | not equals                    | A != B                  | 6 ne 9                                       |
| `str_eq`             | string equals                 | str(A) == str(B)        | 123 str_eq '123'                             |
| `len_eq`, `count_eq` | length or count equals        | len(A) == B             | 'abc' len_eq 3, [1,2] len_eq 2               |
| `len_gt`, `count_gt` | length greater than           | len(A) > B              | 'abc' len_gt 2, [1,2,3] len_gt 2             |
| `len_ge`, `count_ge` | length greater than or equals | len(A) >= B             | 'abc' len_ge 3, [1,2,3] len_gt 3             |
| `len_lt`, `count_lt` | length less than              | len(A) < B              | 'abc' len_lt 4, [1,2,3] len_lt 4             |
| `len_le`, `count_le` | length less than or equals    | len(A) <= B             | 'abc' len_le 3, [1,2,3] len_le 3             |
| `contains`           | contains                      | [1, 2] contains 1       | 'abc' contains 'a', [1,2,3] len_lt 4         |
| `contained_by`       | contained by                  | A in B                  | 'a' contained_by 'abc', 1 contained_by [1,2] |
| `type_match`         | A is instance of B            | isinstance(A, B)        | 123 type_match 'int'                         |
| `regex_match`        | regex matches                 | re.match(B, A)          | 'abcdef' regex 'a\w+d'                       |
| `startswith`         | starts with                   | A.startswith(B) is True | 'abc' startswith 'ab'                        |
| `endswith`           | ends with                     | A.endswith(B) is True   | 'abc' endswith 'bc'                          |



提取和验证
假设我们得到以下HTTP响应。

```
// status code: 200

// response headers
{
    "Content-Type": "application/json"
}

// response body content
{
    "success": False,
    "person": {
        "name": {
            "first_name": "Leo",
            "last_name": "Lee",
        },
        "age": 29,
        "cities": ["Guangzhou", "Shenzhen"]
    }
}
```
在extract和validate，我们可以做链式操作来提取HTTP响应中的数据字段。

例如，如果我们想获得Content-Type响应标题，那么我们可以指定headers.content-type; 如果我们想获得first_name响应内容，我们可以指定content.person.name.first_name。

列表中可能会有细微差别，因此我们可以使用索引来定位列表项。例如，Guangzhou响应内容可以通过指定content.person.cities.0。

```
// get status code
status_code

// get headers field
headers.content-type

// get content field
body.success
content.success
text.success
content.person.name.first_name
content.person.cities.1

extract:
    - content_type: headers.content-type
    - first_name: content.person.name.first_name
validate:
    - eq: ["status_code", 200]
    - eq: ["headers.content-type", "application/json"]
    - gt: ["headers.content-length", 40]
    - eq: ["content.success", true]
    - len_eq: ["content.token", 16]
```
