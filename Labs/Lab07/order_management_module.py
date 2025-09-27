Try AI directly in your favorite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₫489,000 ₫0 for 1 month
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
