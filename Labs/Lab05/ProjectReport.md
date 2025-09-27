# Project Report - Mini App Quản Lý Đơn Hàng Cho Shop Online

## 1. Giới thiệu

**Đề tài: Mini app quản lý đơn hàng cho shop online**

Dự án này được xây dựng nhằm minh họa quy trình phát triển phần mềm từ giai đoạn phân tích yêu cầu → thiết kế UML → cài đặt giao diện → tích hợp & báo cáo.

**Mini app quản lý đơn hàng giúp shop online:** 
- Quản lý sản phẩm và khách hàng
- Tạo, xử lý, và thanh toán đơn hàng

**Công nghệ sử dụng:**
- Diagram: UML (Use Case, Sequence)
- Front-end: HTML, CSS, JavaScript 
- Quản lý version: Git + GitHub.

## 2. Chức năng chính của phần mềm 
- Quản lý sản phẩm: thêm, sửa, xóa, tìm kiếm, hiển thị danh mục. 
- Quản lý khách hàng: đăng ký, đăng nhập, cập nhật thông tin. 
- Quản lý giỏ hàng: thêm/xóa sản phẩm, tính tổng tiền. 
- Quản lý đơn hàng: tạo đơn, cập nhật trạng thái (pending, shipping, completed, 
canceled). 
- Quản lý thanh toán: COD, ví điện tử (mô phỏng). 
- Giao diện người dùng: trang chủ, danh mục sản phẩm, giỏ hàng, đơn hàng.

## 3. Use Case Diagram
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

## 3. Sequence Diagram
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

## 4. Form Login

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



