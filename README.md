**自动化框架说明**
* * *
概况：
组成： Python+Pytest+Allure，外部组件：Jenkins、mysql
* * *
如何使用
* 安装Python，版本3.9.x
* 安装Pytest，版本< 6.1.0
* * *
运行入口：
* runsuilt.py，其中运行需要制定运行的文件夹；# sys.argv.append("cases”)，其中cases是可以根据cases的目录机结构
* 命令行运行 pytest cases --alluredir ./report  ;  -allure 后面可以添加参数，具体参照allure使用方式
* idel窗口直接运行，调试
* * *
代码组成：
* client：接口请求类封装，目前只有get、post，后续根据需要需要playload header，目前是写死的，修改需要修改api装饰器
```
    def api(path=None, method=None):
        def wrapper(func):
            @functools.wraps(func)
            def _wrapper(self, **kwargs):
```
* mysqlcoon：mysql的连接已经封装好，目前有query方法，后面可以根据需求添加
* log：log类封装，本地调试为了方便可以打开log，
```
     #本地调试可以打开，提交代码时关掉
     #logging.root.handlers = [json_console_handler, json_file_handler]
     #默认会添加一个默认的handler,需要移除
     #logging.root.setLevel(LOG_LV)
```
* utility：框架基础方法
* apollocom：配置中心基础类，目前暂时不需要，可以直接写死
```
    #token = yyzx.get_yyzx_token_value
    #service_ip = yyzx.get_yyzx_ip_value
    token = "ea2389592dbe0eda59f38f6f8ebbd396"
    service_ip = "36.134.207.64:19092"
```
* cases：文件夹包括test_cases和test_data，框架使用关键字驱动的概念，所以编写case时需要注意增加同名的case.py和cases.json，
confest会自己去load，具体参考代码实例
* api：定义接口请求
```
    class ProductClient(ApiClient):
        @post(path='/yyzx/product/catalogue/getCatalogueOne')
        def get_catalogue_one(self, id=Noe, name=None):
            """获取产品列表"""

        @get(path='/yyzx/sys/user/info')
        def user_info(self):
            """获取接口信息"""
```
* basacase：封装了assert的方法，框架中可以使用两种asser风格
```
    assert resp.code == 200
    self.assert_equal(data.response, resp.code)
```


hahahha
