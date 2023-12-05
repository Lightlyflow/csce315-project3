# Deployment
Required software:
- [AWS CLI](https://aws.amazon.com/cli/)
- [Lightsail CTL](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software#install-software-lightsailctl)
- [Docker](https://docs.docker.com/get-docker/)

## New Container
Follow [this link](https://aws.amazon.com/tutorials/serve-a-flask-app/).

## Update existing container
1. Login to AWS on the command line \
   ```aws sso login --profile [profileName]``` or ```aws configure sso``` if first time
    1. Note: Start link will be the one in the Google Docs
    2. Note: Scope is `sso:account:access`
    3. Note: We are using server region `us-east-2`
    4. Note: Output format should be `json`
2. Make sure you are in the project directory
3. Start Docker if it isn't already started (it should be an application if you installed Docker Desktop)
    1. Note: It may take a minute or two to start up
4. Create docker image with tag `flask-container` \
   ```docker build -t flask-container .```
5. Test docker image (make sure to navigate around too) \
   ```docker run -p 5000:5000 flask-container```
6. [Optional] Check container services \
   ```aws lightsail --profile [profile] get-container-services```
    1. If you get aws problems, type in `aws configure sso` to reconfigure aws credentials
7. Push to lightsail container (make sure you are project root) \
   ```aws lightsail --profile [profile] push-container-image --service-name flask-service --label flask-container --image flask-container```
    1. Make sure to note down the new image name: `:flask-service.flask-container.X`, where `X` is a number.
8. Change `image` option in `containers.json` to new image version.
    1. Don't change other options!
9. Update deployment to use latest image
    1. `aws lightsail --profile [profile] create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json`
10. Clean up local docker images/containers
    1. List containers: \
       ```docker ps -a```
    2. Delete a container: \
       ```docker rm <containerID>```
    3. List images: \
       ```docker images```
    4. Delete an image: \
       ```docker rmi <imageID>```
