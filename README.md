## Prerequisities

Before you begin, ensure you have met the following requirements:

#### Install Docker:
* You have a _Windows/Linux/Mac_ machine with the latest version of [Docker](https://www.docker.com/) installed.

## Install/Run with Docker


```shell
docker build -t gowit-backend:latest .
docker run -d -p 5000:5000 gowit-backend
```

or, if you want to give your container a specific name:

```shell
docker build -t gowit-backend:latest .
docker run --name my-flask-sample-one -d -p 5000:5000 gowit-backend
```
The application will be accessible at http://localhost:5000 .
## Usage

### PUT
```shell
curl -d "{\"name\":\"umut\"}" -H "Content-Type: application/json" -X PUT http://localhost:5000/keys

{
  "message": "Object created"
}
```
### GET
```shell
curl -XGET -H "Content-Type: application/json" http://localhost:5000/keys

[
  {
    "id": 1,
    "name": "umut"
  }
]
```
### GET by ID
```shell
curl -XGET -H "Content-Type: application/json" http://localhost:5000/keys/1

[
  {
    "id": 1,
    "name": "umut"
  }
]
```
### DELETE ALL
```shell
curl -XDELETE -H "Content-Type: application/json" http://localhost:5000/keys

{
  "message": "Objects deleted"
}
```
### DELETE by ID
```shell
curl -XDELETE -H "Content-Type: application/json" http://localhost:5000/keys/2
{
  "error": "Object does not exist"
}

curl -XDELETE -H "Content-Type: application/json" http://localhost:5000/keys/1
{
  "message": "Object deleted"
}
```
### HEAD
```shell
curl -X HEAD --head  http://localhost:5000/keys/1

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 37
Server: Werkzeug/1.0.1 Python/3.6.12
Date: Mon, 24 Aug 2020 19:42:22 GMT

curl -X HEAD --head  http://localhost:5000/keys/2

HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 39
Server: Werkzeug/1.0.1 Python/3.6.12
Date: Mon, 24 Aug 2020 19:42:19 GMT

```
## License
[MIT](https://choosealicense.com/licenses/mit/)