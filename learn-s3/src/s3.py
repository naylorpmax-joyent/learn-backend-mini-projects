import sys

import boto3
import botocore.exceptions

import utilities


class S3:
	def __init__(self, client):
		self.client = client

	def put_object(self, bucket, key, local_path):
		data = utilities.read_file(local_path)
		resp = {}
		try:
			resp = self.client.put_object(
				Body=data,
				Bucket=bucket,
				Key=key
			)
		except self.client.exceptions.NoSuchBucket as err:
			# create the bucket
			self.client.create_bucket(Bucket=bucket)

			# retry
			self.put_object(bucket, key, local_path)
			return
		except Exception as err:
			print(f"error putting object in bucket at {bucket}/{key}: {err}")
			sys.exit()

		print(f"Uploaded file at {local_path} to {bucket}/{key}")
		print(f"etag={resp['ETag']}")

	def get_object(self, bucket, key, local_path):
		resp = {}
		try:
			resp = self.client.get_object(
				Bucket=bucket,
				Key=key
			)
		except Exception as err:
			print(f"error getting object from bucket at {bucket}/{key}: {err}")
			sys.exit()

		print(f"Downloaded file to {local_path} from {bucket}/{key}")
		print(f"File's etag is {resp['ETag']}")

		return resp["Body"].read()
