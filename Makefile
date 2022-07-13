build-container-dev:
	docker build -t leetcode-discord-bot-dev .

build-container:
	docker buildx build --platform=linux/amd64 -t leetcode-discord-bot .

run-container-dev:
	docker run --name=leetcode-discord-bot-dev -d leetcode-discord-bot-dev

run-container:
	docker run --name=leetcode-discord-bot -d leetcode-discord-bot
