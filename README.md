# Telegram Bot + MongoDB

## Config

**Important!** 

> WARNING (Windows & OS X): The default Docker setup on Windows and OS X uses a VirtualBox VM to host the Docker daemon. Unfortunately, the mechanism VirtualBox uses to share folders between the host system and the Docker container is not compatible with the memory mapped files used by MongoDB (see vbox bug, docs.mongodb.org and related jira.mongodb.org bug). This means that it is not possible to run a MongoDB container with the data directory mapped to the host.

Source: [mongo - Docker Hub](https://registry.hub.docker.com/_/mongo/)

To solve this you should create a external volume

`$ docker volume create mongodata`

_mongodata_ is the volume name that I use in [docker-compose.yml](https://github.com/Mixtomeister/mongobot/blob/master/docker-compose.yml).