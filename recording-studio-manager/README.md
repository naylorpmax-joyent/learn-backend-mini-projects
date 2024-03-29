# recording-studio-manager

## Goals

Note: This project is intended to build on the [learn-s3](../learn-s3) and [learn-sqlite](../learn-sqlite) projects and use some of the same skills for a new project.

You are building an application for a music production studio manager who wants to help artists store and keep track of their recordings.

Each artist will be recording various tracks for each of their songs. (In a typical song recording, a "track" usually contains the recording of a specific instrument, a specific vocalist's vocals, etc - and to release a song, the producer will smash the tracks together, more or less.)

As an artist is working on their recordings, they want to be able to save different versions of each of their track, so that they can eventually choose the best versions of each track to be included in the song's final release.

For a more detailed list of requirements for the application, check out the *Challenges* section.

*Note for clarity: Artists can record many songs; songs can involve many tracks; and tracks can have many versions.*

## Setup

- Install [Docker Desktop](https://docs.docker.com/desktop/)
- Install [Python](https://www.python.org/downloads/) if you haven't done so already
- Create a virtual environment named `recording_studio_venv` (or whatever you'd like to call it)

```bash
python3 -m venv recording_studio_venv
```
- Activate the virtual environment:

```bash
# Windows - in cmd.exe
recording_studio_venv\Scripts\activate.bat

# Windows - in PowerShell
recording_studio_venv\Scripts\Activate.ps1

# Linux/Mac
source recording_studio_venv/bin/activate
```

- Install the project's Python dependencies

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

- Here are some example commands we expect the music production studio manager to use - but they don't work yet! (These examples assume you to be in this directory / folder.)

```bash
# upload a file
python src/manager.py upload \
	--song "Evan Enters the Third Room" \
	--track "DJ's Drums" \
	--file-path "resources/evan_third_room_dj_drums_demo.wav" \
	--version "demo"
```

> `TODO: Implement me please!

```bash
# upload another file (three takes later...)
python src/manager.py upload \
	--song "Evan Enters the Third Room" \
	--track "DJ's Drums" \
	--file-path "resources/evan_third_room_dj_drums_third_take.wav" \
	--version "take_three"
```
> `TODO: Implement me please!

```python
# download the final version!
python src/manager.py download \
	--song "Evan Enters the Third Room" \
	--track "DJ's Drums" \
	--file-path "resources/FINAL_evan_third_room_drums.wav" \
	--version "take_three"
```
> `TODO: Implement me please!

## Challenges

Right now, we have a project structure with some placeholder functions that aren't fully implemented. We would like to enable the application to support the following features.

### Upload

Given a song, track, and version tag, upload a file that contains a new version of the song's tracks. The file should be uploaded to S3. When the artist uploads it, we also want to keep track of the file in our database behind-the-scenes.

The database record should include:

- The unique remote location ("key") of the file ("object")
- Identifying metadata fields that would enable the artist to retrieve the file later when they're ready to construct the final version of a song:
	- Artist
	- Song
	- Track
	- Version tag
	- Original local file path (e.g. `resources/evan_third_room_dj_drums_third_take.wav`)
	- Upload time

### Download

Given a song, track, and version tag, retrieve the S3 location from the database, download the correct file from S3, and save it locally for the artist.

### List Songs

It could also be helpful for artists to be able to see which recordings they've already stored remotely - given different parameters (for example, an artist; an artist and a song title; an artist, song title, and track; etc), lookup and display the list of recordings the artist has uploaded, including the original local file path (e.g. `resources/evan_third_room_dj_drums_third_take.wav`).

## Remaining TODOs (Max)

- [ ] Create a database schema - could take loose inspiration from the chinook database in the [learn-sqlite](../learn-sqlite) project. Alternatively, maybe this could be a good exercise in itself?
- [ ] Create some sample data for the database
- [ ] Flesh out the resources section as-needed
- [ ] Validate ETags to monitor for data corruption?

## Resources

- [boto3 client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
