IMAGE_NAME := discord_bot
LOCAL_TAG := local


build:
	docker build . -t ${IMAGE_NAME}:${LOCAL_TAG}

run: build
	docker run -it --rm ${IMAGE_NAME}:${LOCAL_TAG}
