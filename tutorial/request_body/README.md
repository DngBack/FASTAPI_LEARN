## Request Body 

When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.

-> Quay lại quy trình làm việc của client và API, ở những bài trước chúng ta đã được làm quen với lệnh get, hiểu đơn giản na ná lệnh select trả về một resource hoặc một danh dách resource nhưng trong thực tế thì không phải có cứ tự nhiện nhảy ra kết quả mà cần thêm đầu vào nữa. 
-> Lúc này cần tuân theo request body 

A request body is data sent by the client to your API. A response body is the data your API sends to the client.

--> Cái này làm rõ hơn về hai khái niệm request và response

Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

--> Sử dụng Pydanic để định nghĩa request body

To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.

Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using GET, and proxies in the middle might not support it.

**Request body + path parameters**

You can declare path parameters and request body at the same time.

FastAPI will recognize that the function parameters that match path parameters should be taken from the path, and that function parameters that are declared to be Pydantic models should be taken from the request body.

**Request body + path + query parameters**

You can also declare body, path and query parameters, all at the same time.

FastAPI will recognize each of them and take the data from the correct place.