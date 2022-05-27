import allure

from api.yyzx_client import ProductClient
from client import ApiClient


class TestProduct(ApiClient):
    @classmethod
    def setup_class(cls):
        cls.YYZXClient = ProductClient()

    @allure.step("测试产品分类")
    def test_get_catalogue_one(self, data):
        resp = self.YYZXClient.get_catalogue_one(**data.params)
        # LOGGER.info(resp)
        assert resp.code == 200
        self.assert_equal(data.response, resp.code)

    # @allure.step("获取用户信息")
    # def test_user_info(self):
    #     resp = self.client.userInfo()
    #     print(resp)
    #     # assert int(resp['code']) == 200
    #
    # @allure.step("获取列表信息")
    # def test_get_list(self):
    #     resp = self.client.getlist()
    #     print(resp)
