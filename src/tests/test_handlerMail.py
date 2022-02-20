import sys 
import unittest
import boto3
import datetime 
import os
import warnings
warnings.simplefilter("ignore", ResourceWarning)
sys.path.append('src')

from dotenv import load_dotenv
import json
import handlerMail as target
load_dotenv()


def loading_event(tmp_key):
   return {'Records': [
        {'eventVersion': '2.0', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2022-02-20T12: 47: 54.629Z', 'eventName': 
    'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS: 6A083D2429D1F81EB49C9'
            }, 'requestParameters': {'sourceIPAddress': '127.0.0.1'
            }, 'responseElements': {'x-amz-request-id': '2A8671FB76E471D2', 'x-amz-id-2': '4hSj053f1oFXTl8IBmX4OFkiKnxIQnYeRNR5SvNZu6w='
            }, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'testConfigId', 'bucket': {'name': 'local-bucket', 'ownerIdentity': {'principalId': 'E923A4B33E286D'
                    }, 'arn': 'arn:aws:s3: : :local-bucket'
                }, 'object': {'key': tmp_key, 'sequencer': '17F172C9F05', 'size': 464, 'eTag': '71c03db652e8de6d2e30cb5e060a91bd'
                }
            }
        }
    ]
}

class Testing(unittest.TestCase):
 
    def test_save_file(self):   
        s3 = target.createClient()
        #structure for the name of the log object appName-TimeStamp
        log_name = 'log-{:%Y%m%dT%H%M%S}'.format(datetime.datetime.now())
        with open("resources/ex1.csv","rb") as f:
            s3.upload_fileobj(f,os.getenv('BUCKET_NAME'), log_name)
        new_json_response = loading_event(log_name)
        response = target.email(new_json_response,"")
        response = json.loads(response)
        b = [{'luis.zv27@gmail.com': ['20211102T00:00 - APP2 - SUCCESS: No problem here.']}, 
                {'luis.zv27@gmail.com': ['20211105T00:02 - APP2 - ERROR [3]: Severe error.', 
                                        '20211106T00:02 - APP2 - ERROR [1]: Non-severe error.']}]
        self.assertEqual(response, b) 

    def test_no_file(self):   

        log_name = 'log-{:%Y%m%dT%H%M%S}'.format(datetime.datetime.now())
        new_json_response = loading_event(log_name)
        response = target.email(new_json_response,"")
        b = None
        self.assertEqual(response, b) 
if __name__ == '__main__':
    unittest.main()



