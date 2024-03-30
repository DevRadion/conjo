from docker_engine.docker_engine import DockerEngine

if __name__ == '__main__':
    # Currently supports only docker installation
    docker_engine = DockerEngine()
    docker_engine.install_docker_engine()
