# Deployment
## New Container
Follow [this link](https://aws.amazon.com/tutorials/serve-a-flask-app/).

## Update existing container
1. Create docker image with tag `flask-container` \
```docker build -t flask-container .```
2. Test docker image (make sure to navigate around too) \
```docker run -p 5000:5000 flask-container```
3. [Optional] Check container services \
```aws lightsail get-container-services```
4. Push to lightsail container (make sure you are project root) \
```aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container```