docker build -t jenkin .
docker run --name jenkins-data jenkin echo "Jenkins Data Container"

docker run -d --name jenkins -p 8080:8080 --volumes-from jenkins-data -v /var/run/docker.sock:/var/run/docker.sock jenkin