import docker
from docker import (DockerClient)
from typing import List
def pull_docker_images()-> None:
	client: DockerClient = docker.from_env()
	image_list: List = ["redis:latest", "nginx:latest"]
	for image in image_list:
		print("Pulling image {}".format(image))
		client.images.pull(image)

if __name__ == "__main__":
	pull_docker_images()
