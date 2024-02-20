import requests
from bs4 import BeautifulSoup
import threading

def get_instagram_info(username):
    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'dpr': '1.25',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.217", "Microsoft Edge";v="120.0.2210.133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/120.0.0.0',
        'viewport-width': '307',
    }

    params = {
        'hl': 'en',
    }

    response = requests.get(f'https://www.instagram.com/{username}/', params=params, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', {'name': 'description'})

        if meta_tag:
            description_content = meta_tag.get('content')
            print(f"Thông tin tài khoản của {username} là: {description_content}")
        else:
            print(f"Không tìm thấy thẻ <meta> với thuộc tính content cụ thể cho {username}.")
    else:
        print(f"Yêu cầu thất bại với mã trạng thái {response.status_code} cho {username}")

def process_usernames():
    while True:
        # Lock to prevent race conditions when accessing the file
        with lock:
            if not usernames:
                break  # No more users, exit the loop
            user = usernames.pop(0)

        # Process the user
        get_instagram_info(user)

def main():
    global usernames  # Make usernames a global variable
    global lock  # Global lock to prevent race conditions

    # Nhập số lượng luồng
    num_threads = int(input("Nhap Vao So Luong Luong: "))

    # Mở file user.txt để đọc tên người dùng
    with open('user.txt', 'r') as file:
        usernames = file.read().splitlines()

    # Tạo và khởi chạy các luồng
    lock = threading.Lock()
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=process_usernames)
        threads.append(thread)
        thread.start()

    # Chờ cho tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()