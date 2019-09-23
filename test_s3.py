import unittest

from moto import mock_s3
from secode import get_client, list_s3_buckets, list_s3_objects

class s3testcase(unittest.TestCase):
    def setUp(self):
        """setup will run before execution of each teat case"""
 
        self.bucket = 'a3windows'
        self.key = '0531dadc-8ade-4ba0-b8f0-3b6fb0b420c9/i-059e521a38ba0e966/awsrunPowerShellScript/PatchWindows/stdout'

    @mock_s3
    def __moto_setup(self):
        s3 = get_client()
        s3.create_bucket(Bucket=self.bucket)
        s3.put_object(Bucket=self.bucket, Key=self.key) 
 
    def test_get_client(self):
        """check out connect_client function has a valid endpoint"""
        s3 = get_client()
        self.assertEqual(s3._endpoint.host, 'https://s3.amazonaws.com')
 
    @mock_s3
    def test_list_s3_buckets(self):
        """check bucket shows as expected"""
        self.__moto_setup()
        buckets = [b for b in list_s3_buckets()]
        self.assertTrue(self.bucket in buckets)
   
    @mock_s3
    def test_list_s3_objects(self):
        """check object is in bucket as expected"""
        self.__moto_setup()
        objects = [o for o in list_s3_objects(self.bucket)]
        self.assertTrue(self.key in objects)
 
 
    @mock_s3
    def test_main(self):
        '''verifies the execution'''
        self.__moto_setup()


if __name__ == "__main__":
    unittest.main()
