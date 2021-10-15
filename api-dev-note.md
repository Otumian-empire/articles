# How to design a REST API

## What is a REST API

## Why use REST API

## Steps in designing REST Services

1. Identify Object Model

   Identifying the _objects_ which will be presented as _resources_. We will consider only two resources i.e.

   - Users
   - Products

   These resources will have a unique identifier, `id`

2. Create Model URIs

   These resource URIs are _endpoints_ for RESTful services.

   Example:

   ```
   /users
   /users/{id}

   /products
   /products/{id}

   /users/{id}/products
   /users/{id}/products/{id}
   ```

   Use Plurals for resource urls and use nouns and NOT the verbs
   Just like the above and not /getAllProducts or /getProduct/{id}
   The HTTP methods describes the end point

   this, /products avoids /product/all and even /product may even
   give the idea of reading a single object

3. Determine Representations/format
   how the data is composed, as JSON or XML. Use JSON

4. Use of right HTTP methods

   | Verb          | Meaning                                                           |
   | ------------- | ----------------------------------------------------------------- |
   | **GET**       |   To get a resource or collection of resources.                   |
   | **POST**      |   To create a resource or collection of resources.                |
   | **PUT/PATCH** |  To update the existing resource or collection of resources.      |
   | **DELETE**    |   To delete the existing resource or the collection of resources. |

5. Use parameters

   - `/products?name=ABC` should be preffered over `/getProductsByName`
   - `/products?type=xyz` should be preferred over `/getProductsByType`

   This is help avoid long urls.

6. Use proper HTTP codes
   | | | |
   |-------|------|-----|
   | 200 | OK  |  This is most commonly used HTTP code to show that the operation performed is successful. |
   | 201 | CREATED  |  This can be used when you use POST method to create a new resource. |
   | 202 | ACCEPTED  |  This can be used to acknowledge the request sent to the server.|
   | 400 | BAD REQUEST  |  This can be used when client side input validation fails. |
   | 401 / 403 | UNAUTHORIZED / FORBIDDEN | This can be used if the user or the system is not authorised to perform certain operation. |
   | 404 | NOT FOUND | This can be used if you are looking for certain resource and it is not available in the system. |
   | 500 | INTERNAL SERVER ERROR  |  This should never be thrown explicitly but might occur if the system fails. |
   | 502 | BAD GATEWAY  |  This can be used if server received an invalid response from the upstream server. |

7. Versioning
   use versions as dates or query parameters

   - `/v1/products`
   - `/v2/products`

   Avoid the use of dot `( . )` in the version, as in `/v1.2/products`

8. Use Pagination

   - Use of pagination is a must when you expose an API which might return huge data. If proper load balancing is not done, then a consumer might end up bringing down the service.

   - Use of limit and offset is recommended here. For example, `/products?limit=25&offset=50`
   - It is also advised to keep a default limit and default offset.

9. Use Proper Error Messages

   ```JSON
   {
    "error": {
      "message": "(#803) Some of the aliases you requested do not exist: products",
      "type": "OAuthException",
      "code": 803,
      "fbtrace_id": "FOXX2AhLh80"
    }

   }
   ```

10. Use of Open API specifications.
    A system such as swagger could be used to design the api before implementation.

## Resource

- How to design a REST API - [restfulapi-net]
- RESTful API Design - Step By Step Guide - [hackernoon-com]
- List of HTTP codes - [wikipedia-ord]
- Swagger - [swagger-io]

#

[restfulapi-net]: https://restfulapi.net/rest-api-design-tutorial-with-example/
[hackernoon-com]: https://hackernoon.com/restful-api-design-step-by-step-guide-2f2c9f9fcdbf
[wikipedia-ord]: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
[swagger-io]: https://swagger.io/resources/open-api/
