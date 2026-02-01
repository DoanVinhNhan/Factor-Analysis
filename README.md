# Phân Tích Nhân Tố (Factor Analysis) - Nhóm 04

## 1. Giới thiệu chung
Đây là mã nguồn và tài liệu báo cáo cho bài tập lớn môn **Phân tích số liệu** (Mã lớp: 163626) tại **Đại học Bách khoa Hà Nội**.

- **Đề tài:** Phân tích nhân tố khám phá (Exploratory Factor Analysis - EFA) trên bộ dữ liệu về sự hài lòng của hành khách hàng không.
- **Học kỳ:** 2025.1
- **Giảng viên hướng dẫn:** ThS. Lê Xuân Lý

## 2. Danh sách thành viên (Nhóm 04)

| STT | Họ và tên | MSSV |
|:---:|:---|:---:|
| 1 | Đoàn Vĩnh Nhân | 20237376 |
| 2 | Nguyễn Thị Huệ | 20237439 |
| 3 | Lê Quang Huy | 20237344 |
| 4 | Vũ Quang Vinh | 20237408 |
| 5 | Đặng Thị Thùy Dương | 20237318 |
| 6 | Nguyễn Hải Long | 20237355 |
| 7 | Nguyễn Quang Dương | 20237320 |
| 8 | Hoàng Công Hậu | 20237326 |

## 3. Cấu trúc thư mục

```text
├── data/
│   ├── train.csv          # Dữ liệu huấn luyện
│   ├── test.csv           # Dữ liệu kiểm tra
│   └── dataset.csv        # Dữ liệu gốc
├── airline.ipynb          # Notebook phân tích chính
├── factor_analysis.ipynb  # Notebook thực hiện thuật toán Factor Analysis
├── utils.py               # Các hàm tiện ích hỗ trợ (xử lý dữ liệu, vẽ biểu đồ)
├── Factor_Analysis...pdf  # Báo cáo chi tiết (PDF)
└── README.md              # File hướng dẫn này
```

## 4. Yêu cầu cài đặt (Prerequisites)

Dự án sử dụng ngôn ngữ **Python** và các thư viện phân tích dữ liệu. Để chạy được code, bạn cần cài đặt các gói sau:

- Python 3.8+
- Jupyter Notebook
- Các thư viện cần thiết:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn factor_analyzer
```

## 5. Phương pháp nghiên cứu
Dự án áp dụng mô hình phân tích nhân tố (Factor Analysis) với các bước chính:
1. **Kiểm định dữ liệu:** Sử dụng kiểm định Bartlett và chỉ số KMO (Kaiser-Meyer-Olkin).
2. **Trích xuất nhân tố:** Xác định số lượng nhân tố tối ưu dựa trên Eigenvalues (Scree Plot).
3. **Phép xoay nhân tố:** Sử dụng phương pháp xoay (ví dụ: Varimax/Promax) để làm rõ cấu trúc dữ liệu.
4. **Mô hình toán học:**
   Mô hình trực giao có dạng:
   $$X = \mu + LF + \epsilon$$
   Trong đó:
   - $X$: Vector biến quan sát.
   - $L$: Ma trận tải trọng nhân tố (Loading matrix).
   - $F$: Vector các nhân tố chung (Common factors).
   - $\epsilon$: Vector sai số riêng (Specific factors).

## 6. Kết quả
- Đã trích xuất được các nhân tố chính ảnh hưởng đến sự hài lòng (Dịch vụ trên chuyến bay, Thủ tục mặt đất, v.v.).
- Đánh giá độ tin cậy của thang đo thông qua Cronbach's Alpha.
