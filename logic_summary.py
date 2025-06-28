import os
import json
from glob import glob

def scan_json_files(root_dir):
    """Tìm và đọc tất cả file JSON trong thư mục và trả về danh sách dữ liệu."""
    json_data = []
    for path in glob(os.path.join(root_dir, '**', '*.json'), recursive=True):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                json_data.append({'path': path, 'data': data})
        except Exception as e:
            print(f"Lỗi đọc {path}: {e}")
    return json_data

def summary_report(json_data):
    """Tạo báo cáo tổng hợp nhanh từ các file JSON."""
    lines = []
    lines.append("TỔNG HỢP DỮ LIỆU JSON TRONG DỰ ÁN:\n")
    for item in json_data:
        lines.append(f"- File: {item['path']}")
        if isinstance(item['data'], dict):
            lines.append(f"  Số trường: {len(item['data'])}")
            lines.append(f"  Các trường chính: {list(item['data'].keys())[:5]}")
        elif isinstance(item['data'], list):
            lines.append(f"  Số phần tử: {len(item['data'])}")
            if item['data'] and isinstance(item['data'][0], dict):
                lines.append(f"  Các trường chính: {list(item['data'][0].keys())[:5]}")
        lines.append("")
    report = "\n".join(lines)
    print(report)
    return report

def scan_markdown_files(root_dir):
    """Tìm và đọc tất cả file Markdown trong thư mục."""
    md_files = []
    for path in glob(os.path.join(root_dir, '**', '*.md'), recursive=True):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                md_files.append({'path': path, 'content': content})
        except Exception as e:
            print(f"Lỗi đọc {path}: {e}")
    return md_files

def summary_markdown(md_files):
    lines = []
    lines.append("TỔNG HỢP FILE MARKDOWN TRONG DỰ ÁN:\n")
    for item in md_files:
        lines.append(f"- File: {item['path']}")
        file_lines = item['content'].splitlines()
        headings = [line.strip() for line in file_lines if line.strip().startswith('#')]
        lines.append(f"  Số dòng: {len(file_lines)}")
        lines.append(f"  Heading chính: {headings[:3]}")
        lines.append("")
    report = "\n".join(lines)
    print(report)
    return report

def scan_text_files(root_dir):
    """Tìm và đọc tất cả file text (.txt) trong thư mục."""
    txt_files = []
    for path in glob(os.path.join(root_dir, '**', '*.txt'), recursive=True):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                txt_files.append({'path': path, 'lines': lines})
        except Exception as e:
            print(f"Lỗi đọc {path}: {e}")
    return txt_files

def summary_text(txt_files):
    lines = []
    lines.append("TỔNG HỢP FILE TEXT TRONG DỰ ÁN:\n")
    for item in txt_files:
        lines.append(f"- File: {item['path']}")
        lines.append(f"  Số dòng: {len(item['lines'])}")
        lines.append(f"  Số ký tự: {sum(len(line) for line in item['lines'])}")
        if item['lines']:
            lines.append(f"  Dòng đầu: {item['lines'][0].strip()}")
        lines.append("")
    report = "\n".join(lines)
    print(report)
    return report

def main():
    import sys
    root_dir = '.'
    json_data = scan_json_files(root_dir)
    md_files = scan_markdown_files(root_dir)
    txt_files = scan_text_files(root_dir)
    report1 = summary_report(json_data)
    report2 = summary_markdown(md_files)
    report3 = summary_text(txt_files)
    # Ghi ra file tổng hợp
    with open('project_summary.txt', 'w', encoding='utf-8') as f:
        f.write(report1 + '\n' + report2 + '\n' + report3)

    # Tìm kiếm theo từ khóa nếu có tham số
    if len(sys.argv) > 1:
        keyword = sys.argv[1].lower()
        print(f"\nKẾT QUẢ TÌM KIẾM TỪ KHÓA: '{keyword}'\n")
        results = []
        # Tìm trong JSON
        for item in json_data:
            found = False
            if isinstance(item['data'], dict):
                for v in item['data'].values():
                    if keyword in str(v).lower():
                        found = True
                        break
            elif isinstance(item['data'], list):
                for entry in item['data']:
                    if keyword in str(entry).lower():
                        found = True
                        break
            if found:
                result = f"[JSON] {item['path']}"
                print(result)
                results.append(result)
        # Tìm trong Markdown
        for item in md_files:
            if keyword in item['content'].lower():
                result = f"[MD] {item['path']}"
                print(result)
                results.append(result)
        # Tìm trong Text
        for item in txt_files:
            for line in item['lines']:
                if keyword in line.lower():
                    result = f"[TXT] {item['path']}"
                    print(result)
                    results.append(result)
                    break
        # Ghi kết quả ra file
        if results:
            with open('search_results.txt', 'w', encoding='utf-8') as f:
                f.write(f"KẾT QUẢ TÌM KIẾM TỪ KHÓA: '{keyword}'\n\n")
                for line in results:
                    f.write(line + '\n')
            print(f"\nKết quả đã được lưu vào file search_results.txt\n")
        else:
            print("\nKhông tìm thấy kết quả phù hợp.\n")

if __name__ == "__main__":
    main()
