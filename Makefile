build-container-dev:
	docker build -t leetbot .

build-container:
	docker buildx build --platform=linux/amd64 -t leetbot .

run-container-dev:
	docker run --name=leetbot -d leetbot

run-container:
	docker run --name=leetbot -d leetbot
