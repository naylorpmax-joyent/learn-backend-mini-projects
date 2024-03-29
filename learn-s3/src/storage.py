# Python native imports
import os
import sys

# external imports
import boto3
import click

# local imports (any files under ./src/)
import s3
import utilities


@click.group() # https://click.palletsprojects.com/en/8.1.x/api/#click.group
def root():
    pass


@root.command() # https://click.palletsprojects.com/en/8.1.x/api/#click.command
@click.option("--bucket", type=str, required=True)
@click.option("--key", type=str, required=True)
@click.option("--file-path", type=str, required=True)
def put_object(bucket, key, file_path):
	""" Upload a file to remote storage """
	endpoint_url = os.environ.get("AWS_ENDPOINT", "")

	# make sure all the required values are valid
	utilities.validate({
		"AWS_ENDPOINT": endpoint_url,
		"Bucket": bucket,
		"Key": key,
		"File path": file_path
	})

	# create an S3 client
	s3_client = s3.S3(boto3.client("s3", endpoint_url=endpoint_url))

	# put the file into the S3 bucket
	s3_client.put_object(bucket, key, file_path)


@root.command()
@click.option("--bucket", type=str, required=True)
@click.option("--key", type=str, required=True)
@click.option("--file-path", type=str, required=True)
def get_object(bucket, key, file_path):
	""" Download a file from remote storage """

	# collect all the information we need to upload a new file
	endpoint_url = os.environ.get("AWS_ENDPOINT", "")

	# make sure all the required values are valid
	utilities.validate({
		"AWS_ENDPOINT": endpoint_url,
		"Bucket": bucket,
		"Key": key,
		"File path": file_path
	})

	# create an S3 client
	s3_client = s3.S3(boto3.client("s3", endpoint_url=endpoint_url))

	# put the file into the S3 bucket
	data = s3_client.get_object(bucket, key, file_path)
	utilities.write_file(data.decode(), file_path)


if __name__ == "__main__":
    root()
