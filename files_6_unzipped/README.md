# Dự án Quản lý Tài liệu Vụ án Vắn Ngọc Lan

## Mục tiêu dự án

Hệ thống hóa, lưu trữ, phân loại, cập nhật và chia sẻ toàn bộ tài liệu liên quan đến vụ án Vắn Ngọc Lan một cách khoa học, minh bạch và thuận tiện cho việc tìm kiếm, đối chiếu, hỗ trợ pháp lý và bảo vệ quyền lợi hợp pháp của các bên liên quan.

## Đối tượng sử dụng

- Thành viên gia đình, người hỗ trợ pháp lý và luật sư của bà Vắn Ngọc Lan
- Các chuyên gia pháp lý, nhà hoạt động xã hội quan tâm vụ án
- Cơ quan, tổ chức, cá nhân được ủy quyền tiếp nhận, xử lý, đánh giá tài liệu vụ án

## Cấu trúc thư mục

```
VanNgocLan-Case-Documents/
├── README.md
├── docs/                 # Tài liệu chính, tóm tắt, phân tích, luận cứ pháp lý
│   ├── 2025-06_Tong_hop_luan_cu.md
│   ├── 2025-06_Tom_tat_vu_an.md
│   └── ...
├── legal/                # Hồ sơ pháp lý: bản án, kết luận điều tra, cáo trạng...
│   ├── 2024-07-15_Ban_an_so_tham.pdf
│   ├── 2024-09-24_Ban_an_phuc_tham.pdf
│   ├── 2024-04-17_Ket_luan_dieu_tra.pdf
│   └── ...
├── evidences/            # Chứng cứ: ghi âm, hình ảnh, sao kê, tin nhắn, video...
│   ├── 2023-10-31_Video_bat_giu_trai_phap_luat.mp4
│   ├── 2023-10-25_Ghi_am_dtv_Vuong_de_doa.m4a
│   └── ...
├── petitions/            # Đơn từ: khiếu nại, kháng cáo, tố cáo, đề nghị...
│   ├── 2024-06-28_Don_khieu_nai_KLDT.pdf
│   ├── 2024-09-16_Don_khang_cao_bo_sung.pdf
│   └── ...
├── templates/            # Mẫu đơn, checklist, biểu mẫu pháp lý
│   ├── Mau_don_khieu_nai.docx
│   ├── Checklist_buoc_phap_ly.xlsx
│   └── ...
├── resources/            # Tài liệu tham khảo, liên kết ngoài, hướng dẫn sử dụng
│   ├── Huong_dan_su_dung_repo.md
│   ├── Tai_lieu_lien_quan.pdf
│   └── ...
└── .github/              # Quy trình đóng góp, issue templates (nếu cần)
```

## Quy tắc đặt tên file/thư mục

**Cấu trúc chung:**  
`YYYY-MM-DD_Loai_tai_lieu_Mo_ta_ngan.[định dạng]`

- **YYYY-MM-DD**: Ngày phát hành, lập hoặc ngày sự kiện liên quan (năm-tháng-ngày), chỉ cần năm-tháng nếu không rõ ngày.
- **Loại tài liệu**: Một từ khóa tiếng Việt không dấu hoặc tiếng Anh (Ban_an, Ket_luan, Don_khieu_nai, Ghi_am, Video, Sao_ke, Tom_tat, Luan_cu, v.v.).
- **Mo ta ngan**: Mô tả ngắn gọn nội dung hoặc sự kiện (không dấu, viết liền, dưới 25 ký tự).
- **Định dạng**: pdf, docx, mp3, mp4, xlsx, md...

**Ví dụ:**
- `2024-07-15_Ban_an_so_tham.pdf`
- `2023-10-31_Video_bat_giu_trai_phap_luat.mp4`
- `2024-09-16_Don_khang_cao_bo_sung.docx`
- `2025-06_Tong_hop_luan_cu.md`

**Lưu ý:**
- Các thư mục nên đặt tên bằng tiếng Anh hoặc tiếng Việt không dấu, ngắn gọn, thể hiện nhóm tài liệu.
- Nếu một tài liệu có nhiều phiên bản, thêm hậu tố `_v1`, `_v2` hoặc `_final` ở cuối tên file.
- Với chứng cứ điện tử, nên lưu kèm file text/mô tả đi kèm (ví dụ: `2023-10-25_Ghi_am_dtv_Vuong_de_doa.txt`).
- Nên tạo file tổng hợp hoặc index trong mỗi thư mục để liệt kê các tài liệu quan trọng (có thể là `README.md` nhỏ cho từng thư mục con).

## Hướng dẫn đóng góp tài liệu

1. Thêm tài liệu đúng vào thư mục tương ứng.
2. Đặt tên file theo quy tắc ở trên.
3. Nếu là tài liệu mới hoặc quan trọng, cập nhật thêm vào file index hoặc README.md của thư mục.
4. Nếu là thành viên mới, có thể mở issue để đề xuất bổ sung/tái cấu trúc thư mục nếu cần.

## Đóng góp & liên hệ

- Mọi đóng góp đều hoan nghênh, vui lòng giữ nguyên cấu trúc và quy tắc đặt tên để toàn bộ dự án luôn đồng nhất, dễ tra cứu.
- Mọi thắc mắc/góp ý liên hệ:  
  Quản trị viên: [Tên bạn]  
  Email: [Email liên hệ]

---

**Chú ý:**  
Tất cả tài liệu đăng tải lên repository cần kiểm tra kỹ thông tin cá nhân, dữ liệu nhạy cảm, chỉ công khai khi phù hợp với quy định pháp luật và có sự đồng ý của các bên liên quan.