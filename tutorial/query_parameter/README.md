### Query Parameters

- Link gốc: https://fastapi.tiangolo.com/tutorial/query-params/

Hiểu đơn giản là bạn có thể khởi tạo theo biến và có thể input vào như bình thường hoặc nhập biến trong path. 

Lưu ý cách nhập biến dựa trên link Url:  
- Dấu ?: Hiểu đơn giản là dấu để phân biệt giữa phần path và biến 
- Dấu &: Dấu để phân biệt giữa các biến với nhau 

Ngoài ra có một số hướng đi mà họ gợi ý trong bài này: 
- Khai báo trước định dạng của các biến -> Tiện lợi cho việc dùng các hàm hỗ trợ cho phần đó 
- Also notice that FastAPI is smart enough to notice that the path parameter item_id is a path parameter and q is not, so, it's a query parameter.
- Khai báo biến bool trong này khá là đa dạng
- Và nó cũng có hiện tượng như unpack một hàm trong vấn đề viết hàm bình thừờng
-> Khuyến khích viết hàm và khai báo sẵn ở phần hàm 