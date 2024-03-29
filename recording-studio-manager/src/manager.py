# Python native imports
import os
import sys

# external imports
import boto3
import click

# local imports (any files under ./src/)
import database
import s3
import utilities


@click.group() # https://click.palletsprojects.com/en/8.1.x/api/#click.group
def root():
    pass


@root.command() # https://click.palletsprojects.com/en/8.1.x/api/#click.command
@click.option("--song", type=str, required=True)
@click.option("--track", type=str, required=True)
@click.option("--version", type=str, required=True)
@click.option("--file-path", type=str, required=True)
def upload(song, track, version, file_path):
	""" Upload a new version of an artist's song's track """

	# collect all the information we need to upload a new file
	endpoint_url = os.environ.get("AWS_ENDPOINT", "")
	db_file_path = os.environ.get("DB_FILE_PATH", "")

	bucket_name = os.environ.get("BUCKET_NAME", "")
	artist = os.environ.get("ARTIST_NAME", "")

	# make sure all the required values are valid
	utilities.validate({
		"AWS_ENDPOINT": endpoint_url,
		"BUCKET_NAME": bucket_name,
		"DB_FILE_PATH": db_file_path,
		"ARTIST_NAME": artist,
		"Song name": song,
		"Track name": track,
		"Version tag": version,
		"File path": file_path
	})

	# create an S3 client
	s3_client = s3.S3(boto3.client("s3", endpoint_url=endpoint_url))

	# TODO: put the file into the S3 bucket
	_ = s3.S3(boto3.client("s3", endpoint_url=endpoint_url))

	# TODO: store the metadata in the database
	_ = database.DB(db_file_path)

	print("TODO: Implement me please!")


@root.command()
@click.option("--song", type=str, required=True)
@click.option("--track", type=str, required=True)
@click.option("--version", type=str, required=True)
@click.option("--file-path", type=str, required=True)
def download(song, track, version, file_path):
	""" Download a version of an artist's song's track """

	# collect all the information we need to upload a new file
	endpoint_url = os.environ.get("AWS_ENDPOINT", "")
	db_file_path = os.environ.get("DB_FILE_PATH", "")

	bucket_name = os.environ.get("BUCKET_NAME", "")
	artist = os.environ.get("ARTIST_NAME", "")

	# make sure all the required values are valid
	utilities.validate({
		"AWS_ENDPOINT": endpoint_url,
		"BUCKET_NAME": bucket_name,
		"DB_FILE_PATH": db_file_path,
		"ARTIST_ID": artist,
		"Song name": song,
		"Track name": track,
		"Version tag": version,
		"File path": file_path,
	})

	# TODO: retrieve the metadata from the database
	_ = database.DB(db_file_path)

	# TODO: put the file into the S3 bucket
	_ = s3.S3(boto3.client("s3", endpoint_url=endpoint_url))

	print("TODO: Implement me please!")


if __name__ == "__main__":
    root()
