import unittest
import os

from Scraping import  Spider


class TestSum(unittest.TestCase):
    def test_scrapped_data(self):
        """
        Test test if we scrapped good 5 five items =>> five next pages 
        """
        
        results=list(Spider().parse("https://www.data.gouv.fr/api/1/datasets/?page=3000&page_size=1"))
        self.assertEqual(len(results), 5)

    def test_local_storage_files(self):
        path, dirs, files = next(os.walk("./files"))
        file_count = len(files)
        self.assertEqual(file_count, 5)

if __name__ == '__main__':
    unittest.main()