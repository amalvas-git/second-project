import unittest
from hello_world.app import lambda_handler

class SimpleTest(unittest.TestCase):
			
	#def test_message(self):
	#	result=lambda_handler()
	#	self.assertEqual(result, "hellow world")
	def test_lambda_handler(apigw_event, mocker):

    		ret = app.lambda_handler(apigw_event, "")
    		data = json.loads(ret["body"])
    		assert ret["statusCode"] == 200
    		assert "message" in ret["body"]
    		assert data["message"] == "hello world"

if __name__ == '__main__':
	unittest.main()
