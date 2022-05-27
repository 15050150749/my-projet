from client import ApiClient, post, get


class ProductClient(ApiClient):

    @post(path='/yyzx/product/catalogue/getCatalogueOne')
    def get_catalogue_one(self, **kwargs):
        # def get_catalogue_one(self, id=Noe,name=None):
        """获取产品列表"""

    @get(path='/yyzx/sys/user/info')
    def user_info(self):
        """获取接口信息"""

    @post(path='/yyzx/product/getList')
    def get_list(self):
        """获取列表"""
