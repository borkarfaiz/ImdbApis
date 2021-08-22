# ImdbApis

## About

- Python3.8 is used and other python dependicies listed in requirements.txt.
- MongoDB is used for DB purposes.

## API

- All the API related documentation and endpoints you can find it in [Postman Collectoin.](https://www.getpostman.com/collections/89445c51a4cac6b4399a)
- JWT Authentication is used to authenticate the user.

## Code Deployement

- The code is deployed on AWS and the public ip is http://13.233.83.60/.

## Scaling-Up

- As of now we have single server setup.
- we can create multiple Tiers like Web Tier, Database Tier.
- we can use load balancers to distribute the load among the web Tier where we have multiple web servers to handle the request.
- Database Sharding can be use to distribute the load in Database Tier.
- We can also use Geo-DNS and create multiple centers of our application.
