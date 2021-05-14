 ### POST 
    curl -d '{"title":"title", "image":"image"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/products

### POST 
    curl -d '{"title":"title", "image":"image"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/products

 ### GET 
     curl GET http://localhost:8000/api/products/1 

 ### DELETE 
     curl DELETE http://localhost:8000/api/products/1 

 ### GET_ALL PRODUCTS
     curl http://localhost:8000/api/products


### POST LIKE
    curl -H "Content-Type: application/json" -X POST http://localhost:8001/api/products/17/like
