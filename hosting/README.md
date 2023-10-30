# Deployment
## New Container
Follow [this link](https://aws.amazon.com/tutorials/serve-a-flask-app/).

## Update existing container
1. Create docker image with tag `flask-container` \
```docker build -t flask-container .```
2. Test docker image (make sure to navigate around too) \
```docker run -p 5000:5000 flask-container```
3. [Optional] Check container services \
```aws lightsail --profile [profile] get-container-services```
4. Push to lightsail container (make sure you are project root) \
```aws lightsail --profile [profile] push-container-image --service-name flask-service --label flask-container --image flask-container```
5. Update `containers.json` to new image version.
6. Clean up local docker images
7. Update deployment to use latest image
   1. `aws lightsail --profile [profile] create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json`
