# Final Report - Mini App Quản Lý Đơn Hàng Cho Shop Online

## 1. Use Case Diagram
![](https://github.com/httthaor/Nhom2-CNPM/blob/66d62bbccd0439a7e23efbbfb76474896126f055/Labs/Lab02/UseCaseDiagram.jpg)

**Use Case Description:**

**1. Use Case: Add Product**\
**Actor:** Admin\
**Mô tả:** Admin thêm sản phẩm mới vào hệ thống.\
**Điều kiện tiên quyết:** Admin đã đăng nhập.\
**Luồng chính:**\
Admin nhập thông tin sản phẩm (tên, giá, danh mục, tồn kho).\
Hệ thống kiểm tra dữ liệu, lưu vào cơ sở dữ liệu.\
Thông báo thành công.\
**Luồng phụ:**\
Dữ liệu không hợp lệ: Hiển thị lỗi, yêu cầu nhập lại.\
Kết quả: Sản phẩm mới được thêm.

**2. Use Case: Search Product**\
**Actor:** Customer, Admin\
**Mô tả:** Tìm kiếm sản phẩm theo tên, danh mục, hoặc giá.\
**Điều kiện tiên quyết:** Có sản phẩm trong hệ thống.\
**Luồng chính:**\
Actor nhập từ khóa tìm kiếm.\
Hệ thống trả về danh sách sản phẩm.\
**Luồng phụ:**\
Không tìm thấy: Hiển thị “Không có kết quả”.\
Kết quả: Hiển thị danh sách sản phẩm phù hợp.

**3. Use Case: Register**\
**Actor:** Customer\
**Mô tả:** Khách hàng đăng ký tài khoản.\
**Điều kiện tiên quyết:** Chưa có tài khoản.\
**Luồng chính:**\
Khách hàng nhập username, password, email.\
Hệ thống kiểm tra, mã hóa password, lưu tài khoản.\
Thông báo thành công.\
**Luồng phụ:**\
Username/email trùng: Hiển thị lỗi.\
Kết quả: Tài khoản được tạo.

**4. Use Case: Login**\
**Actor:** Customer\
**Mô tả:** Khách hàng đăng nhập vào hệ thống.\
**Điều kiện tiên quyết:** Có tài khoản.\
**Luồng chính:**\
Khách hàng nhập username, password.\
Hệ thống xác thực, trả JWT token.\
Chuyển hướng đến trang chủ.\
**Luồng phụ:**\
Sai thông tin: Hiển thị lỗi.\
Kết quả: Đăng nhập thành công, nhận token.

**5. Use Case: Add Product to Cart**\
**Actor:** Customer\
**Mô tả:** Thêm sản phẩm vào giỏ hàng.\
**Điều kiện tiên quyết:** Đã đăng nhập, sản phẩm tồn tại.\
**Luồng chính:**\
Khách hàng chọn sản phẩm, thêm vào giỏ.\
Hệ thống kiểm tra tồn kho, cập nhật giỏ hàng.\
Thông báo thành công.\
**Luồng phụ:**\
Hết hàng: Hiển thị lỗi.\
Kết quả: Sản phẩm được thêm vào giỏ.

**6. Use Case: Create Order**
**Actor:** Customer\
**Mô tả:** Tạo đơn hàng từ giỏ hàng.\
**Điều kiện tiên quyết:** Đã đăng nhập, giỏ hàng không rỗng.\
**Luồng chính:**\
Khách hàng xác nhận đặt hàng.\
Hệ thống tính tổng tiền, tạo đơn hàng, cập nhật tồn kho.\
Thông báo thành công.\
**Luồng phụ:**\
Giỏ hàng rỗng: Hiển thị lỗi.\
Kết quả: Đơn hàng được tạo.

**7. Use Case: Process Payment**\
**Actor:** Customer\
**Mô tả:** Thanh toán đơn hàng bằng COD hoặc ví điện tử.\
**Điều kiện tiên quyết:** Có đơn hàng.\
**Luồng chính:**\
Khách hàng chọn phương thức thanh toán (COD/ví điện tử).\
Hệ thống xử lý\
Thông báo thanh toán thành công.\
**Luồng phụ:**\
Thanh toán thất bại: Hiển thị lỗi.\
Kết quả: Thanh toán hoàn tất.

**8. Use Case: View Product Catalog**\
**Actor:** Customer\
**Mô tả:** Xem danh sách sản phẩm và danh mục.\
**Điều kiện tiên quyết:** Có sản phẩm trong hệ thống.\
**Luồng chính:**\
Khách hàng truy cập trang danh mục sản phẩm.\
Hệ thống hiển thị sản phẩm và danh mục\
**Luồng phụ:**\
Không có sản phẩm: Hiển thị thông báo trống.\
Kết quả: Hiển thị danh sách sản phẩm.

## 2. Sequence Diagram
![](https://github.com/httthaor/Nhom2-CNPM/blob/b85866ac277e57131529fc31824cfbd7e224a3a3/Labs/Lab03/SequenceDiagram.jpg)

Quy trình nghiệp vụ được chọn để mô tả chi tiết là: **"Cập nhật trạng thái vận chuyển của đơn hàng"**

Sơ đồ mô tả luồng tương tác chi tiết giữa các đối tượng trong hệ thống khi Chủ Shop thực hiện chức năng này.

**Các đối tượng tham gia:**\
•	**:Chủ Shop:** Người dùng cuối, người bắt đầu tương tác.\
•	**:Giao diện (UI):** Lớp giao diện người dùng mà Chủ Shop tương tác.\
•	**:OrderController:** Lớp điều khiển, nhận yêu cầu từ giao diện.\
•	**:OrderService:** Lớp xử lý logic nghiệp vụ chính.\
•	**:Database:** Cơ sở dữ liệu lưu trữ thông tin.\
•	**:NotificationService:** Dịch vụ chịu trách nhiệm gửi thông báo đến khách hàng.

## 3. Class Diagram
![](https://github.com/httthaor/Nhom2-CNPM/blob/905757ceee786aadbd160bc9f77912a9cd1df37e/Labs/Lab06/ClassDiagram.jpg)

```
@startuml
' Các package để tổ chức class
package "Product Management" {
  class Product {
    -id: String
    -name: String
    -price: double
    -category: String
    -stock: int
    +addProduct()
    +updateProduct()
    +deleteProduct()
    +searchProduct()
    +displayProducts()
  }

  class Category {
    -id: String
    -name: String
    +addCategory()
    +updateCategory()
    +deleteCategory()
    +displayCategories()
  }
}

package "Customer Management" {
  class Customer {
    -id: String
    -username: String
    -password: String
    -email: String
    -address: String
    +register()
    +login()
    +updateInfo()
  }
}

package "Cart Management" {
  class Cart {
    -cartId: String
    -customer: Customer
    -items: List<CartItem>
    +addItem()
    +removeItem()
    +calculateTotal()
  }

  class CartItem {
    -product: Product
    -quantity: int
    +updateQuantity()
  }
}

package "Order Management" {
  class Order {
    -orderId: String
    -customer: Customer
    -items: List<OrderItem>
    -status: String
    -total: double
    +createOrder()
    +updateStatus()
  }

  class OrderItem {
    -product: Product
    -quantity: int
  }
}

package "Payment Management" {
  class Payment {
    -paymentId: String
    -order: Order
    -method: String
    -amount: double
    +processCOD()
    +processEWallet()
  }
}

package "User Interface" {
  class HomePage {
    +display()
  }

  class ProductPage {
    +displayProducts()
    +filterByCategory()
  }

  class CartPage {
    +displayCart()
    +updateCart()
  }

  class OrderPage {
    +displayOrders()
    +trackOrder()
  }
}

' Quan hệ giữa các class
Product "1" --o "many" CartItem
Product "1" --o "many" OrderItem
Customer "1" --o "1" Cart
Customer "1" --o "many" Order
Cart "1" --o "many" CartItem
Order "1" --o "many" OrderItem
Order "1" --o "1" Payment
Category "1" --o "many" Product

@enduml
```
## 4. ERD + DB

**Database**
```
CREATE TABLE `Customer` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50),
  `password` varchar(100),
  `email` varchar(100) UNIQUE,
  `address` varchar(255)
);

CREATE TABLE `Category` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(100)
);

CREATE TABLE `Product` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(100),
  `price` decimal(10,2),
  `stock` int,
  `categoryId` int
);

CREATE TABLE `Cart` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `customerId` int
);

CREATE TABLE `CartItem` (
  `cartId` int,
  `productId` int,
  `quantity` int,
  PRIMARY KEY (`cartId`, `productId`)
);

CREATE TABLE `Order` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `customerId` int,
  `status` varchar(50),
  `total` decimal(10,2)
);

CREATE TABLE `OrderItem` (
  `orderId` int,
  `productId` int,
  `quantity` int,
  PRIMARY KEY (`orderId`, `productId`)
);

CREATE TABLE `Payment` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `orderId` int,
  `method` varchar(50),
  `amount` decimal(10,2)
);

ALTER TABLE `Product` ADD FOREIGN KEY (`categoryId`) REFERENCES `Category` (`id`);

ALTER TABLE `Cart` ADD FOREIGN KEY (`customerId`) REFERENCES `Customer` (`id`);

ALTER TABLE `CartItem` ADD FOREIGN KEY (`cartId`) REFERENCES `Cart` (`id`);

ALTER TABLE `CartItem` ADD FOREIGN KEY (`productId`) REFERENCES `Product` (`id`);

ALTER TABLE `Order` ADD FOREIGN KEY (`customerId`) REFERENCES `Customer` (`id`);

ALTER TABLE `OrderItem` ADD FOREIGN KEY (`orderId`) REFERENCES `Order` (`id`);

ALTER TABLE `OrderItem` ADD FOREIGN KEY (`productId`) REFERENCES `Product` (`id`);

ALTER TABLE `Payment` ADD FOREIGN KEY (`orderId`) REFERENCES `Order` (`id`);
```
**Mô tả các entity chính:**
- Customer (id PK, username, password, email, address)
- Category (id PK, name)
- Product (id PK, name, price, stock, categoryId FK→Category.id)
- Cart (id PK, customerId FK→Customer.id)
- CartItem (cartId FK→Cart.id, productId FK→Product.id, quantity, PK(cartId, productId))
- Order (id PK, customerId FK→Customer.id, status, total)
- OrderItem (orderId FK→Order.id, productId FK→Product.id, quantity, PK(orderId, productId))
- Payment (id PK, orderId FK→Order.id, method, amount)

**ERD**

![]()

## 5. Form Login

**Giao diện đăng nhập:**

![](https://github.com/httthaor/Nhom2-CNPM/blob/b85866ac277e57131529fc31824cfbd7e224a3a3/Labs/Lab04/FormLogin.jpg)

**Code:**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Login</title>
    <style>
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #0258cf88;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.cancel {
  width: auto;
  padding: 10px 18px;
  background-color: #e90a0a;
}

.login-form {
  padding: 16px;
}

span.password {
  float: right;
  padding-top: 16px;
}

a:link{
    color: #000000e4;
}

a:hover{
    color:#b11414;
}

a:visited{
    color:#0258cf88;
}

@media screen and (max-width: 300px) {
  span.password {
     display: block;
     float: none;
  }
  .cancel {
     width: 100%;
  }
}
    </style>
</head>
<body>
    <h2 style="text-align: center;">LOGIN FORM</h2>
    <div class="login-form">
        <form>
            <label for="username"><b>Username</b></label>
            <input type="text" name="username" placeholder="Enter your username" required>
            <label for="password"><b>Password</b></label>
            <input type="password" name="password" placeholder="Enter your password" required>
            <button type="submit">Login</button>
            <input type="checkbox" checked="checked" name="remember"> Remember me
            <br/>
            <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancel">Cancel</button>
            <span class="password"><a href="#">Forgot password?</a></span>
    </form>
    </div>
</body>
</html>
```

## 6. Order Management Module

```
# file: order_management_module.py
import mysql.connector

# --- Cấu hình kết nối CSDL ---
DB_CONFIG = {
    'user': 'root',
    'password': 'sa123', # <-- Config lại password
    'host': '127.0.0.1',
    'database': 'shop_order_management' 
}

def get_db_connection():
    """Tạo và trả về một kết nối CSDL."""
    return mysql.connector.connect(**DB_CONFIG)

class NotificationService:
    """Lớp giả lập dịch vụ gửi thông báo."""
    def send_update_notification(self, customer_id, new_status):
        # Mô phỏng gửi noti
        print(f"--- NotificationService: Đã gửi thông báo cho khách hàng (ID: {customer_id}) về trạng thái mới: '{new_status}'")
        return True

class OrderService:
    """Lớp chứa logic nghiệp vụ chính liên quan đến đơn hàng."""
    def __init__(self):
        self.notification_service = NotificationService()

    def update_order_status(self, order_id, new_status):
        """Cập nhật trạng thái của một đơn hàng và gửi thông báo."""
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Bắt đầu transaction
            conn.start_transaction()

            # 1. Lấy thông tin customer_id để gửi thông báo sau này
            cursor.execute("SELECT customer_id FROM orders WHERE order_id = %s", (order_id,))
            result = cursor.fetchone()
            if not result:
                raise Exception(f"Không tìm thấy đơn hàng với ID: {order_id}")
            customer_id = result[0]

            # 2. Cập nhật trạng thái trong CSDL
            print(f"--- OrderService: Đang cập nhật trạng thái đơn hàng {order_id} thành '{new_status}'...")
            update_query = "UPDATE orders SET status = %s WHERE order_id = %s"
            cursor.execute(update_query, (new_status, order_id))
            
            # Kiểm tra xem có dòng nào được cập nhật không
            if cursor.rowcount == 0:
                 raise Exception(f"Cập nhật thất bại, có thể ID đơn hàng {order_id} không tồn tại.")

            # 3. Gửi thông báo cho khách hàng
            self.notification_service.send_update_notification(customer_id, new_status)

            # 4. Commit transaction nếu mọi thứ thành công
            conn.commit()
            print(f"--- OrderService: Cập nhật đơn hàng {order_id} thành công!")
            return True

        except Exception as e:
            print(f"--- OrderService: Đã xảy ra lỗi! {e}")
            if conn:
                # Rollback để hủy bỏ mọi thay đổi nếu có lỗi
                conn.rollback()
            return False
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

class OrderController:
    """Lớp điều phối, nhận yêu cầu từ giao diện."""
    def __init__(self):
        self.order_service = OrderService()

    def request_update_status(self, order_id, new_status):
        print(f"\n[Controller] Nhận yêu cầu cập nhật trạng thái cho đơn hàng #{order_id} thành '{new_status}'")
        success = self.order_service.update_order_status(order_id, new_status)
        if success:
            print(f"[Controller] Phản hồi: Thành công.")
        else:
            print(f"[Controller] Phản hồi: Thất bại.")
        return success

# --- Main: Đoạn code để chạy thử nghiệm ---
if __name__ == "__main__":
    # Để chạy thử, hãy đảm bảo bạn có một đơn hàng trong CSDL trước.
    # Chạy script SQL để tạo 1 đơn hàng mẫu.
    # INSERT INTO orders (customer_id, user_id, total_amount) VALUES (1, 1, 500000.00);
    # Giả sử đơn hàng này có order_id = 1
    
    order_controller = OrderController()
    
    # Kịch bản 1: Cập nhật thành công
    order_controller.request_update_status(order_id=1, new_status='Shipped')
    
    # Kịch bản 2: Cập nhật cho một đơn hàng không tồn tại
    order_controller.request_update_status(order_id=999, new_status='Cancelled')
```
![](https://github.com/httthaor/Nhom2-CNPM/blob/905757ceee786aadbd160bc9f77912a9cd1df37e/Labs/Lab07/Lab07_Scr.png)
![](https://github.com/httthaor/Nhom2-CNPM/blob/905757ceee786aadbd160bc9f77912a9cd1df37e/Labs/Lab07/Lab07_Scr01.png)

## 7. Test

```
# file: test_order_management.py
import pytest
from unittest.mock import patch, MagicMock
import mysql.connector

# --- Cấu hình để import module từ thư mục lab07 ---
import sys
import os
lab07_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lab07-management'))
sys.path.insert(0, lab07_path)

# Bây giờ mới import module
import order_management_module

# --- Bắt đầu viết Test ---

@pytest.fixture
def mock_services():
    """Fixture để giả lập CSDL và NotificationService."""
    with patch('order_management_module.get_db_connection') as mock_get_conn:
        # Giả lập connection và cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        
        # === DÒNG SỬA LỖI ĐƯỢC THÊM VÀO ĐÂY ===
        # Liên kết mock_cursor.connection ngược lại với mock_conn
        mock_cursor.connection = mock_conn
        
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Giả lập NotificationService
        with patch('order_management_module.NotificationService') as MockNotificationService:
            mock_notification_instance = MockNotificationService.return_value
            
            # Dùng yield để trả về các đối tượng mock cho test case
            yield mock_cursor, mock_notification_instance

class TestOrderService:
    """Nhóm các test case cho OrderService."""
    
    def test_update_status_success(self, mock_services):
        """Kiểm thử trường hợp cập nhật thành công."""
        mock_cursor, mock_notification = mock_services
        
        # Giả lập: tìm thấy đơn hàng với customer_id = 1
        mock_cursor.fetchone.return_value = (1,) 
        # Giả lập: câu lệnh UPDATE thành công, ảnh hưởng 1 dòng
        mock_cursor.rowcount = 1

        order_service = order_management_module.OrderService()
        result = order_service.update_order_status(order_id=1, new_status='Shipped')

        # Assert (Kiểm tra kết quả)
        assert result is True
        mock_cursor.connection.commit.assert_called_once()
        mock_notification.send_update_notification.assert_called_once_with(1, 'Shipped')

    def test_update_status_order_not_found(self, mock_services):
        """Kiểm thử trường hợp không tìm thấy đơn hàng."""
        mock_cursor, mock_notification = mock_services
        
        # Giả lập: không tìm thấy đơn hàng
        mock_cursor.fetchone.return_value = None

        order_service = order_management_module.OrderService()
        result = order_service.update_order_status(order_id=999, new_status='Shipped')

        # Assert
        assert result is False
        mock_cursor.connection.rollback.assert_called_once()
        mock_notification.send_update_notification.assert_not_called()

    def test_update_status_db_error_on_update(self, mock_services):
        """Kiểm thử trường hợp CSDL báo lỗi khi đang UPDATE."""
        mock_cursor, mock_notification = mock_services
        
        # Giả lập: tìm thấy đơn hàng
        mock_cursor.fetchone.return_value = (1,)
        # Giả lập: câu lệnh execute thứ hai (UPDATE) gây ra lỗi
        mock_cursor.execute.side_effect = [None, mysql.connector.Error("Lỗi CSDL")]

        order_service = order_management_module.OrderService()
        result = order_service.update_order_status(order_id=1, new_status='Shipped')

        # Assert
        assert result is False
        mock_cursor.connection.rollback.assert_called_once()
        mock_notification.send_update_notification.assert_not_called()
```

![](https://github.com/httthaor/Nhom2-CNPM/blob/905757ceee786aadbd160bc9f77912a9cd1df37e/Labs/Lab08/Lab08_Scr.png)

## 8. Jira Report

**Jira:**
```https://kimt0832.atlassian.net/jira/software/projects/MAOSM/boards/67/backlog?atlOrigin=eyJpIjoiZTI3NTgwMmQxNTJiNDgwNzg0NzExMjEzNThhZmVkYTQiLCJwIjoiaiJ9```

**User Stories:**

- US1: Muốn quản lý sản phẩm
- US2: Muốn quản lý khách hàng
- US3: Muốn quản lý giỏ hàng
- US4: Muốn quản lý đơn hàng
- US5: Muốn quản lý thanh toán
- US6: Muốn giao diện người dùng

**Tasks:**

- Quản lý sản phẩm:
  - Thiết kế csdl cho sản phẩm và danh mục
  - Phát triển API thêm sản phẩm
  - Phát triển API sửa sản phẩm
  - Phát triển API xóa sản phẩm
  - Phát triển API tìm kiếm sản phẩm
  - Phát triển API hiển thị danh mục
  - Kiểm thử chức năng quản lý sản phẩm

- Quản lý khách hàng
  - Thiết kế csdl cho khách hàng
  - Phát triển API đăng ký
  - Phát triển API đăng nhập
  - Phát triển API cập nhật thông tin khách hàng
  - Kiểm thử chức năng quản lý khách hàng

- Quản lý giỏ hàng
  - Thiết kế csdl cho giỏ hàng
  - Phát triển API thêm sản phẩm vào giỏ hàng
  - Phát triển API xóa sản phẩm khỏi giỏ hàng
  - Phát triển API tính tổng tiền giỏ hàng
  - Kiểm thử chức năng giỏ hàng
  - Phát triển trang danh mục sản phẩm
 
- Quản lý đơn hàng
  - Thiết kế csdl cho đơn hàng
  - Phát triển API tạo đơn hàng
  - Phát triển API cập nhật trạng thái đơn hàng
  - Kiểm thử chức năng đơn hàng
 
- Quản lý thanh toán
  - Thiết kế csdl cho thành toán
  - Phát triển API xử lý thanh toán COD
  - Phát triển API mô phỏng thanh toán ví điện tử
  - Kiểm thử chức năng thanh toán
  - Phát triển trang chủ
 
- Giao diện người dùng
  - Phát triển trang giỏ hàng
  - Phát triển trang đơn hàng
  - Phát triển giao diện thanh toán
  - Kiểm thử giao diện người dùng
 
**Ảnh:**
![](https://github.com/httthaor/Nhom2-CNPM/blob/5e06de9ff1f8c45a9c87f7cd685df1916c069ba4/Labs/Lab09/jira1.jpg)
![](https://github.com/httthaor/Nhom2-CNPM/blob/6e848e7b78b6e2e5de70b781c142c3a470489870/Labs/Lab09/jira2.jpg)
![](https://github.com/httthaor/Nhom2-CNPM/blob/6e848e7b78b6e2e5de70b781c142c3a470489870/Labs/Lab09/jira3.jpg)
![](https://github.com/httthaor/Nhom2-CNPM/blob/6e848e7b78b6e2e5de70b781c142c3a470489870/Labs/Lab09/jira4.jpg)


  
  
