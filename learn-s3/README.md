# learn-s3

## Goals

- Get a Minio instance set up locally - Minio is an alternative backend that is compatible with Amazon's S3 API that can be run on your computer. You can use any of the same libraries that you would use against the S3 service - which makes it perfect for learning S3 without having to sign up for an Amazon account.
- Get some exposure to Docker and docker-compose (see resources to learn more about Docker)
- Write some Python CLI (command line interface) commands that wrap essential S3 operations

## Setup

- Install [Docker Desktop](https://docs.docker.com/desktop/)
- Install [Python](https://www.python.org/downloads/) if you haven't done so already
- Create a virtual environment named `storage_venv` (or whatever you'd like to call it)

```bash
python3 -m venv storage_venv
```
- Activate the virtual environment:

```bash
# Windows - in cmd.exe
storage_venv\Scripts\activate.bat

# Windows - in PowerShell
storage_venv\Scripts\Activate.ps1

# Linux/Mac
source storage_venv/bin/activate
```

- Install the project's Python dependencies in the virtual environment

```bash
pip install -r requirements.txt
```

- (Optional) Install `direnv` tool or another environment variable manager ([Direnv](https://direnv.net/), [Direnv for Windows](https://gist.github.com/rmtuckerphx/4ace28c1605300462340ffa7b7001c6d))

## Trying it out

- Start the Minio Docker container

```bash
docker compose up
```

- Open the Minio UI in your web browser at http://localhost:9001 and login (see the docker-compose.yml - current values are `minioadmin` and `supersecret`, but you can change these if you'd like). This will let you view your buckets, objects, and more! It is very similar to the AWS S3 Console, just looks different.

- In a new command line shell/terminal, set your environment variables

```bash
# using direnv on Linux/Mac
echo 'export AWS_ENDPOINT="http://localhost:9000"
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="storageadmin"
export AWS_SECRET_ACCESS_KEY="supersecret"'> .envrc
direnv allow
```

- Give it a whirl! Here are some example commands to get you started - run them in a shell that has your environment variables set. These examples assume you to be in this directory / folder.

**Upload a file to remote storage**

```bash
python src/storage.py put-object \
	--bucket "music" \
	--key "lyrics" \
	--file-path "resources/little_simz-gorilla.txt"
```

> ```
> Uploaded file at resources/little_simz-gorilla.txt to music/lyrics
> etag="4368ca0faa6e5c78e53753cf4ba47a7d"
> ```

**Download the file back to your local computer**

```bash
python src/storage.py get-object \
	--bucket "music" \
	--key "lyrics" \
	--file-path "resources/little_simz-gorilla_DOWNLOADED.txt"
```

## Challenges

- Create a new command that deletes an object from S3
- Create a new `list` command that lists all of the objects in a bucket at a key prefix
- Create a new `count` command that counts the objects in a bucket at a key prefix
- Update your list and count commands to use pagination; test these by generating and uploading a lot of objects to the same prefix and trying to count them. (See the resources for help with pagination.)

## Resources

**S3**

- [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [boto3 documentation for the S3 ListObjectsV2 paginator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/paginator/ListObjectsV2.html))
- (Optional) The [AWS S3 API CLI](https://docs.aws.amazon.com/cli/latest/reference/s3api/) is probably the simplest way to interact with S3, and may be helpful for understanding different operations if you'd like to play around with it.

**Docker**

- [Docker overview video by Simplilearn](https://www.youtube.com/watch?v=rOTqprHv1YE) - the instructor has clear explanations, helpful visuals, a very calming voice, and is only 15 minutes long
- The official [Docker overview](https://docs.docker.com/get-started/overview/) is also quite helpful if you'd prefer to read
