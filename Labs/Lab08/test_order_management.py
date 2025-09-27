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
