# HƯỚNG DẪN SỬ DỤNG REPOSITORY HỒ SƠ VỤ ÁN VẮN NGỌC LAN

---

## 1. GIỚI THIỆU CHUNG

Repository này được xây dựng nhằm phục vụ quá trình minh oan vụ án của bà **Vắn Ngọc Lan**, với mục tiêu tập hợp, hệ thống hóa toàn bộ tài liệu, chứng cứ, phân tích pháp lý, đơn từ và các dữ liệu liên quan. Việc tổ chức repository theo tiêu chuẩn và quy trình khoa học giúp mọi thành viên dễ dàng tra cứu, đối chiếu thông tin, phục vụ nghiên cứu, tố tụng hoặc truyền thông minh bạch về vụ án.

---

## 2. CẤU TRÚC THƯ MỤC

Dưới đây là các thư mục chính và loại tài liệu đi kèm:

- **docs/**  
  Chứa các tài liệu tổng quan, báo cáo phân tích, hướng dẫn sử dụng, tổng kết vụ án, hoặc các nghiên cứu pháp lý chuyên đề.

- **legal/**  
  Lưu trữ các văn bản pháp lý gốc như kết luận điều tra, cáo trạng, bản án, văn bản pháp luật liên quan, trích lục điều luật, hoặc các tài liệu pháp lý chuẩn hóa.

- **evidences/**  
  Tập hợp các bằng chứng vật chất, file ghi âm, hình ảnh, video, sao kê tài khoản, biên bản, tài liệu xác thực, tài liệu đối chiếu, bảng phân tích dòng tiền, v.v.

- **petitions/**  
  Bao gồm các đơn tố cáo, khiếu nại, kiến nghị, kháng nghị, đề nghị giám đốc thẩm, văn bản gửi các cơ quan chức năng hoặc luật sư.

- **templates/**  
  Chứa các mẫu văn bản, mẫu đơn, mẫu biên bản, checklist, form nhập liệu chuẩn để hỗ trợ quá trình chuẩn hóa dữ liệu và báo cáo.

- **resources/**  
  Tài liệu tham khảo, hướng dẫn sử dụng, từ điển dữ liệu, quy chế quản lý repository, tài liệu hướng dẫn đóng góp, chuẩn hóa thuật ngữ, v.v.

---

## 3. QUY TẮC ĐẶT TÊN FILE

- **Chuẩn đặt tên:**  
  `YYYY-MM-DD_Loai_tai_lieu_Mo_ta_ngan.[định dạng]`
  - **YYYY-MM-DD**: Ngày phát sinh hoặc phát hành tài liệu (nếu không rõ ngày, dùng năm hoặc tháng).
  - **Loại_tai_lieu**: Phân loại tài liệu theo chức năng (evidences, legal, petition, report, v.v.).
  - **Mo_ta_ngan**: Tóm tắt ngắn gọn nội dung, giúp nhận diện nhanh khi duyệt file.
  - **[định dạng]**: Đuôi file, ví dụ: md, pdf, docx, jpg, png, mp3, v.v.

- **Ví dụ:**
  - `2023-10-31_Tuong_trinh_su_kien_Bat_giu_trai_phap_luat.md`
  - `2024-03-27_Bien_ban_ma_boi_thuong.pdf`
  - `2023-02-20_Sao_ke_VPBank_VanNgocLan.pdf`

- **Tầm quan trọng:**  
  Quy tắc này giúp tìm kiếm, lọc dữ liệu nhanh chóng, đảm bảo tính nhất quán và dễ dàng đối chiếu thông tin giữa các tài liệu liên quan.

---

## 4. HƯỚNG DẪN TÌM KIẾM VÀ TRUY XUẤT TÀI LIỆU

### a) **Tìm kiếm theo từ khóa, ngày tháng, loại tài liệu**
- Dùng chức năng tìm kiếm (search) của GitHub hoặc trình quản lý file để nhập:
  - Từ khóa nội dung (ví dụ: “bắt giữ”, “khiếu nại”, “bản án”)
  - Ngày tháng (ví dụ: “2023-11” để lọc các tài liệu tháng 11/2023)
  - Loại tài liệu (ví dụ: “evidences”, “legal”, “petitions”)

### b) **Tìm kiếm theo quy tắc đặt tên**
- Tìm file bằng cách ghép các thành tố: ngày phát sinh + chức năng + mô tả ngắn.
- File luôn nằm đúng thư mục chức năng (evidences/, legal/, petitions/ ...).

### c) **Đối chiếu thông tin giữa các file**
- Các văn bản đơn từ thường có mục **Phụ lục** hoặc **STT bằng chứng**.  
  Bạn dùng số thứ tự này để tìm file tương ứng trong thư mục evidences/ hoặc legal/, đảm bảo dữ liệu đồng bộ.
- Khi đọc một phân tích hoặc lập luận pháp lý, tra cứu ID chuẩn hóa (ví dụ #bc001, #nv002, #mt003 ...) trong file [data_dictionary.md](../data_dictionary.md) để hiểu rõ đối tượng được nhắc tới.

### d) **Liên kết chéo và kiểm chứng**
- Nhiều tài liệu có liên kết chéo (hyperlink) tới bằng chứng gốc hoặc file phân tích liên quan.
- Đọc kỹ phần tham chiếu ở cuối hoặc các link nội bộ để nắm rõ mối liên hệ.

---

## 5. HƯỚNG DẪN ĐÓNG GÓP VÀ CẬP NHẬT

- **Thêm tài liệu mới:**  
  Đặt tên file theo chuẩn, lưu đúng thư mục chức năng, ghi rõ nguồn gốc, ngày tháng và chú thích nếu cần.
- **Cập nhật thông tin:**  
  Sửa đổi hoặc bổ sung thông tin phải ghi chú rõ nội dung cập nhật, lý do, người thực hiện và ngày cập nhật trong phần đầu tài liệu.
- **Đề xuất thay đổi:**  
  Gửi Pull Request (PR) kèm mô tả chi tiết nội dung đề xuất sửa đổi. Đảm bảo không xóa hoặc thay đổi dữ liệu gốc mà không có ý kiến thống nhất của quản trị viên.
- **Kiểm tra trùng lặp:**  
  Trước khi thêm mới, kiểm tra đã có tài liệu tương tự chưa để tránh lặp lại.
- **Tuân thủ chuẩn hóa thuật ngữ:**  
  Luôn sử dụng đúng ID chuẩn hóa (ví dụ: #nv001, #bc003, #vp005) để đảm bảo các tài liệu liên kết chính xác với nhau.

---

## 6. LIÊN HỆ VÀ HỖ TRỢ

- **Quản trị viên repository:**  
  - [Tên quản trị viên]: Hoanchuhp123 (GitHub)
  - Email: hoanchu.hp@gmail.com
- **Yêu cầu hỗ trợ hoặc góp ý:**  
  - Tạo Issue trên repository với nội dung chi tiết.
  - Hoặc liên hệ qua email, đảm bảo ghi rõ nội dung cần hỗ trợ, file/tài liệu liên quan và nhu cầu cụ thể.
- **Tài liệu tham khảo, hướng dẫn thêm:**  
  - Xem các file trong resources/ hoặc docs/ để biết thêm về quy trình chuẩn hóa, từ điển dữ liệu và các ví dụ mẫu.

---

**Mọi đóng góp, đề xuất chỉnh sửa đều được hoan nghênh nhằm hoàn thiện và bảo vệ công lý cho vụ án của bà Vắn Ngọc Lan.**  