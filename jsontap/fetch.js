laydulieuApi = () => {
    fetch('https://api.muaviaxmdt.com/v1/public/category/list')
    .then(response => {
        if (!response.ok) {
            throw new Error('Có lỗi khi lấy dữ liệu từ API.');
        }
        return response.json();
    })
    .then(data => {
        // Biến để tích lũy các hàng HTML
        let categoryRows = '';
        
        // Duyệt qua mỗi mục trong mảng data.data và tạo các hàng HTML tương ứng
        data.data.forEach(item => {
            const category = item.category;
            const categoryInfo = `
                <tr>
                    <td>${category.name}</td>
                    <td>${category.price}</td>
                    <td>${category.note}</td>
                    <td>${category.totalProduct}</td>
                    <td><button type="button" class="btn btn-primary">Mua Ngay</button> </td>
                </tr>
            `;
            // Thêm hàng vào biến categoryRows
            categoryRows += categoryInfo;
        });
        
        // Chèn tất cả các hàng vào tbody của bảng
        document.getElementById("data-table").innerHTML = categoryRows;
    })
    .catch(error => {
        console.error("Đã xảy ra lỗi:", error);
    });
}

// Gọi hàm để lấy dữ liệu từ API
laydulieuApi();
