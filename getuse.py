import requests
import json

# Replace 'desired_username' with the actual username you want to search for
username = 'thuyen'

# Gửi yêu cầu GET đến URL
user_query_res = requests.get(f"https://www.instagram.com/web/search/topsearch/?query={username}")

# Kiểm tra xem yêu cầu có thành công không
if user_query_res.status_code == 200:
    # Parse dữ liệu JSON từ nội dung trả về
    user_query_json = user_query_res.json()

    # Kiểm tra xem có thông tin về người dùng không
    if 'users' in user_query_json and user_query_json['users']:
        # Lấy giá trị username từ JSON và lưu vào file
        with open('usernames.txt', 'w') as file:
            for user_info in user_query_json['users']:
                if 'user' in user_info and 'username' in user_info['user']:
                    username = user_info['user']['username']
                    file.write(username + '\n')
    else:
        print("Dữ liệu JSON không có thông tin về người dùng.")
else:
    print(f"Yêu cầu thất bại với mã trạng thái {user_query_res.status_code}.")
