echo "Start UniFi Docker Update"
docker stop unifi-controller
docker pull jacobalberty/unifi:latest
docker rm unifi-controller
docker run -d --init --restart=unless-stopped --name=unifi-controller --net=host --volume=/volume1/docker/unifi:/var/lib/unifi -p 8080:8080/tcp -p 8081:8081/tcp -p 8443:8443/tcp -p 8843:8843/tcp -p 8880:8880/tcp -p 8883:8883/tcp -p 3478:3478/udp jacobalberty/unifi:latest
echo "End UniFi Docker Update"