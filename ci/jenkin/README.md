This Dockerfile takes the Jenkins base image, installs the Docker binary, and adds
password-less sudo rights to the jenkins user. We intentionally haven’t added jen
kins to the Docker group, so we will have to prefix all our Docker commands with
sudo.