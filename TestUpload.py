import unittest
from main import image_info
import requests
import asyncio


class TestImageinfo(unittest.TestCase):

    async def test_imageinfo_img(self):
        data = requests.get(
            'https://geol.msu.ru/sites/default/files/%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B8%20%D0%BD%D0%B0%20%D0%9F%D0%93%D0%90%D0%A1%20%28xls%29/obrazec_zayavki.xlsx').text

        self.assertTrue(image_info(data))


if __name__ == "__main__":
    asyncio.run(unittest.main())
