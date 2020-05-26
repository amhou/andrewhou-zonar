DOCKER               ?= docker
DOCKER_COMPOSE       ?= docker-compose

default_target: initialize

initialize:
	$(MAKE) pull
	$(MAKE) build
	@echo "Images are prepped. Run 'make start'."

build: pull
	@echo "Building base"
	@${DOCKER_COMPOSE} build --pull base

pull:
	@echo "Pulling all images"
	@${DOCKER_COMPOSE} pull --ignore-pull-failures

shell:
	@echo "Getting you a shell"
	@${DOCKER_COMPOSE} run shell

start:
	@echo "Starting Language App"
	@${DOCKER_COMPOSE} up -d language_app

down:
	@${DOCKER_COMPOSE} down

test:
	@${DOCKER_COMPOSE} run shell pytest
